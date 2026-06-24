-- Enable Foreign Key support in SQLite (must be run on connection)
PRAGMA foreign_keys = ON;

-- 1. Dim Fund Table
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT NOT NULL,
    scheme_name TEXT NOT NULL,
    category TEXT NOT NULL,
    sub_category TEXT NOT NULL,
    plan TEXT NOT NULL,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount INTEGER,
    min_lumpsum_amount INTEGER,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

-- 2. Dim Date Table
CREATE TABLE IF NOT EXISTS dim_date (
    date TEXT PRIMARY KEY, -- Format YYYY-MM-DD
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month_name TEXT NOT NULL,
    day_name TEXT NOT NULL,
    is_weekend INTEGER NOT NULL, -- 0 or 1
    day_of_week INTEGER NOT NULL -- 0-6 (Sunday-Saturday or Monday-Sunday)
);

-- 3. Fact Daily NAV Table
CREATE TABLE IF NOT EXISTS fact_nav (
    amfi_code INTEGER NOT NULL,
    date TEXT NOT NULL,
    nav REAL NOT NULL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code) ON DELETE CASCADE,
    FOREIGN KEY (date) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 4. Fact Transactions Table
CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT NOT NULL,
    transaction_date TEXT NOT NULL,
    amfi_code INTEGER NOT NULL,
    transaction_type TEXT NOT NULL, -- SIP, Lumpsum, Redemption
    amount_inr REAL NOT NULL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT, -- Verified, Pending
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code) ON DELETE CASCADE,
    FOREIGN KEY (transaction_date) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 5. Fact Performance Table
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,
    risk_grade TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code) ON DELETE CASCADE
);

-- 6. Fact AUM Table (Fund House Level AUM)
CREATE TABLE IF NOT EXISTS fact_aum (
    date TEXT NOT NULL,
    fund_house TEXT NOT NULL,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER,
    PRIMARY KEY (date, fund_house),
    FOREIGN KEY (date) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 7. Fact Portfolio Holdings
CREATE TABLE IF NOT EXISTS fact_portfolio_holdings (
    amfi_code INTEGER NOT NULL,
    stock_symbol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    sector TEXT NOT NULL,
    weight_pct REAL NOT NULL,
    market_value_cr REAL NOT NULL,
    current_price_inr REAL NOT NULL,
    portfolio_date TEXT NOT NULL,
    PRIMARY KEY (amfi_code, stock_symbol, portfolio_date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund (amfi_code) ON DELETE CASCADE,
    FOREIGN KEY (portfolio_date) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 8. Fact Benchmark Indices
CREATE TABLE IF NOT EXISTS fact_benchmark_indices (
    date TEXT NOT NULL,
    index_name TEXT NOT NULL,
    close_value REAL NOT NULL,
    PRIMARY KEY (date, index_name),
    FOREIGN KEY (date) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 9. Fact Monthly SIP Inflows
CREATE TABLE IF NOT EXISTS fact_monthly_sip_inflows (
    month TEXT PRIMARY KEY, -- Format YYYY-MM-01
    sip_inflow_crore REAL NOT NULL,
    active_sip_accounts_crore REAL NOT NULL,
    new_sip_accounts_lakh REAL NOT NULL,
    sip_aum_lakh_crore REAL NOT NULL,
    yoy_growth_pct REAL,
    FOREIGN KEY (month) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 10. Fact Category Inflows
CREATE TABLE IF NOT EXISTS fact_category_inflows (
    month TEXT NOT NULL, -- Format YYYY-MM-01
    category TEXT NOT NULL,
    net_inflow_crore REAL NOT NULL,
    PRIMARY KEY (month, category),
    FOREIGN KEY (month) REFERENCES dim_date (date) ON DELETE CASCADE
);

-- 11. Fact Folio Count
CREATE TABLE IF NOT EXISTS fact_folio_count (
    month TEXT PRIMARY KEY, -- Format YYYY-MM-01
    total_folios_crore REAL NOT NULL,
    equity_folios_crore REAL NOT NULL,
    debt_folios_crore REAL NOT NULL,
    hybrid_folios_crore REAL NOT NULL,
    others_folios_crore REAL NOT NULL,
    FOREIGN KEY (month) REFERENCES dim_date (date) ON DELETE CASCADE
);
