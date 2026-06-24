# Data Loading Row Count Verification Report

| Table Name | DB Row Count | DF Row Count | Status | Source/Notes |
| :--- | :--- | :--- | :--- | :--- |
| `dim_date` | 1826 | 1826 | MATCH | Generated calendar |
| `dim_fund` | 40 | 40 | MATCH | 01_fund_master.csv |
| `fact_nav` | 64320 | 64320 | MATCH | 02_nav_history.csv (processed) |
| `fact_transactions` | 32778 | 32778 | MATCH | 08_investor_transactions.csv |
| `fact_performance` | 40 | 40 | MATCH | 07_scheme_performance.csv |
| `fact_aum` | 90 | 90 | MATCH | 03_aum_by_fund_house.csv |
| `fact_portfolio_holdings` | 322 | 322 | MATCH | 09_portfolio_holdings.csv |
| `fact_benchmark_indices` | 8050 | 8050 | MATCH | 10_benchmark_indices.csv |
| `fact_monthly_sip_inflows` | 48 | 48 | MATCH | 04_monthly_sip_inflows.csv |
| `fact_category_inflows` | 144 | 144 | MATCH | 05_category_inflows.csv |
| `fact_folio_count` | 21 | 21 | MATCH | 06_industry_folio_count.csv |
