from pydantic import BaseModel


class NotificationMatrixRowRead(BaseModel):
    event: str
    label: str
    customer: bool
    rm: bool
    account: bool
    ops_head: bool
    admin: bool
