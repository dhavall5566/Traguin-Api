from __future__ import annotations

import ipaddress

from fastapi import Request


def client_ip_or_none(request: Request) -> str | None:
    if request.client is None or not request.client.host:
        return None
    host = request.client.host.strip()
    if not host:
        return None
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return None
    return host
