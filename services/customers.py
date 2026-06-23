from models.crm.customers import Customer
from schemas.crm.customer import CustomerRead


def customer_to_read(customer: Customer) -> CustomerRead:
    if not (customer.last_name or "").strip():
        customer.last_name = "Visitor"
    return CustomerRead.model_validate(customer)
