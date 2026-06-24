from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


RAW_DIR = Path("data/raw")
REPORTS_DIR = Path("reports")
EXPECTED_DATASETS = 10


def find_csv_files(raw_dir: Path = RAW_DIR) -> list[Path]:
    return sorted(
        path
        for path in raw_dir.rglob("*.csv")
        if path.is_file() and not path.name.startswith(".")
    )


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin-1")


def print_dataset_profile(path: Path, df: pd.DataFrame) -> list[str]:
    anomalies: list[str] = []

    print(f"\n{'=' * 88}")
    print(f"Dataset: {path}")
    print(f"Shape: {df.shape}")
    print("\nDtypes:")
    print(df.dtypes)
    print("\nHead:")
    print(df.head())

    if df.empty:
        anomalies.append("dataset is empty")
    if df.columns.duplicated().any():
        duplicates = sorted(df.columns[df.columns.duplicated()].unique())
        anomalies.append(f"duplicate columns: {duplicates}")
    if df.duplicated().any():
        anomalies.append(f"{int(df.duplicated().sum())} duplicate rows")

    null_only_columns = sorted(df.columns[df.isna().all()].tolist())
    if null_only_columns:
        anomalies.append(f"all-null columns: {null_only_columns}")

    unnamed_columns = [col for col in df.columns if str(col).lower().startswith("unnamed")]
    if unnamed_columns:
        anomalies.append(f"unnamed index-like columns: {unnamed_columns}")

    null_pct = df.isna().mean().sort_values(ascending=False)
    high_null_columns = null_pct[null_pct >= 0.5]
    if not high_null_columns.empty:
        formatted = {col: round(float(pct), 3) for col, pct in high_null_columns.items()}
        anomalies.append(f"columns with >=50% nulls: {formatted}")

    if anomalies:
        print("\nAnomalies:")
        for anomaly in anomalies:
            print(f"- {anomaly}")
    else:
        print("\nAnomalies: none detected by automated checks")

    return anomalies


def normalize_columns(df: pd.DataFrame) -> dict[str, str]:
    return {col: str(col).strip().lower().replace(" ", "_") for col in df.columns}


def first_matching_column(df: pd.DataFrame, candidates: Iterable[str]) -> str | None:
    normalized = normalize_columns(df)
    candidate_set = {candidate.lower() for candidate in candidates}
    for original, normalized_name in normalized.items():
        if normalized_name in candidate_set:
            return original
    for original, normalized_name in normalized.items():
        if any(candidate in normalized_name for candidate in candidate_set):
            return original
    return None


def find_dataset(csv_files: list[Path], stem_keywords: Iterable[str]) -> Path | None:
    keywords = [keyword.lower() for keyword in stem_keywords]
    for path in csv_files:
        searchable = f"{path.stem} {path.parent}".lower()
        if all(keyword in searchable for keyword in keywords):
            return path
    return None


def print_unique_values(df: pd.DataFrame, label: str, candidates: list[str]) -> str:
    column = first_matching_column(df, candidates)
    if column is None:
        message = f"{label}: column not found using candidates {candidates}"
        print(message)
        return message

    values = sorted(df[column].dropna().astype(str).str.strip().unique())
    print(f"\nUnique {label} ({column}) [{len(values)}]:")
    print(values)
    return f"{label}: {len(values)} unique values from column '{column}'"


def explore_fund_master(csv_files: list[Path]) -> tuple[pd.DataFrame | None, Path | None, list[str]]:
    fund_master_path = find_dataset(csv_files, ["fund", "master"])
    notes: list[str] = []
    if fund_master_path is None:
        note = "fund_master CSV not found in data/raw"
        print(f"\n{note}")
        return None, None, [note]

    fund_master = read_csv(fund_master_path)
    print(f"\n{'=' * 88}")
    print(f"Fund master exploration: {fund_master_path}")
    notes.append(print_unique_values(fund_master, "fund houses", ["fund_house", "amc", "asset_management_company"]))
    notes.append(print_unique_values(fund_master, "categories", ["category", "scheme_category"]))
    notes.append(print_unique_values(fund_master, "sub-categories", ["sub_category", "subcategory", "scheme_sub_category"]))
    notes.append(print_unique_values(fund_master, "risk grades", ["risk_grade", "risk", "riskometer", "risk_level"]))
    notes.append(
        "AMFI scheme codes are numeric scheme identifiers. Treat them as stable IDs, "
        "not as a semantic hierarchy where digits encode fund house/category."
    )
    print(f"\nAMFI scheme code note: {notes[-1]}")
    return fund_master, fund_master_path, notes


def validate_amfi_codes(
    fund_master: pd.DataFrame | None,
    csv_files: list[Path],
) -> list[str]:
    notes: list[str] = []
    if fund_master is None:
        return ["AMFI code validation skipped because fund_master was not found."]

    nav_history_path = find_dataset(csv_files, ["nav", "history"])
    if nav_history_path is None:
        note = "AMFI code validation skipped because nav_history CSV was not found."
        print(f"\n{note}")
        return [note]

    nav_history = read_csv(nav_history_path)
    master_code_col = first_matching_column(
        fund_master,
        ["scheme_code", "amfi_code", "code", "scheme_id"],
    )
    nav_code_col = first_matching_column(
        nav_history,
        ["scheme_code", "amfi_code", "code", "scheme_id"],
    )

    if master_code_col is None or nav_code_col is None:
        note = (
            "AMFI code validation skipped because a code column was not found in "
            f"fund_master ({master_code_col}) or nav_history ({nav_code_col})."
        )
        print(f"\n{note}")
        return [note]

    master_codes = set(fund_master[master_code_col].dropna().astype(str).str.strip())
    nav_codes = set(nav_history[nav_code_col].dropna().astype(str).str.strip())
    missing_from_nav = sorted(master_codes - nav_codes)

    print(f"\n{'=' * 88}")
    print("AMFI code validation")
    print(f"fund_master code column: {master_code_col}")
    print(f"nav_history code column: {nav_code_col}")
    print(f"fund_master codes: {len(master_codes)}")
    print(f"nav_history codes: {len(nav_codes)}")
    print(f"missing fund_master codes from nav_history: {len(missing_from_nav)}")
    if missing_from_nav:
        print(missing_from_nav[:50])

    notes.append(f"fund_master unique AMFI codes: {len(master_codes)}")
    notes.append(f"nav_history unique AMFI codes: {len(nav_codes)}")
    notes.append(f"fund_master codes missing in nav_history: {len(missing_from_nav)}")
    if missing_from_nav:
        notes.append(f"first missing codes: {missing_from_nav[:50]}")
    else:
        notes.append("All fund_master AMFI codes exist in nav_history.")
    return notes


def write_quality_summary(
    csv_files: list[Path],
    dataset_anomalies: dict[Path, list[str]],
    fund_master_notes: list[str],
    validation_notes: list[str],
) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = REPORTS_DIR / "data_quality_summary.md"

    lines = [
        "# Day 1 Data Quality Summary",
        "",
        f"- CSV files discovered in `data/raw`: {len(csv_files)}",
        f"- Expected provided datasets: {EXPECTED_DATASETS}",
    ]
    if len(csv_files) != EXPECTED_DATASETS:
        lines.append(f"- Dataset count anomaly: expected {EXPECTED_DATASETS}, found {len(csv_files)}")

    lines.extend(["", "## Dataset Anomalies"])
    if dataset_anomalies:
        for path, anomalies in dataset_anomalies.items():
            lines.append(f"- `{path}`: {'; '.join(anomalies)}")
    else:
        lines.append("- None detected by automated checks.")

    lines.extend(["", "## Fund Master Exploration"])
    lines.extend(f"- {note}" for note in fund_master_notes)

    lines.extend(["", "## AMFI Code Validation"])
    lines.extend(f"- {note}" for note in validation_notes)

    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return summary_path


def main() -> None:
    csv_files = find_csv_files()
    print(f"Discovered {len(csv_files)} CSV file(s) under {RAW_DIR}.")
    if len(csv_files) != EXPECTED_DATASETS:
        print(f"Dataset count anomaly: expected {EXPECTED_DATASETS}, found {len(csv_files)}.")

    dataset_anomalies: dict[Path, list[str]] = {}
    for path in csv_files:
        df = read_csv(path)
        anomalies = print_dataset_profile(path, df)
        if anomalies:
            dataset_anomalies[path] = anomalies

    fund_master, _fund_master_path, fund_master_notes = explore_fund_master(csv_files)
    validation_notes = validate_amfi_codes(fund_master, csv_files)
    summary_path = write_quality_summary(
        csv_files,
        dataset_anomalies,
        fund_master_notes,
        validation_notes,
    )
    print(f"\nWrote data quality summary to {summary_path}")


if __name__ == "__main__":
    main()
