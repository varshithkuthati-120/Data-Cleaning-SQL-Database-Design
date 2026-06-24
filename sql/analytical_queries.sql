-- 1. Top 5 Funds by AUM
-- Ranks funds by AUM in crores (populates from fact_performance).
-- Shows the fund name, fund house, category, and its AUM in crore.
SELECT 
    f.amfi_code,
    f.scheme_name,
    f.fund_house,
    f.category,
    p.aum_crore
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;


-- 2. Average NAV per Month
-- Calculates monthly average NAV for each fund.
SELECT 
    strftime('%Y-%m', n.date) AS month,
    f.scheme_name,
    f.amfi_code,
    ROUND(AVG(n.nav), 4) AS average_nav
FROM fact_nav n
JOIN dim_fund f ON n.amfi_code = f.amfi_code
GROUP BY month, f.amfi_code
ORDER BY month ASC, average_nav DESC;


-- 3. SIP YoY Growth
-- Calculates the YoY growth percentage of total SIP transaction amounts from fact_transactions.
-- It groups by year and month, then joins the monthly amounts with the same month in the previous year.
WITH monthly_sip AS (
    SELECT 
        strftime('%Y-%m', transaction_date) AS yr_mo,
        strftime('%Y', transaction_date) AS yr,
        strftime('%m', transaction_date) AS mo,
        SUM(amount_inr) AS total_sip_amount
    FROM fact_transactions
    WHERE transaction_type = 'SIP'
    GROUP BY yr_mo
)
SELECT 
    m1.yr_mo AS current_month,
    m1.total_sip_amount AS current_amount,
    m2.yr_mo AS prev_year_month,
    m2.total_sip_amount AS prev_amount,
    ROUND(((m1.total_sip_amount - m2.total_sip_amount) * 100.0 / m2.total_sip_amount), 2) AS yoy_growth_pct
FROM monthly_sip m1
JOIN monthly_sip m2 ON m1.mo = m2.mo AND CAST(m1.yr AS INTEGER) = CAST(m2.yr AS INTEGER) + 1
ORDER BY current_month;


-- 4. Transactions by State
-- Aggregates transaction counts and total transaction amount per state from fact_transactions.
SELECT 
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_transaction_amount_inr,
    ROUND(AVG(amount_inr), 2) AS average_transaction_amount_inr
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount_inr DESC;


-- 5. Funds with Expense Ratio < 1%
-- Lists funds with low expense ratios from dim_fund.
SELECT 
    amfi_code,
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;


-- 6. Top 5 Sectors by Portfolio Holdings Market Value
-- Groups portfolio holdings by sector to find the highest market value in crores.
SELECT 
    sector,
    COUNT(DISTINCT stock_symbol) AS unique_stocks_count,
    ROUND(SUM(market_value_cr), 2) AS total_market_value_cr,
    ROUND(AVG(weight_pct), 2) AS average_weight_pct
FROM fact_portfolio_holdings
GROUP BY sector
ORDER BY total_market_value_cr DESC
LIMIT 5;


-- 7. Transactions and Income Stats by Age Group and Transaction Type
-- Shows transaction count, total volume, and average investor annual income grouped by transaction type and age group.
SELECT 
    transaction_type,
    age_group,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount_inr,
    ROUND(AVG(annual_income_lakh), 2) AS average_annual_income_lakh
FROM fact_transactions
GROUP BY transaction_type, age_group
ORDER BY transaction_type ASC, transaction_count DESC;


-- 8. Monthly Net Inflows by Scheme Category
-- Details monthly net inflows for Large Cap, Mid Cap, Small Cap, etc. from category inflows.
SELECT 
    strftime('%Y-%m', month) AS year_month,
    category,
    net_inflow_crore
FROM fact_category_inflows
ORDER BY year_month ASC, net_inflow_crore DESC;


-- 9. Index vs. Fund NAV Performance Comparison
-- Compares the daily close value of the NIFTY100 index to the NAV of SBI Bluechip Fund (AMFI: 119551) which benchmarks against it.
-- This shows how the fund tracks the index value day-to-day.
SELECT 
    n.date,
    f.scheme_name,
    n.nav AS fund_nav,
    b.index_name,
    b.close_value AS index_close_value
FROM fact_nav n
JOIN dim_fund f ON n.amfi_code = f.amfi_code
JOIN fact_benchmark_indices b ON n.date = b.date 
    AND (
        (f.benchmark = 'NIFTY 100 TRI' AND b.index_name = 'NIFTY100') OR
        (f.benchmark = 'NIFTY 50 TRI' AND b.index_name = 'NIFTY50') OR
        (f.benchmark = 'NIFTY Midcap 150 TRI' AND b.index_name = 'NIFTY_MIDCAP150') OR
        (f.benchmark = 'BSE 250 SmallCap TRI' AND b.index_name = 'BSE_SMALLCAP') OR
        (f.benchmark = 'NIFTY 500 TRI' AND b.index_name = 'NIFTY500') OR
        (f.benchmark = 'CRISIL Liquid Fund AI Index' AND b.index_name = 'CRISIL_LIQUID') OR
        (f.benchmark = 'CRISIL Dynamic Gilt Index' AND b.index_name = 'CRISIL_GILT')
    )
WHERE f.amfi_code = 119551
ORDER BY n.date ASC
LIMIT 15;


-- 10. AUM Growth by Fund House over Time
-- Shows quarterly AUM changes and active schemes counts for each AMC.
SELECT 
    date,
    fund_house,
    aum_crore,
    num_schemes
FROM fact_aum
ORDER BY fund_house ASC, date ASC;
