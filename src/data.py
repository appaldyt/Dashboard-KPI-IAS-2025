"""Data access and lightweight analysis utilities."""

from __future__ import annotations

import pandas as pd

SHEET_ID = "1hBAwASHH0mdtv798lSPoZGDq5xZmdyobmJRsWzgIxzk"
GID = "0"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}"


def load_data(csv_url: str | None = None) -> pd.DataFrame:
    """Load data from a Google Sheets CSV export URL."""
    url = csv_url or CSV_URL
    return pd.read_csv(url)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    """Return basic numeric summary for quick inspection."""
    return df.describe(include="number").T
