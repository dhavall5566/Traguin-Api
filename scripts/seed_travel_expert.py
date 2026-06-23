#!/usr/bin/env python3
"""Seed travel-expert page CMS content."""
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
        "/travel-expert-settings",
        {
            "desk_headline": "Always here for you",
            "hours_label": "Working hours",
            "hours_value": "2",
            "live_desk_label": "Live desk",
            "live_desk_value": "24·7·365",
        },
    )
    steps.append(f"travel-expert-settings: {code}")

    services = [
        {
            "slug": "bespoke-journeys",
            "number_label": "01",
            "title": "Bespoke Journeys",
            "description": "Routes shaped around your rhythm, stays, pacing, and moments no brochure can offer.",
            "icon_key": "sparkles",
            "is_featured": True,
            "is_wide": False,
            "sort_order": 0,
        },
        {
            "slug": "visa-documentation",
            "number_label": "02",
            "title": "Visa & Documentation",
            "description": "Paperwork, appointments, and approvals cleared before you ever pack a bag.",
            "icon_key": "file-check",
            "is_featured": False,
            "is_wide": False,
            "sort_order": 1,
        },
        {
            "slug": "corporate-mice",
            "number_label": "07",
            "title": "Corporate & MICE",
            "description": "Leadership retreats, incentive travel, and board-level programs without a single loose end.",
            "icon_key": "briefcase",
            "is_featured": False,
            "is_wide": True,
            "sort_order": 6,
        },
    ]

    for service in services:
        code, _ = req("POST", "/concierge-services", service)
        steps.append(f"concierge-service {service['slug']}: {code}")

    print("\n".join(steps))


if __name__ == "__main__":
    main()
