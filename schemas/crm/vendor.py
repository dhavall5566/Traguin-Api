from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field

from schemas.crm.common import CrmORMModel, CrmTimestampRead


class VendorRateNested(BaseModel):
    rate: Decimal = Field(..., ge=0)
    season_start: datetime
    season_end: datetime


class VendorServiceNested(BaseModel):
    type: str = Field(..., min_length=1, max_length=32)
    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    base_rate: Decimal = Field(default=Decimal("0.00"), ge=0)
    rates: list[VendorRateNested] = Field(default_factory=list)


class VendorPackageNested(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    price: Decimal = Field(default=Decimal("0.00"), ge=0)
    rates: list[VendorRateNested] = Field(default_factory=list)


class VendorRateRead(CrmORMModel):
    id: UUID
    vendor_service_id: UUID | None
    vendor_package_id: UUID | None
    rate: Decimal
    season_start: datetime
    season_end: datetime


class VendorServiceRead(CrmORMModel):
    id: UUID
    vendor_id: UUID
    type: str
    name: str
    description: str | None
    base_rate: Decimal
    rates: list[VendorRateRead] = Field(default_factory=list)


class VendorPackageRead(CrmORMModel):
    id: UUID
    vendor_id: UUID
    name: str
    description: str | None
    price: Decimal
    rates: list[VendorRateRead] = Field(default_factory=list)


class VendorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    type: str = Field(..., min_length=1, max_length=32)
    email: str | None = Field(default=None, max_length=255)
    phone: str | None = Field(default=None, max_length=64)
    address: str | None = None
    ledger_balance: Decimal = Field(default=Decimal("0.00"))


class VendorCreate(VendorBase):
    services: list[VendorServiceNested] = Field(default_factory=list)
    packages: list[VendorPackageNested] = Field(default_factory=list)


class VendorUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=255)
    type: str | None = Field(default=None, min_length=1, max_length=32)
    email: str | None = Field(default=None, max_length=255)
    phone: str | None = Field(default=None, max_length=64)
    address: str | None = None
    ledger_balance: Decimal | None = None
    services: list[VendorServiceNested] | None = None
    packages: list[VendorPackageNested] | None = None


class VendorRead(CrmTimestampRead, VendorBase):
    agency_id: UUID
    services: list[VendorServiceRead] = Field(default_factory=list)
    packages: list[VendorPackageRead] = Field(default_factory=list)


class VendorListRead(CrmTimestampRead, VendorBase):
    """Lightweight row for CRM tables — omits nested services and packages."""

    agency_id: UUID
