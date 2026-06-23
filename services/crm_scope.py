from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.crm.bookings import Booking
from models.crm.customers import Customer
from models.crm.finance import Expense, Invoice, Payment, Quotation, VendorPayout
from models.crm.itineraries import Itinerary
from models.crm.tenancy import Permission, Role, User
from models.crm.vendors import Vendor, VendorPackage, VendorService


def get_customer_for_agency(
    db: Session,
    customer_id: UUID,
    agency_id: UUID,
    *,
    include_deleted: bool = False,
) -> Customer | None:
    query = db.query(Customer).filter(Customer.id == customer_id, Customer.agency_id == agency_id)
    if not include_deleted:
        query = query.filter(Customer.is_deleted.is_(False))
    return query.one_or_none()


def require_customer_for_agency(db: Session, customer_id: UUID, agency_id: UUID) -> Customer:
    customer = get_customer_for_agency(db, customer_id, agency_id)
    if customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found.")
    return customer


def get_itinerary_for_agency(db: Session, itinerary_id: UUID, agency_id: UUID) -> Itinerary | None:
    return (
        db.query(Itinerary)
        .filter(Itinerary.id == itinerary_id, Itinerary.agency_id == agency_id)
        .one_or_none()
    )


def require_itinerary_for_agency(db: Session, itinerary_id: UUID, agency_id: UUID) -> Itinerary:
    itinerary = get_itinerary_for_agency(db, itinerary_id, agency_id)
    if itinerary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found.")
    return itinerary


def get_vendor_for_agency(db: Session, vendor_id: UUID, agency_id: UUID) -> Vendor | None:
    return db.query(Vendor).filter(Vendor.id == vendor_id, Vendor.agency_id == agency_id).one_or_none()


def require_vendor_for_agency(db: Session, vendor_id: UUID, agency_id: UUID) -> Vendor:
    vendor = get_vendor_for_agency(db, vendor_id, agency_id)
    if vendor is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found.")
    return vendor


def get_booking_for_agency(db: Session, booking_id: UUID, agency_id: UUID) -> Booking | None:
    return db.query(Booking).filter(Booking.id == booking_id, Booking.agency_id == agency_id).one_or_none()


def require_booking_for_agency(db: Session, booking_id: UUID, agency_id: UUID) -> Booking:
    booking = get_booking_for_agency(db, booking_id, agency_id)
    if booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking not found.")
    return booking


def get_invoice_for_agency(db: Session, invoice_id: UUID, agency_id: UUID) -> Invoice | None:
    return db.query(Invoice).filter(Invoice.id == invoice_id, Invoice.agency_id == agency_id).one_or_none()


def require_invoice_for_agency(db: Session, invoice_id: UUID, agency_id: UUID) -> Invoice:
    invoice = get_invoice_for_agency(db, invoice_id, agency_id)
    if invoice is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invoice not found.")
    return invoice


def get_role_for_agency(db: Session, role_id: UUID, agency_id: UUID) -> Role | None:
    return db.query(Role).filter(Role.id == role_id, Role.agency_id == agency_id).one_or_none()


def require_role_for_agency(db: Session, role_id: UUID, agency_id: UUID) -> Role:
    role = get_role_for_agency(db, role_id, agency_id)
    if role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found.")
    return role


def require_user_for_agency(db: Session, user_id: UUID, agency_id: UUID) -> User:
    user = db.query(User).filter(User.id == user_id, User.agency_id == agency_id, User.is_deleted.is_(False)).one_or_none()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return user


def require_permission(db: Session, permission_id: UUID) -> Permission:
    permission = db.get(Permission, permission_id)
    if permission is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found.")
    return permission


def require_vendor_service_for_agency(db: Session, service_id: UUID, agency_id: UUID) -> VendorService:
    service = (
        db.query(VendorService)
        .join(Vendor)
        .filter(VendorService.id == service_id, Vendor.agency_id == agency_id)
        .one_or_none()
    )
    if service is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor service not found.")
    return service


def require_vendor_package_for_agency(db: Session, package_id: UUID, agency_id: UUID) -> VendorPackage:
    package = (
        db.query(VendorPackage)
        .join(Vendor)
        .filter(VendorPackage.id == package_id, Vendor.agency_id == agency_id)
        .one_or_none()
    )
    if package is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor package not found.")
    return package


def get_quotation_for_agency(db: Session, quotation_id: UUID, agency_id: UUID) -> Quotation | None:
    return db.query(Quotation).filter(Quotation.id == quotation_id, Quotation.agency_id == agency_id).one_or_none()


def get_expense_for_agency(db: Session, expense_id: UUID, agency_id: UUID) -> Expense | None:
    return db.query(Expense).filter(Expense.id == expense_id, Expense.agency_id == agency_id).one_or_none()


def get_payment_for_agency(db: Session, payment_id: UUID, agency_id: UUID) -> Payment | None:
    return db.query(Payment).filter(Payment.id == payment_id, Payment.agency_id == agency_id).one_or_none()


def get_vendor_payout_for_agency(db: Session, payout_id: UUID, agency_id: UUID) -> VendorPayout | None:
    return db.query(VendorPayout).filter(VendorPayout.id == payout_id, VendorPayout.agency_id == agency_id).one_or_none()
