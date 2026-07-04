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
            "eyebrow": "Luxury · Corporate · Experiential",
            "title": "India-rooted. Globally trusted.",
            "description": "TRAGUIN is a full-spectrum travel and destination management company delivering domestic and international travel solutions with global service standards and deep regional expertise. From leadership offsites and incentive programs to luxury leisure and immersive cultural journeys, we design experiences that are seamless, meaningful, and impeccably managed.",
        },
    )
    steps.append(f"about-page-header: {code}")

    sections = [
        (
            "Brand Story",
            "TRAGUIN is a modern, premium, trust-driven travel brand headquartered in India, with an expanding international presence.",
            0,
        ),
        (
            "Who We Are",
            "India remains our foundation and strongest capability, while our international portfolio is selective, curated, and premium by design.",
            1,
        ),
        (
            "Founder's Message",
            "TRAGUIN was created with a simple but uncompromising belief—travel must be built on trust, intention, and excellence.",
            2,
        ),
        (
            "Philosophy & Pillars",
            "Our philosophy rests on three pillars: craftsmanship, experience first, and responsible growth.",
            3,
        ),
        (
            "Core Services",
            "TRAGUIN delivers end-to-end premium travel solutions across domestic and international destinations.",
            4,
        ),
        (
            "India — Destination Expertise",
            "Deep regional mastery across West, North, East, North-East, and South India.",
            5,
        ),
        (
            "Corporate & MICE Excellence",
            "Strategic corporate travel, MICE, leadership offsites, and end-to-end on-ground execution.",
            6,
        ),
        (
            "International Portfolio",
            "Select international destinations curated with the same luxury standards as our domestic expertise.",
            7,
        ),
        (
            "TRAGUIN Villas",
            "Ultra-luxury private villa stays for discerning guests, families, and corporate leaders.",
            8,
        ),
        (
            "Inbound — India for the World",
            "Trusted India specialist for global partners—reliability, transparency, and destination authority.",
            9,
        ),
        (
            "Leadership",
            "Abhilash Pillai, Founder—visionary thinking and execution discipline behind TRAGUIN.",
            10,
        ),
        (
            "Our Promise",
            "We do not sell trips. We design experiences, manage responsibility, and deliver trust.",
            11,
        ),
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
