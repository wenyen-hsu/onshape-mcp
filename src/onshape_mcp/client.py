"""Minimal httpx-based Onshape REST client with request signing."""

from __future__ import annotations

from typing import Any

import httpx

from .auth import build_headers


class OnshapeError(Exception):
    def __init__(self, status: int, message: str, body: Any = None):
        super().__init__(f"[{status}] {message}")
        self.status = status
        self.body = body


class OnshapeClient:
    def __init__(
        self,
        access_key: str,
        secret_key: str,
        base_url: str = "https://cad.onshape.com",
        timeout: float = 60.0,
    ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.base_url = base_url.rstrip("/")
        self._client = httpx.Client(timeout=timeout, follow_redirects=False)

    def close(self) -> None:
        self._client.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict | None = None,
        json: Any = None,
        accept: str = "application/json",
        content_type: str = "application/json",
    ) -> httpx.Response:
        url = httpx.URL(f"{self.base_url}{path}")
        if params:
            url = url.copy_merge_params(params)

        headers = build_headers(
            method,
            str(url),
            self.access_key,
            self.secret_key,
            content_type=content_type,
            accept=accept,
        )
        response = self._client.request(method, url, headers=headers, json=json)

        # Onshape often 307s to a signed CDN host; must re-sign with new URL.
        if response.status_code == 307:
            new_url = response.headers.get("Location")
            if not new_url:
                raise OnshapeError(307, "redirect missing Location header")
            headers = build_headers(
                method,
                new_url,
                self.access_key,
                self.secret_key,
                content_type=content_type,
                accept=accept,
            )
            response = self._client.request(method, new_url, headers=headers, json=json)

        if response.status_code >= 400:
            try:
                body = response.json()
                msg = body.get("message") or body.get("moreInfoUrl") or response.text
            except Exception:
                body = response.text
                msg = response.text[:500]
            raise OnshapeError(response.status_code, msg, body)

        return response

    def get(self, path: str, params: dict | None = None) -> Any:
        r = self.request("GET", path, params=params)
        if r.headers.get("content-type", "").startswith("application/json"):
            return r.json()
        return r.content

    def post(self, path: str, json: Any = None, params: dict | None = None) -> Any:
        r = self.request("POST", path, params=params, json=json)
        if r.headers.get("content-type", "").startswith("application/json"):
            return r.json()
        return r.content

    def delete(self, path: str, params: dict | None = None) -> Any:
        r = self.request("DELETE", path, params=params)
        if r.status_code == 204 or not r.content:
            return {"ok": True}
        return r.json()
