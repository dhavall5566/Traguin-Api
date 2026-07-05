"""Tests for lead source merging and phone deduplication helpers."""

from services.lead_phone_dedup import merge_lead_sources


def test_merge_lead_sources_appends_unique():
    assert merge_lead_sources("Website · contact_consultation", "WhatsApp") == (
        "Website · contact_consultation, WhatsApp"
    )


def test_merge_lead_sources_skips_duplicate():
    existing = "Website · contact_consultation, WhatsApp"
    assert merge_lead_sources(existing, "WhatsApp") == existing


def test_merge_lead_sources_empty_existing():
    assert merge_lead_sources(None, "Instagram") == "Instagram"


def test_merge_lead_sources_splits_existing_commas():
    assert merge_lead_sources("WhatsApp, Instagram", "Manual CRM input") == (
        "WhatsApp, Instagram, Manual CRM input"
    )
