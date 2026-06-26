# Walkthrough - Mutual Fund EDA Analysis

We have successfully performed the Exploratory Data Analysis (EDA) for the mutual fund dataset. The deliverables include the executed notebook [EDA_Analysis.ipynb](file:///C:/Users/varsh/.gemini/antigravity/scratch/mutual-fund-analytics/source%20code/notebooks/EDA_Analysis.ipynb) containing **17 high-quality visualizations** and a dedicated markdown section presenting the **10 key findings**. All charts have been exported as high-resolution PNG files to the [reports/charts/](file:///C:/Users/varsh/.gemini/antigravity/scratch/mutual-fund-analytics/source%20code/reports/charts) directory.

---

## 10 Key EDA Findings & Insights

1. **NAV Growth Trend**: Daily NAV values across all 40 schemes rose significantly from 2022 to 2026, with a strong acceleration during the 2023 bull run and short-term drawdowns during the 2024 market corrections.
   * *Supporting Chart*: [Chart 1: Daily NAV Trend](reports/charts/chart1_daily_nav_trend.png)
2. **AUM Dominance**: SBI Mutual Fund maintains a clear lead in AUM, reaching a dominant scale of ₹12.5L Cr in 2025, showing steady growth from ₹6.05L Cr in 2022.
   * *Supporting Chart*: [Chart 2: AUM Growth Grouped Bar Chart](reports/charts/chart2_aum_growth.png)
3. **SIP Inflow Acceleration**: Monthly SIP inflows showed a continuous upward trend, peaking at an all-time high of ₹31,002 Cr in December 2025, reflecting growing retail investor participation.
   * *Supporting Chart*: [Chart 3: Monthly SIP Inflow Trend](reports/charts/chart3_sip_inflow_trend.png)
4. **Category-wise Inflows**: Sectoral/Thematic and Liquid funds experienced the most intense net inflows in mid-to-late 2024, whereas traditional ELSS funds saw relatively flat or modest inflows.
   * *Supporting Chart*: [Chart 4: Category Inflow Heatmap](reports/charts/chart4_category_inflow_heatmap.png)
5. **Age Demographics**: The age group of 36-45 years represents the largest segment of mutual fund investors, indicating that middle-aged individuals form the core investor base.
   * *Supporting Chart*: [Chart 5: Investor Age Group Distribution](reports/charts/chart5_age_distribution.png)
6. **SIP Sizes by Age**: Investors in the 36-45 and 46-55 age brackets commit higher median SIP amounts compared to younger cohorts (18-25), aligned with their higher disposable income and career progression.
   * *Supporting Chart*: [Chart 6: SIP Transaction Amount by Age Group](reports/charts/chart6_sip_amount_by_age.png)
7. **Geographic Distribution**: Western states like Maharashtra and southern states like Karnataka contribute the highest share of total SIP inflows, indicating a geographic concentration of wealth.
   * *Supporting Chart*: [Chart 9: SIP Inflow by State](reports/charts/chart9_sip_by_state.png)
8. **City Tier Penetration**: While T30 (Top 30) cities still account for the majority of unique investors, B30 (Beyond 30) cities represent a substantial 35%+ share, indicating strong expansion into smaller towns.
   * *Supporting Chart*: [Chart 11: T30 vs B30 City Tier Distribution](reports/charts/chart11_city_tier_distribution.png)
9. **Folio Growth Milestone**: Total industry folios grew exponentially, nearly doubling from 13.26 Cr in January 2022 to 26.12 Cr in December 2025, driven by rapid digitalization and equity market interest.
   * *Supporting Chart*: [Chart 13: Industry Folio Count Growth](reports/charts/chart13_folio_count_growth.png)
10. **NAV Returns Correlation**: High-growth equity funds (such as small-cap and mid-cap funds) exhibit strong positive correlation with each other, while debt and liquid funds show near-zero correlation with equity categories, confirming their diversification benefits.
    * *Supporting Chart*: [Chart 15: NAV Return Correlation Heatmap](reports/charts/chart15_nav_return_correlation.png)

---

## Visualizations Gallery (17 Charts)

### 1. Daily NAV Trend
Interactive time-series of daily NAV for all 40 schemes from 2022 to 2026. Shaded areas represent the **2023 Bull Run** and **2024 Market Corrections**.
![Daily NAV Trend](reports/charts/chart1_daily_nav_trend.png)

### 2. AUM Growth by Fund House
Grouped bar chart showing AUM from 2022 to 2025. **SBI Mutual Fund's ₹12.5L Cr dominance in 2025** is highlighted in gold with a callout arrow.
![AUM Growth](reports/charts/chart2_aum_growth.png)

### 3. Monthly SIP Inflows
Monthly SIP inflows from Jan 2022 to Dec 2025. The all-time high of **₹31,002 Cr (Dec 2025)** is highlighted with an annotated callout box.
![SIP Inflows](reports/charts/chart3_sip_inflow_trend.png)

### 4. Category Inflow Heatmap
Grid heatmap of category net inflows by month. The RdBu colormap highlights positive inflows in blue and negative inflows/redemptions in red.
![Category Inflow Heatmap](reports/charts/chart4_category_inflow_heatmap.png)

### 5-8. Investor Demographics
We analyzed unique investors' demographic split to avoid transactor bias.
- **Chart 5**: Age group distribution pie chart showing 36-45 as the dominant group.
- **Chart 6**: Box plot of SIP amount by age group (excluding outliers to show clean distributions).
- **Chart 7**: Gender distribution pie chart showing a 60/40 male-to-female ratio.
- **Chart 8**: Box plot comparing SIP amount distribution between genders.

````carousel
![Age Group Distribution](reports/charts/chart5_age_distribution.png)
<!-- slide -->
![SIP Amount by Age](reports/charts/chart6_sip_amount_by_age.png)
<!-- slide -->
![Gender Split](reports/charts/chart7_gender_split.png)
<!-- slide -->
![SIP Amount by Gender](reports/charts/chart8_sip_amount_by_gender.png)
````

### 9-12. Geographic Distribution
Geographic analysis comparing SIP inflows across states and top (T30) vs. beyond (B30) city tiers.
- **Chart 9**: Total SIP amount contributed by each state, showing Maharashtra and Karnataka at the top.
- **Chart 10**: Total number of unique investors in each state.
- **Chart 11**: City tier (T30 vs B30) unique investor split (approx. 63% T30, 37% B30).
- **Chart 12**: Total SIP contribution value comparison between T30 and B30.

````carousel
![SIP Inflow by State](reports/charts/chart9_sip_by_state.png)
<!-- slide -->
![Investor Count by State](reports/charts/chart10_investor_count_by_state.png)
<!-- slide -->
![T30 vs B30 Tier Split](reports/charts/chart11_city_tier_distribution.png)
<!-- slide -->
![T30 vs B30 Value Comparison](reports/charts/chart12_city_tier_sip_comparison.png)
````

### 13-14. Folio Count Growth
- **Chart 13**: Total industry folios growing from 13.26 Cr (Jan 2022) to 26.12 Cr (Dec 2025).
- **Chart 14**: Detailed folio growth breakdown across Equity, Debt, Hybrid, and Others.

````carousel
![Total Folio Count Growth](reports/charts/chart13_folio_count_growth.png)
<!-- slide -->
![Folio Growth by Category](reports/charts/chart14_folio_count_by_category.png)
````

### 15. NAV Return Correlation Matrix
Pairwise correlation heatmap of daily return percentages for 10 selected funds across diverse asset classes (large-cap, mid-cap, small-cap, liquid, and gilt). Equity funds are highly correlated (>0.85), whereas debt/liquid funds are uncorrelated (~0.00).
![Correlation Matrix](reports/charts/chart15_nav_return_correlation.png)

### 16-17. Sector Allocation Donuts
- **Chart 16**: Donut chart representing aggregate sector weights across all equity mutual funds.
- **Chart 17**: Side-by-side donut charts comparing Large Cap vs. Small Cap sector allocations.

````carousel
![Aggregate Sector Allocation](reports/charts/chart16_sector_allocation_donut.png)
<!-- slide -->
![Sector Allocation Comparison](reports/charts/chart17_sector_allocation_comparison.png)
````

---

## How to Review
1. The full interactive notebook is available at [notebooks/EDA_Analysis.ipynb](file:///C:/Users/varsh/.gemini/antigravity/scratch/mutual-fund-analytics/source%20code/notebooks/EDA_Analysis.ipynb).
2. The static high-resolution PNG charts are available under [reports/charts/](file:///C:/Users/varsh/.gemini/antigravity/scratch/mutual-fund-analytics/source%20code/reports/charts) for your final presentation.
