import os
import sqlite3
from pathlib import Path
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text

# Paths
WORKSPACE_DIR = Path(__file__).resolve().parent
RAW_DIR = WORKSPACE_DIR / "data" / "raw"
PROCESSED_DIR = WORKSPACE_DIR / "data" / "processed"
DB_PATH = WORKSPACE_DIR / "data" / "mutual_fund.db"
SCHEMA_SQL_PATH = WORKSPACE_DIR / "sql" / "schema.sql"

# Make sure directories exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_nav_history() -> pd.DataFrame:
    print("--- Cleaning nav_history.csv ---")
    raw_path = RAW_DIR / "02_nav_history.csv"
    df = pd.read_csv(raw_path)

    # 1. Parse dates to datetime
    df["date"] = pd.to_datetime(df["date"])

    # 2. Remove duplicates
    initial_len = len(df)
    df = df.drop_duplicates(subset=["amfi_code", "date"])
    print(f"Removed {initial_len - len(df)} duplicate rows.")

    # 3. Validate NAV > 0
    invalid_nav = df[df["nav"] <= 0]
    if not invalid_nav.empty:
        print(f"Warning: Found {len(invalid_nav)} rows with NAV <= 0. Removing them.")
        df = df[df["nav"] > 0]

    # 4. Forward-fill missing NAV for holidays/weekends
    # Generate daily calendar from 2022-01-03 to 2026-05-29 for each fund
    min_date = df["date"].min()
    max_date = df["date"].max()
    print(f"NAV history date range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")

    # Pivot to fill missing dates
    pivot_df = df.pivot(index="date", columns="amfi_code", values="nav")
    full_date_range = pd.date_range(start=min_date, end=max_date, freq="D")
    pivot_df = pivot_df.reindex(full_date_range)

    # Forward-fill
    pivot_df = pivot_df.ffill()

    # Melt back to long format
    df_cleaned = pivot_df.unstack().reset_index()
    df_cleaned.columns = ["amfi_code", "date", "nav"]

    # Format date as YYYY-MM-DD string
    df_cleaned["date"] = df_cleaned["date"].dt.strftime("%Y-%m-%d")

    # 5. Sort by amfi_code + date
    df_cleaned = df_cleaned.sort_values(by=["amfi_code", "date"]).reset_index(drop=True)
    print(f"Resampled and forward-filled NAV history from {initial_len} to {len(df_cleaned)} rows.")

    # Save to processed
    df_cleaned.to_csv(PROCESSED_DIR / "fact_nav.csv", index=False)
    return df_cleaned


def clean_investor_transactions() -> pd.DataFrame:
    print("--- Cleaning investor_transactions.csv ---")
    raw_path = RAW_DIR / "08_investor_transactions.csv"
    df = pd.read_csv(raw_path)

    # 1. Standardise transaction_type values (SIP/Lumpsum/Redemption)
    df["transaction_type"] = df["transaction_type"].str.strip().str.title().replace({
        "Sip": "SIP",
        "Lumpsum": "Lumpsum",
        "Redemption": "Redemption"
    })

    # 2. Validate amount > 0
    invalid_amount = df[df["amount_inr"] <= 0]
    if not invalid_amount.empty:
        print(f"Warning: Found {len(invalid_amount)} transactions with amount <= 0. Removing them.")
        df = df[df["amount_inr"] > 0]

    # 3. Fix date formats
    df["transaction_date"] = pd.to_datetime(df["transaction_date"]).dt.strftime("%Y-%m-%d")

    # 4. Check KYC status enum values
    df["kyc_status"] = df["kyc_status"].str.strip().str.title()
    allowed_kyc = {"Verified", "Pending"}
    invalid_kyc = df[~df["kyc_status"].isin(allowed_kyc)]
    if not invalid_kyc.empty:
        print(f"Warning: Found invalid KYC status values: {invalid_kyc['kyc_status'].unique()}. Standardising to Pending.")
        df.loc[~df["kyc_status"].isin(allowed_kyc), "kyc_status"] = "Pending"

    print(f"Cleaned transactions shape: {df.shape}")

    # Save to processed
    df.to_csv(PROCESSED_DIR / "fact_transactions.csv", index=False)
    return df


def clean_scheme_performance() -> pd.DataFrame:
    print("--- Cleaning scheme_performance.csv ---")
    raw_path = RAW_DIR / "07_scheme_performance.csv"
    df = pd.read_csv(raw_path)

    # 1. Validate all return values are numeric
    return_cols = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct", "benchmark_3yr_pct"]
    for col in return_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 2. Check expense_ratio range (0.1% - 2.5%)
    # Let's check both in performance and fund master if needed, here we check in performance.
    df["expense_ratio_pct"] = pd.to_numeric(df["expense_ratio_pct"], errors="coerce")
    out_of_range = df[(df["expense_ratio_pct"] < 0.1) | (df["expense_ratio_pct"] > 2.5)]
    if not out_of_range.empty:
        print(f"Warning: Expense ratios outside 0.1% - 2.5% range found:")
        print(out_of_range[["amfi_code", "scheme_name", "expense_ratio_pct"]])

    # 3. Flag anomalies
    # Anomaly criteria: Sharpe ratio > 3.0 (liquid fund outliers), return_3yr_pct > 30% or < -10%, beta > 1.5 or < 0.2
    anomalies = []
    for idx, row in df.iterrows():
        if row["sharpe_ratio"] > 3.0:
            anomalies.append(f"High Sharpe Ratio Anomaly: {row['scheme_name']} (AMFI: {row['amfi_code']}) has Sharpe Ratio of {row['sharpe_ratio']}.")
        if row["sortino_ratio"] > 5.0:
            anomalies.append(f"High Sortino Ratio Anomaly: {row['scheme_name']} (AMFI: {row['amfi_code']}) has Sortino Ratio of {row['sortino_ratio']}.")
        if row["return_3yr_pct"] > 30.0:
            anomalies.append(f"High Return Anomaly: {row['scheme_name']} (AMFI: {row['amfi_code']}) has 3Yr Return of {row['return_3yr_pct']}%.")
        if row["beta"] > 1.5 or row["beta"] < 0.1:
            anomalies.append(f"Beta Outlier Anomaly: {row['scheme_name']} (AMFI: {row['amfi_code']}) has Beta of {row['beta']}.")

    print(f"Flagged {len(anomalies)} performance anomalies:")
    for anomaly in anomalies:
        print(f"  - {anomaly}")

    # Write anomalies report
    anomalies_report_path = WORKSPACE_DIR / "reports" / "performance_anomalies.txt"
    with open(anomalies_report_path, "w", encoding="utf-8") as f:
        f.write("Mutual Fund Scheme Performance Anomalies Report\n")
        f.write("===============================================\n\n")
        for anomaly in anomalies:
            f.write(f"- {anomaly}\n")
    print(f"Wrote anomalies report to {anomalies_report_path}")

    # Save to processed
    df.to_csv(PROCESSED_DIR / "fact_performance.csv", index=False)
    return df


def clean_fund_master() -> pd.DataFrame:
    print("--- Cleaning fund_master.csv ---")
    raw_path = RAW_DIR / "01_fund_master.csv"
    df = pd.read_csv(raw_path)
    df.to_csv(PROCESSED_DIR / "dim_fund.csv", index=False)
    return df


def clean_aum() -> pd.DataFrame:
    print("--- Cleaning aum_by_fund_house.csv ---")
    raw_path = RAW_DIR / "03_aum_by_fund_house.csv"
    df = pd.read_csv(raw_path)
    # Parse date to YYYY-MM-DD
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df.to_csv(PROCESSED_DIR / "fact_aum.csv", index=False)
    return df


def clean_benchmark_indices() -> pd.DataFrame:
    print("--- Cleaning benchmark_indices.csv ---")
    raw_path = RAW_DIR / "10_benchmark_indices.csv"
    df = pd.read_csv(raw_path)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df.to_csv(PROCESSED_DIR / "fact_benchmark_indices.csv", index=False)
    return df


def clean_portfolio_holdings() -> pd.DataFrame:
    print("--- Cleaning portfolio_holdings.csv ---")
    raw_path = RAW_DIR / "09_portfolio_holdings.csv"
    df = pd.read_csv(raw_path)
    df["portfolio_date"] = pd.to_datetime(df["portfolio_date"]).dt.strftime("%Y-%m-%d")
    df.to_csv(PROCESSED_DIR / "fact_portfolio_holdings.csv", index=False)
    return df


def clean_monthly_table(filename: str, processed_name: str) -> pd.DataFrame:
    print(f"--- Cleaning {filename} (monthly) ---")
    raw_path = RAW_DIR / filename
    df = pd.read_csv(raw_path)
    # Convert 'month' column YYYY-MM to YYYY-MM-01 format to link with dim_date
    df["month"] = pd.to_datetime(df["month"]).dt.strftime("%Y-%m-01")
    df.to_csv(PROCESSED_DIR / processed_name, index=False)
    return df


def generate_dim_date() -> pd.DataFrame:
    print("--- Generating dim_date ---")
    # Date range from 2022-01-01 to 2026-12-31 to cover all files
    dates = pd.date_range(start="2022-01-01", end="2026-12-31", freq="D")
    df = pd.DataFrame({"date": dates})
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["quarter"] = df["date"].dt.quarter
    df["month_name"] = df["date"].dt.strftime("%B")
    df["day_name"] = df["date"].dt.strftime("%A")
    df["is_weekend"] = df["date"].dt.dayofweek.isin([5, 6]).astype(int)
    df["day_of_week"] = df["date"].dt.dayofweek # 0 is Monday, 6 is Sunday

    # Convert date column to YYYY-MM-DD string
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    df.to_csv(PROCESSED_DIR / "dim_date.csv", index=False)
    return df


def setup_database_and_load():
    print("--- Setting up database schema and loading data ---")
    # 1. Clean and process dataframes
    df_date = generate_dim_date()
    df_fund = clean_fund_master()
    df_nav = clean_nav_history()
    df_transactions = clean_investor_transactions()
    df_performance = clean_scheme_performance()
    df_aum = clean_aum()
    df_holdings = clean_portfolio_holdings()
    df_benchmarks = clean_benchmark_indices()
    df_sip = clean_monthly_table("04_monthly_sip_inflows.csv", "fact_monthly_sip_inflows.csv")
    df_cat_inflows = clean_monthly_table("05_category_inflows.csv", "fact_category_inflows.csv")
    df_folios = clean_monthly_table("06_industry_folio_count.csv", "fact_folio_count.csv")

    # 2. Execute schema DDL
    print(f"Reading DDL schema from {SCHEMA_SQL_PATH}")
    with open(SCHEMA_SQL_PATH, "r", encoding="utf-8") as f:
        ddl_sql = f.read()

    # Remove existing DB file if it exists to start fresh
    if DB_PATH.exists():
        print(f"Removing existing database at {DB_PATH}")
        DB_PATH.unlink()

    # Connect using sqlite3 directly first to enable foreign keys and execute DDL
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.executescript(ddl_sql)
    conn.commit()
    conn.close()
    print("Database schema initialized successfully.")

    # 3. Load tables using SQLAlchemy engine
    engine = create_engine(f"sqlite:///{DB_PATH}")

    # To enforce foreign keys in SQLAlchemy connections, we add an event listener
    from sqlalchemy.engine import Engine
    from sqlalchemy import event

    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    # Load in dependency order:
    # 1. Dimensions
    print("Loading dim_date...")
    df_date.to_sql("dim_date", engine, if_exists="append", index=False)
    print("Loading dim_fund...")
    df_fund.to_sql("dim_fund", engine, if_exists="append", index=False)

    # 2. Facts and other tables
    print("Loading fact_nav...")
    df_nav.to_sql("fact_nav", engine, if_exists="append", index=False)
    print("Loading fact_transactions...")
    # Map column names if they match
    df_transactions.to_sql("fact_transactions", engine, if_exists="append", index=False)
    print("Loading fact_performance...")
    df_performance.to_sql("fact_performance", engine, if_exists="append", index=False)
    print("Loading fact_aum...")
    df_aum.to_sql("fact_aum", engine, if_exists="append", index=False)
    print("Loading fact_portfolio_holdings...")
    df_holdings.to_sql("fact_portfolio_holdings", engine, if_exists="append", index=False)
    print("Loading fact_benchmark_indices...")
    df_benchmarks.to_sql("fact_benchmark_indices", engine, if_exists="append", index=False)
    print("Loading fact_monthly_sip_inflows...")
    df_sip.to_sql("fact_monthly_sip_inflows", engine, if_exists="append", index=False)
    print("Loading fact_category_inflows...")
    df_cat_inflows.to_sql("fact_category_inflows", engine, if_exists="append", index=False)
    print("Loading fact_folio_count...")
    df_folios.to_sql("fact_folio_count", engine, if_exists="append", index=False)

    print("Data loaded successfully.")

    # 4. Verification Check
    print("--- Row Count Verification ---")
    verification_results = []
    
    tables_to_verify = [
        ("dim_date", len(df_date), "Generated calendar"),
        ("dim_fund", len(df_fund), "01_fund_master.csv"),
        ("fact_nav", len(df_nav), "02_nav_history.csv (processed)"),
        ("fact_transactions", len(df_transactions), "08_investor_transactions.csv"),
        ("fact_performance", len(df_performance), "07_scheme_performance.csv"),
        ("fact_aum", len(df_aum), "03_aum_by_fund_house.csv"),
        ("fact_portfolio_holdings", len(df_holdings), "09_portfolio_holdings.csv"),
        ("fact_benchmark_indices", len(df_benchmarks), "10_benchmark_indices.csv"),
        ("fact_monthly_sip_inflows", len(df_sip), "04_monthly_sip_inflows.csv"),
        ("fact_category_inflows", len(df_cat_inflows), "05_category_inflows.csv"),
        ("fact_folio_count", len(df_folios), "06_industry_folio_count.csv")
    ]

    with engine.connect() as conn:
        for table_name, df_count, source_name in tables_to_verify:
            res = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            db_count = res.scalar()
            match_status = "MATCH" if db_count == df_count else "MISMATCH"
            print(f"Table: {table_name:<25} | DB Row Count: {db_count:<8} | DF Row Count: {df_count:<8} | Status: {match_status} | Source: {source_name}")
            verification_results.append((table_name, db_count, df_count, match_status, source_name))

    # Write verification report
    verification_report_path = WORKSPACE_DIR / "reports" / "data_loading_verification.md"
    with open(verification_report_path, "w", encoding="utf-8") as f:
        f.write("# Data Loading Row Count Verification Report\n\n")
        f.write("| Table Name | DB Row Count | DF Row Count | Status | Source/Notes |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for table_name, db_count, df_count, status, source in verification_results:
            f.write(f"| `{table_name}` | {db_count} | {df_count} | {status} | {source} |\n")
    print(f"\nWrote verification report to {verification_report_path}")


if __name__ == "__main__":
    setup_database_and_load()
