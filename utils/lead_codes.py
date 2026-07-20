"""Lead & customer reference codes — Travel CRM Lead Flow Guide v4.2.

Before booking:  TEMP202607100001-FB
After booking:   TG2026070001 (customer permanent ID)
Legacy:          TRG001-WA (still recognized in UI)
"""

from __future__ import annotations

import re
from datetime import date

# Website form types (CMS intake) → suffix
_WEBSITE_FORM_ABBREVS: dict[str, str] = {
    "travel_planner": "TP",
    "itinerary_inquiry": "IT",
    "hotel_booking": "HB",
    "contact_consultation": "CC",
    "travel_expert_consultation": "TE",
    "plan_my_journey": "PJ",
}

# Channel sources → suffix (longer keys first)
_CHANNEL_SOURCE_ABBREVS: tuple[tuple[str, str], ...] = (
    ("facebook / instagram", "FB"),
    ("facebook", "FB"),
    ("instagram", "IG"),
    ("google ads", "GA"),
    ("google business", "GB"),
    ("landing page", "LP"),
    ("offline campaign", "OC"),
    ("phone call", "PC"),
    ("club member", "CM"),
    ("club members", "CM"),
    ("travel partner", "TW"),
    ("travel partners", "TW"),
    ("existing / repeat", "RP"),
    ("existing", "RP"),
    ("repeat", "RP"),
    ("walk-in", "WI"),
    ("walk in", "WI"),
    ("corporate", "CP"),
    ("influencer", "IN"),
    ("influencers", "IN"),
    ("referral", "REF"),
    ("client referral", "REF"),
    ("whatsapp", "WA"),
    ("direct whatsapp", "WA"),
    ("manual crm input", "MN"),
    ("manual input", "MN"),
    ("social ads", "IG"),
    ("travel expert", "TE"),
    ("contact consultation", "CC"),
    ("itinerary inquiry", "IT"),
    ("plan my journey", "PJ"),
    ("travel planner", "TP"),
    ("hotel booking", "HB"),
    ("website", "WEB"),
    ("email", "EM"),
    ("phone", "PC"),
    ("manual", "MN"),
    ("direct", "DR"),
)

LEAD_SOURCE_ABBREV_LEGEND: tuple[tuple[str, str], ...] = (
    ("WEB", "Website"),
    ("FB", "Facebook"),
    ("IG", "Instagram"),
    ("GA", "Google Ads"),
    ("GB", "Google Business"),
    ("WA", "WhatsApp"),
    ("REF", "Referral"),
    ("RP", "Existing / repeat"),
    ("WI", "Walk-in"),
    ("CP", "Corporate"),
    ("CM", "Club members"),
    ("TW", "Travel partners"),
    ("IN", "Influencers"),
    ("PC", "Phone call"),
    ("EM", "Email"),
    ("LP", "Landing page"),
    ("OC", "Offline campaign"),
    ("IT", "Itinerary inquiry"),
    ("TP", "Travel planner"),
    ("HB", "Hotel booking"),
    ("CC", "Contact form"),
    ("TE", "Expert consultation"),
    ("PJ", "Plan my journey"),
    ("MN", "Manual CRM entry"),
    ("DR", "Direct / other"),
    ("RF", "Referral (legacy)"),
    ("WB", "Website (legacy)"),
)

TEMP_CODE_RE = re.compile(r"^TEMP(\d{8})(\d{4})-([A-Z0-9]{2,3})$")
LEGACY_TRG_CODE_RE = re.compile(r"^TRG(\d+)-([A-Z0-9]{2,3})$")
CUSTOMER_CODE_RE = re.compile(r"^TG(\d{6})(\d{4})$")


def normalize_phone_digits(phone: str | None) -> str | None:
    digits = "".join(ch for ch in (phone or "") if ch.isdigit())
    if len(digits) >= 10:
        return digits[-10:]
    return digits or None


def _two_letter_fallback(raw: str) -> str:
    words = [w for w in raw.replace("·", " ").split() if any(ch.isalnum() for ch in w)]
    if len(words) >= 2:
        return (words[0][0] + words[1][0]).upper()
    token = "".join(ch for ch in raw if ch.isalnum()).upper()
    if len(token) >= 2:
        return token[:2]
    if len(token) == 1:
        return f"{token}X"
    return "DR"


def source_abbreviation(source: str | None) -> str:
    raw = (source or "").strip()
    if not raw:
        return "DR"

    lowered = raw.lower()

    if lowered.startswith("website"):
        form_type = raw.split("·", 1)[-1].strip().lower()
        if form_type in _WEBSITE_FORM_ABBREVS:
            return _WEBSITE_FORM_ABBREVS[form_type]
        if form_type == "website":
            return "WEB"
        return _two_letter_fallback(form_type)

    for needle, abbrev in _CHANNEL_SOURCE_ABBREVS:
        if lowered == needle or needle in lowered:
            return abbrev

    return _two_letter_fallback(raw)


def format_temp_lead_code(day: date, sequence: int, source: str | None) -> str:
    """TEMP + YYYYMMDD + 0001 + source suffix."""
    return f"TEMP{day.strftime('%Y%m%d')}{sequence:04d}-{source_abbreviation(source)}"


def format_customer_code(year_month: str, sequence: int) -> str:
    """TG + YYYYMM + 0001 permanent customer ID."""
    ym = year_month.strip()
    if len(ym) != 6 or not ym.isdigit():
        raise ValueError("year_month must be YYYYMM")
    return f"TG{ym}{sequence:04d}"


def format_lead_code(sequence: int, source: str | None) -> str:
    """Legacy TRG format — kept for backward-compatible backfill scripts."""
    return f"TRG{sequence:03d}-{source_abbreviation(source)}"


def abbrev_label(abbrev: str) -> str | None:
    key = (abbrev or "").strip().upper()
    for code, label in LEAD_SOURCE_ABBREV_LEGEND:
        if code == key:
            return label
    return None


def is_temp_lead_code(code: str | None) -> bool:
    return bool(code and TEMP_CODE_RE.match(code.strip()))


def is_legacy_trg_lead_code(code: str | None) -> bool:
    return bool(code and LEGACY_TRG_CODE_RE.match(code.strip()))


def is_customer_code(code: str | None) -> bool:
    return bool(code and CUSTOMER_CODE_RE.match(code.strip()))
