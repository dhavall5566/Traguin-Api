"""Human-readable lead reference codes: TRG001-WA (2-letter source suffix)."""

from __future__ import annotations

# Website form types (from cms intake) → 2-letter suffix
_WEBSITE_FORM_ABBREVS: dict[str, str] = {
    "travel_planner": "TP",
    "itinerary_inquiry": "IT",
    "hotel_booking": "HB",
    "contact_consultation": "CC",
    "travel_expert_consultation": "TE",
    "plan_my_journey": "PJ",
}

# CRM / channel sources → 2-letter suffix (order: longer keys first when matching)
_CHANNEL_SOURCE_ABBREVS: tuple[tuple[str, str], ...] = (
    ("manual crm input", "MN"),
    ("manual input", "MN"),
    ("direct whatsapp", "WA"),
    ("client referral", "RF"),
    ("social ads", "IG"),
    ("travel expert", "TE"),
    ("contact consultation", "CC"),
    ("itinerary inquiry", "IT"),
    ("plan my journey", "PJ"),
    ("travel planner", "TP"),
    ("hotel booking", "HB"),
    ("whatsapp", "WA"),
    ("instagram", "IG"),
    ("referral", "RF"),
    ("website", "WB"),
    ("manual", "MN"),
    ("direct", "DR"),
)

# Legend shown in CRM UI (code → label)
LEAD_SOURCE_ABBREV_LEGEND: tuple[tuple[str, str], ...] = (
    ("WB", "Website"),
    ("IT", "Itinerary inquiry"),
    ("TP", "Travel planner"),
    ("HB", "Hotel booking"),
    ("CC", "Contact form"),
    ("TE", "Expert consultation"),
    ("PJ", "Plan my journey"),
    ("WA", "WhatsApp"),
    ("IG", "Instagram / social ads"),
    ("RF", "Referral"),
    ("MN", "Manual CRM entry"),
    ("DR", "Direct / other"),
)


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
            return "WB"
        return _two_letter_fallback(form_type)

    for needle, abbrev in _CHANNEL_SOURCE_ABBREVS:
        if lowered == needle or needle in lowered:
            return abbrev

    return _two_letter_fallback(raw)


def format_lead_code(sequence: int, source: str | None) -> str:
    return f"TRG{sequence:03d}-{source_abbreviation(source)}"


def abbrev_label(abbrev: str) -> str | None:
    key = (abbrev or "").strip().upper()
    for code, label in LEAD_SOURCE_ABBREV_LEGEND:
        if code == key:
            return label
    return None
