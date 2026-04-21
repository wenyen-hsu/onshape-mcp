"""Onshape API request signing (HMAC-SHA256)."""

from __future__ import annotations

import base64
import hashlib
import hmac
import secrets
from datetime import datetime, timezone
from urllib.parse import urlparse


def generate_nonce() -> str:
    """Random 32-char hex string (>= 16 chars required)."""
    return secrets.token_hex(16)


def http_date() -> str:
    """RFC 1123 date string in GMT."""
    return datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")


def sign_request(
    method: str,
    url: str,
    nonce: str,
    date: str,
    content_type: str,
    access_key: str,
    secret_key: str,
) -> str:
    """Build the Authorization header value for an Onshape API request.

    The string-to-sign is: method + nonce + date + content-type + pathname + query,
    each followed by '\\n', all lowercased. HMAC-SHA256 with the secret key,
    base64-encoded.
    """
    parsed = urlparse(url)
    path = parsed.path
    query = parsed.query or ""

    string_to_sign = (
        f"{method}\n{nonce}\n{date}\n{content_type}\n{path}\n{query}\n"
    ).lower()

    digest = hmac.new(
        secret_key.encode("utf-8"),
        string_to_sign.encode("utf-8"),
        hashlib.sha256,
    ).digest()
    signature = base64.b64encode(digest).decode("ascii")
    return f"On {access_key}:HmacSHA256:{signature}"


def build_headers(
    method: str,
    url: str,
    access_key: str,
    secret_key: str,
    content_type: str = "application/json",
    accept: str = "application/json",
) -> dict[str, str]:
    nonce = generate_nonce()
    date = http_date()
    auth = sign_request(
        method.upper(), url, nonce, date, content_type, access_key, secret_key
    )
    return {
        "Date": date,
        "On-Nonce": nonce,
        "Content-Type": content_type,
        "Accept": accept,
        "Authorization": auth,
    }
