from pydantic import BaseModel, EmailStr, Field


class AgencySmtpSettingsRead(BaseModel):
    enabled: bool = False
    host: str = ""
    port: int = 587
    use_tls: bool = True
    use_ssl: bool = False
    username: str = ""
    from_email: str = ""
    from_name: str = ""
    password_configured: bool = False


class AgencySmtpSettingsUpdate(BaseModel):
    enabled: bool | None = None
    host: str | None = None
    port: int | None = Field(default=None, ge=1, le=65535)
    use_tls: bool | None = None
    use_ssl: bool | None = None
    username: str | None = None
    password: str | None = None
    from_email: str | None = None
    from_name: str | None = None


class SmtpTestEmailRequest(BaseModel):
    to_email: EmailStr | None = None


class MessageResponse(BaseModel):
    message: str
