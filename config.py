from pathlib import Path
from uuid import UUID

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

_API_DIR = Path(__file__).resolve().parent
_ENV_FILE = _API_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_ENV_FILE if _ENV_FILE.is_file() else None,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str
    cms_database_url: str | None = None
    crm_database_url: str | None = None
    jwt_secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expire_hours: int = 24
    cors_origins: list[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        "http://localhost:3002",
        "http://127.0.0.1:3002",
        "https://traguin.in",
        "https://www.traguin.in",
    ]
    traguin_default_agency_id: UUID | None = None
    traguin_system_user_id: UUID | None = None
    groq_api_key: str | None = None
    pexels_api_key: str | None = None
    media_upload_dir: Path = _API_DIR / "uploads" / "media"
    media_upload_max_bytes: int = 10 * 1024 * 1024
    api_public_base_url: str | None = None
    # WhatsMarketing: WHATSAPP_API_URL=user_id|api_token (full string is apiToken)
    whatsapp_api_url: str | None = None
    whatsapp_api_base_url: str = "https://app.whatsmarketing.in"
    whatsapp_phone_number_id: str | None = None
    # WhatsMarketing internal template id (preferred when set); from template/list after Meta sync
    whatsapp_template_id: str | None = None
    whatsapp_lead_template: str | None = None
    whatsapp_crm_template: str | None = None
    whatsapp_lead_template_language: str = "en"
    whatsapp_customer_inquiry_template_id: str | None = None
    whatsapp_notifications_enabled: bool = True
    whatsapp_crm_base_url: str | None = None
    whatsapp_use_meta_api: bool = True
    whatsapp_webhook_verify_token: str | None = None

    @field_validator("api_public_base_url", mode="before")
    @classmethod
    def normalize_api_public_base_url(cls, value: str | None) -> str | None:
        if value is None:
            return None
        raw = str(value).strip().rstrip("/")
        return raw or None

    @field_validator("whatsapp_api_url", mode="before")
    @classmethod
    def normalize_whatsapp_api_url(cls, value: str | None) -> str | None:
        if value is None:
            return None
        raw = str(value).strip()
        if not raw or "|" not in raw:
            return raw or None
        prefix, token = raw.split("|", 1)
        # Fix common typo: h21572|token → 21572|token (matches developer console)
        if prefix.startswith("h") and prefix[1:].isdigit():
            prefix = prefix[1:]
        return f"{prefix}|{token.strip()}"

    @field_validator("whatsapp_notifications_enabled", mode="before")
    @classmethod
    def parse_whatsapp_notifications_enabled(cls, value):
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return value

    @field_validator("whatsapp_use_meta_api", mode="before")
    @classmethod
    def parse_whatsapp_use_meta_api(cls, value):
        if isinstance(value, str):
            return value.strip().lower() in {"1", "true", "yes", "on"}
        return value

    @field_validator("pexels_api_key", mode="before")
    @classmethod
    def normalize_pexels_api_key(cls, value: str | None) -> str | None:
        if value is None:
            return None
        key = str(value).strip()
        if key.lower().startswith("bearer "):
            key = key[7:].strip()
        return key or None

    @field_validator("database_url", "cms_database_url", "crm_database_url", mode="before")
    @classmethod
    def normalize_database_url(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if value.startswith("postgres://"):
            value = value.replace("postgres://", "postgresql://", 1)
        if value.startswith("postgresql://") and "+psycopg2" not in value:
            value = value.replace("postgresql://", "postgresql+psycopg2://", 1)
        return value

    @property
    def resolved_cms_database_url(self) -> str:
        return self.cms_database_url or self.database_url

    @property
    def resolved_crm_database_url(self) -> str:
        return self.crm_database_url or self.database_url

    @property
    def is_split_database(self) -> bool:
        return self.resolved_cms_database_url != self.resolved_crm_database_url

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value


settings = Settings()
