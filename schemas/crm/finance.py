from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmCreatedAtRead, CrmORMModel


class QuotationBase(BaseModel):
    itinerary_id: UUID
    amount: Decimal = Field(..., ge=0)
    status: str = Field(default="DRAFT", max_length=32)


class QuotationCreate(QuotationBase):
    pass


class QuotationUpdate(BaseModel):
    itinerary_id: UUID | None = None
    amount: Decimal | None = Field(default=None, ge=0)
    status: str | None = Field(default=None, max_length=32)


class QuotationRead(CrmCreatedAtRead, QuotationBase):
    agency_id: UUID


class InvoiceBase(BaseModel):
    booking_id: UUID
    invoice_number: str = Field(..., min_length=1, max_length=64)
    amount: Decimal = Field(..., ge=0)
    due_date: datetime
    status: str = Field(default="UNPAID", max_length=32)


class InvoiceCreate(InvoiceBase):
    pass


class InvoiceUpdate(BaseModel):
    booking_id: UUID | None = None
    invoice_number: str | None = Field(default=None, min_length=1, max_length=64)
    amount: Decimal | None = Field(default=None, ge=0)
    due_date: datetime | None = None
    status: str | None = Field(default=None, max_length=32)


class InvoiceRead(CrmCreatedAtRead, InvoiceBase):
    agency_id: UUID


class PaymentBase(BaseModel):
    invoice_id: UUID
    amount: Decimal = Field(..., ge=0)
    payment_method: str = Field(..., min_length=1, max_length=32)
    transaction_reference: str | None = Field(default=None, max_length=255)
    payment_date: datetime | None = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    invoice_id: UUID | None = None
    amount: Decimal | None = Field(default=None, ge=0)
    payment_method: str | None = Field(default=None, min_length=1, max_length=32)
    transaction_reference: str | None = Field(default=None, max_length=255)
    payment_date: datetime | None = None


class PaymentRead(CrmORMModel):
    id: UUID
    agency_id: UUID
    invoice_id: UUID
    amount: Decimal
    payment_method: str
    transaction_reference: str | None
    payment_date: datetime


class ExpenseBase(BaseModel):
    booking_id: UUID | None = None
    amount: Decimal = Field(..., ge=0)
    category: str = Field(..., min_length=1, max_length=64)
    description: str | None = None
    expense_date: datetime | None = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    booking_id: UUID | None = None
    amount: Decimal | None = Field(default=None, ge=0)
    category: str | None = Field(default=None, min_length=1, max_length=64)
    description: str | None = None
    expense_date: datetime | None = None


class ExpenseRead(CrmORMModel):
    id: UUID
    agency_id: UUID
    booking_id: UUID | None
    amount: Decimal
    category: str
    description: str | None
    expense_date: datetime


class VendorPayoutBase(BaseModel):
    vendor_id: UUID
    amount: Decimal = Field(..., ge=0)
    payment_date: datetime | None = None
    status: str = Field(default="PAID", max_length=32)


class VendorPayoutCreate(VendorPayoutBase):
    pass


class VendorPayoutUpdate(BaseModel):
    vendor_id: UUID | None = None
    amount: Decimal | None = Field(default=None, ge=0)
    payment_date: datetime | None = None
    status: str | None = Field(default=None, max_length=32)


class VendorPayoutRead(CrmORMModel):
    id: UUID
    agency_id: UUID
    vendor_id: UUID
    amount: Decimal
    payment_date: datetime
    status: str
