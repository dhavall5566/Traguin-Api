"""Build {{Variable}} maps for notification templates."""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from config import settings
from models.crm.bookings import Booking
from models.crm.customers import Customer
from models.crm.finance import Invoice, Payment
from models.crm.leads import Lead
from models.crm.tenancy import Agency, User
from services.customer_inquiry_history import build_customer_inquiry_history
from utils.lead_pipeline import pipeline_status_label

DEFAULT_SUPPORT_PHONE = "+91 98765 43210"
DEFAULT_EMERGENCY_PHONE = "+91 98765 43210"


def _crm_base() -> str:
    return (settings.whatsapp_crm_base_url or "http://localhost:3002").rstrip("/")


def _format_dates(start: date | None, end: date | None = None) -> str:
    if start is None and end is None:
        return "—"
    if start and end and start != end:
        return f"{start.strftime('%d %b %Y')} – {end.strftime('%d %b %Y')}"
    if start:
        return start.strftime("%d %b %Y")
    if end:
        return end.strftime("%d %b %Y")
    return "—"


def _format_money(value: Decimal | float | int | None) -> str:
    if value is None:
        return "—"
    try:
        amount = Decimal(str(value))
    except Exception:
        return "—"
    return f"{amount:,.2f}"


def _lead_destination(lead: Lead) -> str:
    return (lead.travel_destination or lead.title or "—").strip() or "—"


def _guests_label(lead: Lead) -> str:
    adults = lead.adults_count or 0
    children = lead.children_count or 0
    total = adults + children
    if total <= 0:
        return "—"
    if children:
        return f"{total} ({adults} adults, {children} children)"
    return str(total)


def _assignment_links(lead_id: UUID) -> tuple[str, str, str]:
    base = _crm_base()
    crm_link = f"{base}/dashboard/crm?openLead={lead_id}"
    accept = f"{crm_link}&assignmentAction=accept"
    reject = f"{crm_link}&assignmentAction=reject"
    return crm_link, accept, reject


def build_lead_context(
    db: Session,
    lead: Lead,
    *,
    rm_user: User | None = None,
    elapsed_time: str | None = None,
    escalation_level: str | None = None,
    escalation_message: str | None = None,
    attempt_count: str | None = None,
    last_attempt_date: str | None = None,
) -> dict[str, str]:
    agency = db.get(Agency, lead.agency_id)
    agency_name = agency.name if agency else "Traguin"

    if rm_user is None and lead.assigned_to_id:
        rm_user = db.get(User, lead.assigned_to_id)

    rm_name = rm_user.name if rm_user else "Your Traguin Expert"
    rm_phone = (rm_user.phone if rm_user else None) or DEFAULT_SUPPORT_PHONE
    rm_email = (rm_user.email if rm_user else None) or "support@traguin.com"

    customer: Customer | None = None
    if lead.customer_id:
        customer = db.get(Customer, lead.customer_id)

    history = build_customer_inquiry_history(
        db,
        agency_id=lead.agency_id,
        phone=lead.phone,
        email=lead.email,
        customer_id=lead.customer_id,
        current_lead_id=lead.id,
    )

    active = history.last_two_active_enquiries
    active_1 = "—"
    active_2 = "—"
    if len(active) > 0:
        active_1 = f"{active[0].get('lead_code') or active[0]['id']} ({active[0]['status_label']})"
    if len(active) > 1:
        active_2 = f"{active[1].get('lead_code') or active[1]['id']} ({active[1]['status_label']})"

    flags = "; ".join(flag["remark"] for flag in history.flags[:5]) if history.flags else "None"

    crm_link, accept_link, reject_link = _assignment_links(lead.id)

    travel_start = lead.travel_date or lead.arrival_date
    travel_end = lead.travel_date

    return {
        "Customer_Name": f"{lead.first_name} {lead.last_name}".strip(),
        "Temp_ID": lead.lead_code or str(lead.id)[:8].upper(),
        "Customer_ID": (customer.customer_code if customer and customer.customer_code else "—"),
        "Destination": _lead_destination(lead),
        "Travel_Dates": _format_dates(travel_start, travel_end),
        "Travel_Start": _format_dates(travel_start),
        "Travel_End": _format_dates(travel_end),
        "Guests": _guests_label(lead),
        "RM_Name": rm_name,
        "RM_Phone": rm_phone,
        "RM_Email": rm_email,
        "Support_Phone": DEFAULT_SUPPORT_PHONE,
        "Emergency_Phone": DEFAULT_EMERGENCY_PHONE,
        "Phone": lead.phone or "—",
        "Priority": (lead.priority or "Medium").title(),
        "Source_Code": lead.source or "—",
        "Budget": _format_money(lead.value) if lead.value else "—",
        "Inquiry_Count": str(history.inquiry_number or history.total_inquiry_count or 1),
        "Active_Enquiry_1": active_1,
        "Active_Enquiry_2": active_2,
        "Customer_Flags": flags,
        "CRM_Link": crm_link,
        "Accept_Link": accept_link,
        "Reject_Link": reject_link,
        "Elapsed_Time": elapsed_time or "15 minutes",
        "Escalation_Level": escalation_level or "—",
        "Escalation_Message": escalation_message or "—",
        "Attempt_Count": attempt_count or "—",
        "Last_Attempt_Date": last_attempt_date or "—",
        "Agency_Name": agency_name,
        "Nights": "—",
        "Days": "—",
        "Holiday_Type": (lead.travel_type or lead.lead_category or "—"),
        "Total_Amount": _format_money(lead.value),
        "Inclusions_Summary": "As per approved itinerary",
        "Quote_Valid_Till": "—",
        "Booking_ID": "—",
        "Invoice_No": "—",
        "Due_Amount": "—",
        "Due_Date": "—",
        "Payment_Link": crm_link,
        "Receipt_No": "—",
        "Paid_Amount": "—",
        "Payment_Date": "—",
        "Balance_Remaining": "—",
        "Balance_Message": "—",
        "Docs_Link": crm_link,
        "Days_Left": "—",
        "Feedback_Link": f"{_crm_base()}/dashboard/customers",
        "Status_Label": pipeline_status_label(lead.status),
    }


def build_booking_context(
    db: Session,
    booking: Booking,
    *,
    lead: Lead | None = None,
) -> dict[str, str]:
    customer = booking.customer
    if lead is None and customer:
        lead = db.scalar(
            select(Lead)
            .where(
                Lead.agency_id == booking.agency_id,
                Lead.is_deleted.is_(False),
                Lead.customer_id == customer.id,
            )
            .order_by(Lead.updated_at.desc())
            .limit(1)
        )
    base = build_lead_context(db, lead, rm_user=None) if lead else {}
    if customer:
        base["Customer_Name"] = f"{customer.first_name} {customer.last_name}".strip()
        base["Customer_ID"] = customer.customer_code or str(customer.id)[:8].upper()
        base["Phone"] = customer.phone or base.get("Phone", "—")
    base["Booking_ID"] = str(booking.id)[:8].upper()
    base["Status_Label"] = booking.status.replace("_", " ").title()
    return base


def build_invoice_context(
    db: Session,
    invoice: Invoice,
    *,
    lead: Lead | None = None,
    payment: Payment | None = None,
) -> dict[str, str]:
    booking = invoice.booking
    base = build_booking_context(db, booking, lead=lead) if booking else {}
    due = invoice.due_date
    if isinstance(due, datetime):
        due_str = due.strftime("%d %b %Y")
    else:
        due_str = str(due) if due else "—"
    base["Invoice_No"] = invoice.invoice_number
    base["Due_Amount"] = _format_money(invoice.amount)
    base["Due_Date"] = due_str
    if payment:
        base["Receipt_No"] = str(payment.id)[:8].upper()
        base["Paid_Amount"] = _format_money(payment.amount)
        paid_at = payment.payment_date
        base["Payment_Date"] = paid_at.strftime("%d %b %Y") if paid_at else "—"
        try:
            remaining = Decimal(str(invoice.amount)) - Decimal(str(payment.amount))
            base["Balance_Remaining"] = _format_money(max(remaining, Decimal("0")))
            base["Balance_Message"] = (
                "Your booking is fully paid." if remaining <= 0 else "Further payments may be due per your schedule."
            )
        except Exception:
            base["Balance_Remaining"] = "—"
            base["Balance_Message"] = "—"
    return base
