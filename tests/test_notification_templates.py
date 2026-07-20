"""Tests for Traguin notification templates."""

from __future__ import annotations

from services.notification_templates.catalog import TEMPLATE_IDS, get_template
from services.notification_templates.renderer import render_email, render_plain, render_whatsapp


def test_all_templates_registered():
    assert len(TEMPLATE_IDS) == 19
    for template_id in TEMPLATE_IDS:
        spec = get_template(template_id)
        assert spec.id == template_id
        assert spec.subject
        assert spec.email_body_html


def test_render_customer_inquiry_received():
    variables = {
        "Customer_Name": "Priya Sharma",
        "Support_Phone": "+91 98765 43210",
    }
    subject, html = render_email("customer_inquiry_received", variables)
    assert "Priya Sharma" in subject or "Priya Sharma" in html
    assert "received your enquiry" in html.lower()

    wa = render_whatsapp("customer_inquiry_received", variables)
    assert "Hello Priya Sharma" in wa
    assert "successfully received your enquiry" in wa
    assert "Thank you for choosing Traguin" in wa


def test_render_customer_welcome():
    variables = {
        "Customer_Name": "Priya Sharma",
        "Temp_ID": "TEMP202607080001-WEB",
        "Destination": "Bali",
        "Travel_Dates": "15 Aug 2026",
        "Guests": "2",
        "RM_Name": "Rahul Mehta",
        "Support_Phone": "+91 98765 43210",
    }
    subject, html = render_email("customer_enquiry_welcome", variables)
    assert "TEMP202607080001-WEB" in subject
    assert "Priya Sharma" in html
    assert "Bali" in html
    assert "Rahul Mehta" in html

    wa = render_whatsapp("customer_enquiry_welcome", variables)
    assert "Welcome to Traguin" in wa
    assert "TEMP202607080001-WEB" in wa

    plain = render_plain("customer_enquiry_welcome", variables)
    assert "Priya Sharma" in plain


def test_render_rm_assignment():
    variables = {
        "RM_Name": "Rahul",
        "Temp_ID": "TEMP202607080001-WEB",
        "Customer_Name": "Priya",
        "Phone": "+91 99999 88888",
        "Destination": "Bali",
        "Travel_Dates": "15 Aug 2026",
        "Priority": "High",
        "Inquiry_Count": "2",
        "Active_Enquiry_1": "—",
        "Active_Enquiry_2": "—",
        "Customer_Flags": "None",
        "Accept_Link": "https://crm.example/accept",
        "Reject_Link": "https://crm.example/reject",
        "CRM_Link": "https://crm.example/lead",
    }
    subject, html = render_email("team_lead_assigned", variables)
    assert "Action Required" in subject
    assert "Accept Lead" in html
    assert "https://crm.example/accept" in html


if __name__ == "__main__":
    test_all_templates_registered()
    test_render_customer_inquiry_received()
    test_render_customer_welcome()
    test_render_rm_assignment()
    print("notification_templates tests passed")
