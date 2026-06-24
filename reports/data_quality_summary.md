# Day 1 Data Quality Summary

- CSV files discovered in `data/raw`: 17
- Expected provided datasets: 10
- Dataset count anomaly: expected 10, found 17

## Dataset Anomalies
- None detected by automated checks.

## Fund Master Exploration
- fund houses: 10 unique values from column 'fund_house'
- categories: 2 unique values from column 'category'
- sub-categories: 12 unique values from column 'sub_category'
- risk grades: 5 unique values from column 'risk_category'
- AMFI scheme codes are numeric scheme identifiers. Treat them as stable IDs, not as a semantic hierarchy where digits encode fund house/category.

## AMFI Code Validation
- fund_master unique AMFI codes: 40
- nav_history unique AMFI codes: 40
- fund_master codes missing in nav_history: 0
- All fund_master AMFI codes exist in nav_history.
