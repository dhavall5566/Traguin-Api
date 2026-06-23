#!/usr/bin/env python3
"""Seed about/careers/legal CMS content for frontend verification."""
import json
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:8001/api/cms/admin"


def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(
        f"{BASE}{path}",
        data=data,
        method=method,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as resp:
            raw = resp.read().decode()
            return resp.status, json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read().decode())


def main():
    steps = []

    code, _ = req(
        "PATCH",
        "/about-page-header",
        {
            "eyebrow": "Who We Are",
            "title": "Crafted for discerning travelers",
            "description": "Like the world's finest travel houses, we combine deep destination knowledge with white-glove service, so every journey feels effortless and entirely yours.",
        },
    )
    steps.append(f"about-page-header: {code}")

    sections = [
        ("Our Story", "Founded in Ahmedabad, TRAGUIN began with a simple belief: luxury travel should feel personal, not transactional.", 0),
        ("Since 2024", "We refined our craft from day one, pairing discerning travelers with properties, experiences, and specialists that reflect their standards.", 1),
        ("Philosophy", "We design around how you wish to feel. Every itinerary balances beauty, comfort, and authenticity.", 2),
    ]
    for title, body, sort_order in sections:
        code, _ = req("POST", "/about-story-sections", {"title": title, "body": body, "sort_order": sort_order})
        steps.append(f"about-story-section '{title}': {code}")

    code, _ = req(
        "PATCH",
        "/careers-page-extras",
        {
            "culture_chips": ["Bespoke travel studio", "Collaborative expert team", "Ahmedabad headquarters"],
            "fallback_title": "Don't see your role?",
            "fallback_description": "Send your résumé and a short note on what you would bring to TRAGUIN. We review every application personally.",
        },
    )
    steps.append(f"careers-page-extras: {code}")

    code, _ = req(
        "POST",
        "/job-openings",
        {
            "slug": "luxury-travel-designer",
            "title": "Luxury Travel Designer",
            "location": "Ahmedabad · Hybrid",
            "employment_type": "Full-time",
            "description": "Craft bespoke itineraries for discerning travelers, from Himalayan retreats to global luxury escapes.",
            "sort_order": 0,
            "is_published": True,
        },
    )
    steps.append(f"job-opening luxury-travel-designer: {code}")

    privacy_sections = [
        {
            "title": "Introduction",
            "paragraphs": [
                "TRAGUIN Luxury Travel respects your privacy and is committed to protecting the personal information you share when using our website and services.",
                "This Privacy Policy explains what data we collect, why we collect it, and the choices available to you.",
            ],
        },
        {
            "title": "Information We Collect",
            "paragraphs": ["We may collect the following categories of information:"],
            "list": [
                "Contact details such as name, email address, and phone number",
                "Travel preferences including destinations, dates, budget, and special requests",
                "Communications you send us via forms, email, phone, or messaging platforms",
            ],
        },
    ]

    code, _ = req(
        "POST",
        "/legal-pages",
        {
            "slug": "privacy-policy",
            "eyebrow": "Legal",
            "title": "Privacy Policy",
            "description": "How TRAGUIN collects, uses, and protects your personal information when you plan and book luxury travel with us.",
            "effective_date": "June 2026",
            "hero_media_id": None,
            "hero_image_alt": "Luxury travel landscape",
            "sections": privacy_sections,
        },
    )
    steps.append(f"legal privacy-policy: {code}")

    terms_sections = [
        {
            "title": "Agreement",
            "paragraphs": [
                "By accessing our website or engaging TRAGUIN Luxury Travel for travel planning services, you agree to these Terms of Service.",
            ],
        },
        {
            "title": "Website Use",
            "paragraphs": ["When using our website, you agree not to:"],
            "list": [
                "Misuse the site or attempt unauthorized access",
                "Copy or reproduce content without permission",
                "Submit false or misleading information",
            ],
        },
    ]

    code, _ = req(
        "POST",
        "/legal-pages",
        {
            "slug": "terms-of-service",
            "eyebrow": "Legal",
            "title": "Terms of Service",
            "description": "The terms governing your use of TRAGUIN's website and luxury travel planning services.",
            "effective_date": "June 2026",
            "hero_media_id": None,
            "hero_image_alt": "Travel expert at work",
            "sections": terms_sections,
        },
    )
    steps.append(f"legal terms-of-service: {code}")

    print("\n".join(steps))


if __name__ == "__main__":
    main()
