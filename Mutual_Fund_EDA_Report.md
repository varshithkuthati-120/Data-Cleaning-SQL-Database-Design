# Executive Report: Mutual Fund Exploratory Data Analysis (2022 – 2026)

**Prepared for:** Investment Operations and Strategy Teams  
**Author:** Antigravity Data Science Group  
**Analysis Scope:** January 2022 – May 2026  
**Deliverables:** `EDA_Analysis.ipynb` & 17 Exported Visualizations  

---

## 1. Executive Summary

This report provides a detailed Exploratory Data Analysis (EDA) of mutual fund performance, asset growth, retail investment trends, and investor demographics in India from 2022 to 2026. 

By analyzing scheme-level daily Net Asset Values (NAV), industry-wide assets under management (AUM), monthly Systematic Investment Plan (SIP) inflows, and detailed transaction records for over 32,000 retail investors, we highlight key trends that defined the mutual fund landscape over this period:
* **The retail investment boom** pushed monthly SIP inflows to an all-time high of **₹31,002 Cr** in December 2025.
* **SBI Mutual Fund** solidified its industry leadership, reaching an AUM of **₹12.5L Cr** in 2025.
* **Middle-aged investors (36-45 years)** and Tier-30 (T30) cities continue to drive the core of the market, though B30 (Beyond 30) cities represent a rapidly growing 37% segment.
* **Diversification benefits** are highlighted by the near-zero correlation between equity schemes and debt/liquid assets.

---

## 2. Dataset Overview & Cleaning Methodology

The analysis was performed on a relational schema consisting of the following key datasets:
1. **Fund Master (`dim_fund.csv`)**: Details on the 40 analyzed schemes, including category, plan type, launch date, benchmark index, expense ratios, and risk profiles.
2. **NAV History (`fact_nav.csv`)**: Over 46,000 daily NAV records from January 2022 to May 2026, forward-filled to account for market holidays.
3. **AUM History (`fact_aum.csv`)**: Quarterly/semi-annual asset history for the major fund houses.
4. **SIP Inflows (`fact_monthly_sip_inflows.csv`)**: Monthly aggregated inflows, active accounts, and year-on-year growth rates.
5. **Category Inflows (`fact_category_inflows.csv`)**: Category-wise monthly net flows highlighting sector rotations.
6. **Folio Counts (`fact_folio_count.csv`)**: Industry-wide folio count growth across Equity, Debt, Hybrid, and other asset classes.
7. **Investor Transactions (`fact_transactions.csv`)**: Transaction-level details including amount, type (SIP/Lumpsum/Redemption), state, city tier, age, and gender.
8. **Portfolio Holdings (`fact_portfolio_holdings.csv`)**: Stock-level weights and market values across the equity funds.

---

## 3. Comprehensive Analysis & Detailed Findings

### 3.1. Performance and Market Cycle Analysis
* **The 2023 Bull Run**: Triggered by resilient domestic corporate earnings and capital expenditure cycles, equity NAVs accelerated sharply between April and December 2023. Growth schemes registered substantial capital appreciation.
* **The 2024 Market Corrections**: Occurred in two distinct phases: a mid-cap valuation correction in March 2024 and election-day volatility in June 2024. Despite these drawdowns, the market recovered rapidly, illustrating high liquidity and domestic investor resilience.
* *Supporting Visualizations*: `reports/charts/chart1_daily_nav_trend.png`

### 3.2. Fund House Competition & Scale
* **AUM Dominance**: SBI Mutual Fund maintains a clear lead in AUM, reaching a scale of **₹12.5L Cr** by early 2025. This scale is driven by strong institutional distribution channels, public sector bank tie-ups, and consistent long-term performance in bluechip and small-cap segments.
* **Peer Comparison**: ICICI Prudential MF (₹10.74L Cr) and HDFC Mutual Fund (₹9.3L Cr) represent the closest competitors, growing their market share in the private sector.
* *Supporting Visualizations*: `reports/charts/chart2_aum_growth.png`

### 3.3. Retail Inflow Momentum
* **SIP Exponential Growth**: Monthly SIP inflows grew from **₹11,517 Cr** in January 2022 to **₹31,002 Cr** in December 2025, showing a compounded growth path. The consistent monthly inflows highlight a structural shift in household savings, moving from physical assets (gold, real estate) and traditional deposits to financial assets.
* *Supporting Visualizations*: `reports/charts/chart3_sip_inflow_trend.png`, `reports/charts/chart4_category_inflow_heatmap.png`

### 3.4. Demographics & Wealth Profiles
* **The Core Investor Segment**: Individuals aged **36–45 years** constitute the largest portion of unique investors (approx. 40.5%). This group is followed by the 26-35 age bracket. Together, the 26-45 segment controls over 70% of the active folio base.
* **Wealth Accumulation by Age**: The 36-45 and 46-55 segments exhibit the highest median SIP transaction sizes, as these cohorts are in their peak earning years. In contrast, the younger 18-25 group has smaller SIP sizes, presenting a long-term nurturing opportunity for AMCs.
* **Gender Participation**: The investor gender split is **60.3% Male** and **39.7% Female**. Interestingly, the distribution of SIP transaction sizes between male and female investors is highly similar, suggesting that female investors commit similar ticket sizes as their male counterparts when they enter the market.
* *Supporting Visualizations*: `reports/charts/chart5_age_distribution.png`, `reports/charts/chart6_sip_amount_by_age.png`, `reports/charts/chart7_gender_split.png`, `reports/charts/chart8_sip_amount_by_gender.png`

### 3.5. Geographic Penetration
* **Concentrated Contributions**: Western states (Maharashtra and Gujarat) and southern states (Karnataka and Tamil Nadu) lead total SIP volumes. Maharashtra alone accounts for the largest share of inflows, driven by metropolitan centers like Mumbai and Pune.
* **T30 vs. B30 Tier Split**: T30 (Top 30 cities) represents **63.4% of unique investors** and **65.2% of SIP inflow value**. However, B30 (Beyond 30 cities) has carved out a massive **36.6% market share**, showing that mutual fund awareness has successfully penetrated smaller cities and semi-urban districts.
* *Supporting Visualizations*: `reports/charts/chart9_sip_by_state.png`, `reports/charts/chart10_investor_count_by_state.png`, `reports/charts/chart11_city_tier_distribution.png`, `reports/charts/chart12_city_tier_sip_comparison.png`

### 3.6. Industry Expansion (Folios)
* **Digital Onboarding Impact**: Total industry folios grew from **13.26 Cr** in January 2022 to **26.12 Cr** in December 2025. This near-doubling of accounts was accelerated by simplified KYC norms, mobile-first discount brokers, and digital payment integrations (UPI Autopay).
* **Asset Class Trends**: Equity folios grew at the fastest rate, while debt folios remained flat or slightly declined due to changes in taxation rules (loss of indexation benefits) in 2023.
* *Supporting Visualizations*: `reports/charts/chart13_folio_count_growth.png`, `reports/charts/chart14_folio_count_by_category.png`

### 3.7. Portfolio Asset Allocation
* **Diversification Benefits**: Daily return correlation analysis reveals a strong positive correlation (typically >0.85) among diversified equity funds (Large Cap, Mid Cap, Small Cap). However, debt and liquid funds show correlations close to **0.00** with equity categories, confirming their essential role in portfolio stabilization.
* **Sector Preferences**: Banking/Financial Services, IT, and Pharma represent the top sector allocations across equity holdings. Large-cap schemes show heavy exposure to Banking and IT, while small-cap schemes display a more diversified allocation across Capital Goods, Chemicals, and Consumption.
* *Supporting Visualizations*: `reports/charts/chart15_nav_return_correlation.png`, `reports/charts/chart16_sector_allocation_donut.png`, `reports/charts/chart17_sector_allocation_comparison.png`

---

## 4. Key Analytical Insights Matrix

| Finding | Insight Description | Supporting Visualization |
| :--- | :--- | :--- |
| **1. NAV Trends** | Market cycles from 2022 to 2026 highlight the resilience of domestic equity funds, which recovered swiftly from the 2024 market corrections. | `reports/charts/chart1_daily_nav_trend.png` |
| **2. AUM scale** | SBI Mutual Fund holds a dominant scale advantage, representing the largest single AMC entity with ₹12.5L Cr AUM in 2025. | `reports/charts/chart2_aum_growth.png` |
| **3. Retail Saving** | SIP inflows have crossed the structural threshold of ₹30,000 Cr monthly by the end of 2025, showing resilient retail behavior. | `reports/charts/chart3_sip_inflow_trend.png` |
| **4. Heatmap Trends** | Sectoral/Thematic and Liquid funds led net inflows in 2024, demonstrating periodic investor risk appetite and cash parking. | `reports/charts/chart4_category_inflow_heatmap.png` |
| **5. Demographics** | Middle-aged professionals (36-45 years) represent the primary driver of capital, making up over 40% of the active investor base. | `reports/charts/chart5_age_distribution.png` |
| **6. Capital Size** | The size of monthly SIP commitments is heavily correlated with age, peaking in the 36-55 brackets. | `reports/charts/chart6_sip_amount_by_age.png` |
| **7. State Share** | Maharashtra and Karnataka lead total financial inflows, reflecting a strong geographical concentration of financial wealth. | `reports/charts/chart9_sip_by_state.png` |
| **8. City Tiers** | B30 cities now comprise ~37% of the investor base, indicating that financial inclusion campaigns are yield-positive. | `reports/charts/chart11_city_tier_distribution.png` |
| **9. Folio Counts** | Industry-wide folios doubled over 4 years, highlighting a digital-led retail retailization wave. | `reports/charts/chart13_folio_count_growth.png` |
| **10. Asset Mix** | Debt and liquid funds exhibit zero return correlation with equities, validating their inclusion for portfolio hedging. | `reports/charts/chart15_nav_return_correlation.png` |

---

## 5. Strategic Recommendations for Fund Houses

1. **Leverage the B30 Growth Wave**: AMCs should continue expanding digital vernacular platforms and micro-SIP products (e.g., ₹100-₹250 minimums) to capture the rapid financialization in Tier-3 and rural markets.
2. **Nurture Gen-Z & Millennial Cohorts**: While the 18-25 age group currently has a small average ticket size, their early entry presents a lifetime-value opportunity. Targeted educational content and micro-investing features are key to building long-term loyalty.
3. **Product Innovation in Debt & Hybrid**: With equity valuations rising and taxation changes impacting traditional debt funds, hybrid funds (such as Multi-Asset Allocation and Arbitrage funds) should be promoted as tax-efficient alternatives for conservative investors.
4. **Enhanced Customer Retention Strategies**: Since folio counts are growing rapidly, AMCs must focus on reducing churn during market corrections by implementing proactive customer communications and digital goal-based planning tools.
