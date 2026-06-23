from sqlalchemy.orm import Session, selectinload

from models.crm.vendors import Vendor, VendorPackage, VendorRate, VendorService
from schemas.crm.vendor import VendorListRead, VendorRead


def vendor_query_with_nested(db: Session):
    return db.query(Vendor).options(
        selectinload(Vendor.services).selectinload(VendorService.rates),
        selectinload(Vendor.packages).selectinload(VendorPackage.rates),
    )


def vendor_to_read(vendor: Vendor) -> VendorRead:
    return VendorRead.model_validate(vendor)


def vendor_to_list_read(vendor: Vendor) -> VendorListRead:
    return VendorListRead.model_validate(vendor)


def sync_vendor_services(db: Session, vendor: Vendor, services: list) -> None:
    vendor.services.clear()
    db.flush()
    for service_data in services:
        rates = service_data.rates if hasattr(service_data, "rates") else service_data.get("rates", [])
        service_fields = (
            service_data.model_dump(exclude={"rates"})
            if hasattr(service_data, "model_dump")
            else {k: v for k, v in service_data.items() if k != "rates"}
        )
        service = VendorService(vendor_id=vendor.id, **service_fields)
        db.add(service)
        db.flush()
        for rate_data in rates:
            rate_fields = rate_data.model_dump() if hasattr(rate_data, "model_dump") else rate_data
            db.add(VendorRate(vendor_service_id=service.id, vendor_package_id=None, **rate_fields))


def sync_vendor_packages(db: Session, vendor: Vendor, packages: list) -> None:
    vendor.packages.clear()
    db.flush()
    for package_data in packages:
        rates = package_data.rates if hasattr(package_data, "rates") else package_data.get("rates", [])
        package_fields = (
            package_data.model_dump(exclude={"rates"})
            if hasattr(package_data, "model_dump")
            else {k: v for k, v in package_data.items() if k != "rates"}
        )
        package = VendorPackage(vendor_id=vendor.id, **package_fields)
        db.add(package)
        db.flush()
        for rate_data in rates:
            rate_fields = rate_data.model_dump() if hasattr(rate_data, "model_dump") else rate_data
            db.add(VendorRate(vendor_service_id=None, vendor_package_id=package.id, **rate_fields))
