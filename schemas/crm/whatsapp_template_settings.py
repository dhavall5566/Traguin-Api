from pydantic import BaseModel, Field


class WhatsAppTemplateCatalogEntry(BaseModel):
    id: str
    subject: str
    whatsapp_enabled: bool
    audience: str
    whatsapp_text: str = ""
    default_template_id: str = ""
    default_template_name: str = ""


class AgencyWhatsAppTemplateSettingsRead(BaseModel):
    default_template_id: str = ""
    default_template_name: str = ""
    template_language: str = "en"
    overrides: dict[str, str] = Field(default_factory=dict)
    env_default_template_id: str = ""
    env_default_template_name: str = ""
    env_template_language: str = "en"
    sender_display_phone: str = ""


class AgencyWhatsAppTemplateSettingsUpdate(BaseModel):
    default_template_id: str | None = None
    default_template_name: str | None = None
    template_language: str | None = Field(default=None, min_length=2, max_length=16)
    overrides: dict[str, str] | None = None


class WhatsAppTemplateTestRequest(BaseModel):
    catalog_id: str = Field(min_length=1, max_length=64)
    to_phone: str | None = Field(default=None, max_length=32)
    template_override: str | None = Field(default=None, max_length=128)
