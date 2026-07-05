from decimal import Decimal
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from database import get_db
from dependencies.crm_auth import require_agency_scope, require_crm_user
from dependencies.pagination import get_pagination
from models.crm.finance import Expense, Invoice, Payment, Quotation, VendorPayout
from models.crm.tenancy import User
from schemas.crm.finance import (
    ExpenseCreate,
    ExpenseRead,
    ExpenseUpdate,
    InvoiceCreate,
    InvoiceRead,
    InvoiceUpdate,
    PaymentCreate,
    PaymentRead,
    PaymentUpdate,
    QuotationCreate,
    QuotationRead,
    QuotationUpdate,
    VendorPayoutCreate,
    VendorPayoutRead,
    VendorPayoutUpdate,
)
from schemas.pagination import PaginatedResponse
from services.crm_scope import (
    get_booking_for_agency,
    get_expense_for_agency,
    get_invoice_for_agency,
    get_payment_for_agency,
    get_quotation_for_agency,
    get_vendor_payout_for_agency,
    require_itinerary_for_agency,
    require_invoice_for_agency,
    require_vendor_for_agency,
)
from services.crm_audit import audit_create, audit_delete, audit_update, changed_fields_from_payload
from services.invoice_finance import apply_invoice_status_from_payments
from services.whatsapp_notifications import (
    notify_invoice_created_by_id,
    notify_payment_received_by_id,
    notify_quotation_created_by_id,
)
from utils.db import apply_partial_update, commit_or_raise
from utils.pagination import paginate

router = APIRouter()


# --- Quotations ---


@router.get("/quotations", response_model=PaginatedResponse[QuotationRead])
def list_quotations(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Quotation).filter(Quotation.agency_id == agency_id).order_by(Quotation.created_at.desc())
    return paginate(query, limit, offset, transform=QuotationRead.model_validate)


@router.get("/quotations/{quotation_id}", response_model=QuotationRead)
def get_quotation(
    quotation_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    quotation = get_quotation_for_agency(db, quotation_id, agency_id)
    if quotation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quotation not found.")
    return quotation


@router.post("/quotations", response_model=QuotationRead, status_code=status.HTTP_201_CREATED)
def create_quotation(
    payload: QuotationCreate,
    background_tasks: BackgroundTasks,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    require_itinerary_for_agency(db, payload.itinerary_id, agency_id)
    quotation = Quotation(**payload.model_dump(), agency_id=agency_id)
    db.add(quotation)
    commit_or_raise(db)
    db.refresh(quotation)
    background_tasks.add_task(notify_quotation_created_by_id, quotation.id)
    return quotation


@router.patch("/quotations/{quotation_id}", response_model=QuotationRead)
def update_quotation(
    quotation_id: UUID,
    payload: QuotationUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    quotation = get_quotation_for_agency(db, quotation_id, agency_id)
    if quotation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quotation not found.")
    if payload.itinerary_id is not None:
        require_itinerary_for_agency(db, payload.itinerary_id, agency_id)
    apply_partial_update(quotation, payload.model_dump(exclude_unset=True))
    commit_or_raise(db)
    db.refresh(quotation)
    return quotation


@router.delete("/quotations/{quotation_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_quotation(
    quotation_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    quotation = get_quotation_for_agency(db, quotation_id, agency_id)
    if quotation is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quotation not found.")
    db.delete(quotation)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Invoices ---


@router.get("/invoices", response_model=PaginatedResponse[InvoiceRead])
def list_invoices(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Invoice).filter(Invoice.agency_id == agency_id).order_by(Invoice.created_at.desc())
    return paginate(query, limit, offset, transform=InvoiceRead.model_validate)


@router.get("/invoices/{invoice_id}", response_model=InvoiceRead)
def get_invoice(
    invoice_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    invoice = get_invoice_for_agency(db, invoice_id, agency_id)
    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found.")
    return invoice


@router.post("/invoices", response_model=InvoiceRead, status_code=status.HTTP_201_CREATED)
def create_invoice(
    payload: InvoiceCreate,
    background_tasks: BackgroundTasks,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if get_booking_for_agency(db, payload.booking_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")

    existing_open = (
        db.query(Invoice)
        .filter(
            Invoice.agency_id == agency_id,
            Invoice.booking_id == payload.booking_id,
            Invoice.status.in_(("UNPAID", "PARTIALLY_PAID", "OVERDUE")),
        )
        .order_by(Invoice.created_at.desc())
        .first()
    )
    if existing_open is not None:
        return existing_open

    invoice = Invoice(**payload.model_dump(), agency_id=agency_id)
    db.add(invoice)
    db.flush()
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Invoice",
        entity_id=invoice.id,
        details=f"Created invoice {invoice.invoice_number} for ₹{invoice.amount}",
    )
    commit_or_raise(db, unique_fields=("invoice_number",))
    db.refresh(invoice)
    background_tasks.add_task(notify_invoice_created_by_id, invoice.id)
    return invoice


@router.patch("/invoices/{invoice_id}", response_model=InvoiceRead)
def update_invoice(
    invoice_id: UUID,
    payload: InvoiceUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    invoice = get_invoice_for_agency(db, invoice_id, agency_id)
    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found.")
    if payload.booking_id is not None and get_booking_for_agency(db, payload.booking_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    apply_partial_update(invoice, payload.model_dump(exclude_unset=True))
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Invoice",
        entity_id=invoice.id,
        details=f"Updated invoice {invoice.invoice_number}",
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(db, unique_fields=("invoice_number",))
    db.refresh(invoice)
    return invoice


@router.delete("/invoices/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_invoice(
    invoice_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    invoice = get_invoice_for_agency(db, invoice_id, agency_id)
    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Invoice",
        entity_id=invoice.id,
        details=f"Deleted invoice {invoice.invoice_number}",
    )
    db.delete(invoice)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Payments ---


@router.get("/payments", response_model=PaginatedResponse[PaymentRead])
def list_payments(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Payment).filter(Payment.agency_id == agency_id).order_by(Payment.payment_date.desc())
    return paginate(query, limit, offset, transform=PaymentRead.model_validate)


@router.get("/payments/{payment_id}", response_model=PaymentRead)
def get_payment(
    payment_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    payment = get_payment_for_agency(db, payment_id, agency_id)
    if payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")
    return payment


@router.post("/payments", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
def create_payment(
    payload: PaymentCreate,
    background_tasks: BackgroundTasks,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    invoice = require_invoice_for_agency(db, payload.invoice_id, agency_id)
    data = payload.model_dump()
    if data.get("payment_date") is None:
        data.pop("payment_date", None)
    payment = Payment(**data, agency_id=agency_id)
    db.add(payment)
    db.flush()
    apply_invoice_status_from_payments(db, invoice, include_pending_amount=payment.amount)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Payment",
        entity_id=payment.id,
        details=f"Recorded payment ₹{payment.amount} on invoice {invoice.invoice_number} via {payment.payment_method}",
    )
    commit_or_raise(db)
    db.refresh(payment)
    background_tasks.add_task(notify_payment_received_by_id, payment.id)
    return payment


@router.patch("/payments/{payment_id}", response_model=PaymentRead)
def update_payment(
    payment_id: UUID,
    payload: PaymentUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    payment = get_payment_for_agency(db, payment_id, agency_id)
    if payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")
    if payload.invoice_id is not None:
        require_invoice_for_agency(db, payload.invoice_id, agency_id)
    apply_partial_update(payment, payload.model_dump(exclude_unset=True))
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Payment",
        entity_id=payment.id,
        details=f"Updated payment ₹{payment.amount}",
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(db)
    db.refresh(payment)
    return payment


@router.delete("/payments/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(
    payment_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    payment = get_payment_for_agency(db, payment_id, agency_id)
    if payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Payment",
        entity_id=payment.id,
        details=f"Deleted payment ₹{payment.amount}",
    )
    db.delete(payment)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Expenses ---


@router.get("/expenses", response_model=PaginatedResponse[ExpenseRead])
def list_expenses(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(Expense).filter(Expense.agency_id == agency_id).order_by(Expense.expense_date.desc())
    return paginate(query, limit, offset, transform=ExpenseRead.model_validate)


@router.get("/expenses/{expense_id}", response_model=ExpenseRead)
def get_expense(
    expense_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    expense = get_expense_for_agency(db, expense_id, agency_id)
    if expense is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found.")
    return expense


@router.post("/expenses", response_model=ExpenseRead, status_code=status.HTTP_201_CREATED)
def create_expense(
    payload: ExpenseCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    if payload.booking_id is not None and get_booking_for_agency(db, payload.booking_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    data = payload.model_dump()
    if data.get("expense_date") is None:
        data.pop("expense_date", None)
    expense = Expense(**data, agency_id=agency_id)
    db.add(expense)
    db.flush()
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Expense",
        entity_id=expense.id,
        details=f'Created expense "{expense.description}" for ₹{expense.amount}',
    )
    commit_or_raise(db)
    db.refresh(expense)
    return expense


@router.patch("/expenses/{expense_id}", response_model=ExpenseRead)
def update_expense(
    expense_id: UUID,
    payload: ExpenseUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    expense = get_expense_for_agency(db, expense_id, agency_id)
    if expense is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found.")
    if payload.booking_id is not None and get_booking_for_agency(db, payload.booking_id, agency_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    apply_partial_update(expense, payload.model_dump(exclude_unset=True))
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Expense",
        entity_id=expense.id,
        details=f'Updated expense "{expense.description}"',
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(db)
    db.refresh(expense)
    return expense


@router.delete("/expenses/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(
    expense_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    expense = get_expense_for_agency(db, expense_id, agency_id)
    if expense is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="Expense",
        entity_id=expense.id,
        details=f'Deleted expense "{expense.description}" for ₹{expense.amount}',
    )
    db.delete(expense)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# --- Vendor payouts ---


@router.get("/vendor-payouts", response_model=PaginatedResponse[VendorPayoutRead])
def list_vendor_payouts(
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
    pagination: tuple[int, int] = Depends(get_pagination),
):
    limit, offset = pagination
    query = db.query(VendorPayout).filter(VendorPayout.agency_id == agency_id).order_by(VendorPayout.payment_date.desc())
    return paginate(query, limit, offset, transform=VendorPayoutRead.model_validate)


@router.get("/vendor-payouts/{payout_id}", response_model=VendorPayoutRead)
def get_vendor_payout(
    payout_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    db: Session = Depends(get_db),
):
    payout = get_vendor_payout_for_agency(db, payout_id, agency_id)
    if payout is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor payout not found.")
    return payout


@router.post("/vendor-payouts", response_model=VendorPayoutRead, status_code=status.HTTP_201_CREATED)
def create_vendor_payout(
    payload: VendorPayoutCreate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    vendor = require_vendor_for_agency(db, payload.vendor_id, agency_id)
    data = payload.model_dump()
    if data.get("payment_date") is None:
        data.pop("payment_date", None)
    payout = VendorPayout(**data, agency_id=agency_id)
    db.add(payout)
    db.flush()
    if payout.status.upper() == "PAID":
        vendor.ledger_balance = max(Decimal("0.00"), vendor.ledger_balance - payout.amount)
    audit_create(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="VendorPayout",
        entity_id=payout.id,
        details=f"Created vendor payout ₹{payout.amount} to {vendor.name} ({payout.status})",
    )
    commit_or_raise(db)
    db.refresh(payout)
    return payout


@router.patch("/vendor-payouts/{payout_id}", response_model=VendorPayoutRead)
def update_vendor_payout(
    payout_id: UUID,
    payload: VendorPayoutUpdate,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    payout = get_vendor_payout_for_agency(db, payout_id, agency_id)
    if payout is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor payout not found.")
    if payload.vendor_id is not None:
        require_vendor_for_agency(db, payload.vendor_id, agency_id)
    apply_partial_update(payout, payload.model_dump(exclude_unset=True))
    audit_update(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="VendorPayout",
        entity_id=payout.id,
        details=f"Updated vendor payout ₹{payout.amount}",
        changed_fields=changed_fields_from_payload(payload),
    )
    commit_or_raise(db)
    db.refresh(payout)
    return payout


@router.delete("/vendor-payouts/{payout_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendor_payout(
    payout_id: UUID,
    agency_id: UUID = Depends(require_agency_scope),
    current_user: User = Depends(require_crm_user),
    db: Session = Depends(get_db),
):
    payout = get_vendor_payout_for_agency(db, payout_id, agency_id)
    if payout is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor payout not found.")
    audit_delete(
        db,
        agency_id=agency_id,
        user_id=current_user.id,
        entity_type="VendorPayout",
        entity_id=payout.id,
        details=f"Deleted vendor payout ₹{payout.amount}",
    )
    db.delete(payout)
    commit_or_raise(db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
