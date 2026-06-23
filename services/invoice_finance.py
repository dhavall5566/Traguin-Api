from decimal import Decimal

from sqlalchemy import func
from sqlalchemy.orm import Session

from models.crm.finance import Invoice, Payment


def apply_invoice_status_from_payments(
    db: Session,
    invoice: Invoice,
    *,
    include_pending_amount: Decimal = Decimal("0"),
) -> None:
    """Derive invoice status by summing persisted payments plus an optional pending amount."""
    paid_so_far = (
        db.query(func.coalesce(func.sum(Payment.amount), 0))
        .filter(Payment.invoice_id == invoice.id)
        .scalar()
    )
    total_paid = Decimal(paid_so_far) + include_pending_amount
    if total_paid >= invoice.amount:
        invoice.status = "PAID"
    elif total_paid > Decimal("0"):
        invoice.status = "PARTIALLY_PAID"
    else:
        invoice.status = "UNPAID"
