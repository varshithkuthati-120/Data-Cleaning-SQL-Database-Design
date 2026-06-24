from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import requests


API_URL = "https://api.mfapi.in/mf/{scheme_code}"
RAW_NAV_DIR = Path("data/raw/live_nav")

SCHEMES = {
    "HDFC Top 100 Direct": "125497",
    "SBI Bluechip": "119551",
    "ICICI Bluechip": "120503",
    "Nippon Large Cap": "118632",
    "Axis Bluechip": "119092",
    "Kotak Bluechip": "120841",
}


def fetch_scheme_nav(scheme_name: str, scheme_code: str) -> pd.DataFrame:
    response = requests.get(API_URL.format(scheme_code=scheme_code), timeout=30)
    response.raise_for_status()
    payload: dict[str, Any] = response.json()

    records = payload.get("data", [])
    if not isinstance(records, list):
        raise ValueError(f"Unexpected data format for {scheme_code}: expected list.")

    df = pd.DataFrame(records)
    if df.empty:
        df = pd.DataFrame(columns=["date", "nav"])

    meta = payload.get("meta", {}) or {}
    if not isinstance(meta, dict):
        meta = {}

    df.insert(0, "scheme_code", scheme_code)
    df.insert(1, "scheme_name_requested", scheme_name)
    df.insert(2, "scheme_name_api", meta.get("scheme_name"))
    df.insert(3, "fund_house", meta.get("fund_house"))
    df.insert(4, "scheme_type", meta.get("scheme_type"))
    df.insert(5, "scheme_category", meta.get("scheme_category"))
    df["fetched_at_utc"] = datetime.now(timezone.utc).isoformat()

    if "nav" in df.columns:
        df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

    return df


def safe_name(name: str) -> str:
    return (
        name.lower()
        .replace("&", "and")
        .replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
    )


def main() -> None:
    RAW_NAV_DIR.mkdir(parents=True, exist_ok=True)

    frames: list[pd.DataFrame] = []
    for scheme_name, scheme_code in SCHEMES.items():
        print(f"Fetching {scheme_name} ({scheme_code})...")
        df = fetch_scheme_nav(scheme_name, scheme_code)
        frames.append(df)

        output_path = RAW_NAV_DIR / f"{scheme_code}_{safe_name(scheme_name)}.csv"
        df.to_csv(output_path, index=False)
        print(f"Saved {len(df)} NAV row(s) to {output_path}")

    combined = pd.concat(frames, ignore_index=True)
    combined_path = RAW_NAV_DIR / "key_schemes_nav_history.csv"
    combined.to_csv(combined_path, index=False)
    print(f"Saved combined NAV history to {combined_path}")


if __name__ == "__main__":
    main()
