"""Lead & customer reference code formatting."""

from __future__ import annotations

from datetime import date

import pytest

from utils.lead_codes import (
    format_customer_code,
    format_temp_lead_code,
    is_customer_code,
    is_legacy_trg_lead_code,
    is_temp_lead_code,
    source_abbreviation,
)


def test_format_temp_lead_code() -> None:
    code = format_temp_lead_code(date(2026, 7, 10), 1, "Facebook / Instagram")
    assert code == "TEMP202607100001-FB"
    assert is_temp_lead_code(code)


def test_format_customer_code() -> None:
    code = format_customer_code("202607", 1)
    assert code == "TG2026070001"
    assert is_customer_code(code)


def test_source_abbreviation_spec_channels() -> None:
    assert source_abbreviation("Website") == "WEB"
    assert source_abbreviation("WhatsApp") == "WA"
    assert source_abbreviation("Referral") == "REF"
    assert source_abbreviation("Google Ads") == "GA"
    assert source_abbreviation("Walk-in") == "WI"


def test_legacy_trg_still_recognized() -> None:
    assert is_legacy_trg_lead_code("TRG001-WA")
    assert not is_legacy_trg_lead_code("TEMP202607100001-WA")
