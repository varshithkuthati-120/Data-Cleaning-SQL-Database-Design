# Day 2: Analytical SQL Queries Report

This report contains the results of running the 10 analytical SQL queries against the SQLite database.

## Query 1: 1. Top 5 Funds by AUM | Ranks funds by AUM in crores (populates from fact_performance). | Shows the fund name, fund house, category, and its AUM in crore.
```sql
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
```

### Results
| amfi_code | scheme_name | fund_house | category | aum_crore |
| --- | --- | --- | --- | --- |
| 148568 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | Mirae Asset MF | Equity | 49046.0 |
| 120842 | Kotak Emerging Equity Fund - Regular - Growth | Kotak Mahindra MF | Equity | 47469.0 |
| 118634 | Nippon India Small Cap Fund - Regular - Growth | Nippon India MF | Equity | 43630.0 |
| 149322 | DSP Top 100 Equity Fund - Regular - Growth | DSP Mutual Fund | Equity | 41828.0 |
| 102886 | UTI Mid Cap Fund - Regular - Growth | UTI Mutual Fund | Equity | 41728.0 |

---

## Query 2: 2. Average NAV per Month | Calculates monthly average NAV for each fund.
```sql
SELECT 
    strftime('%Y-%m', n.date) AS month,
    f.scheme_name,
    f.amfi_code,
    ROUND(AVG(n.nav), 4) AS average_nav
FROM fact_nav n
JOIN dim_fund f ON n.amfi_code = f.amfi_code
GROUP BY month, f.amfi_code
ORDER BY month ASC, average_nav DESC;
```

### Results
| month | scheme_name | amfi_code | average_nav |
| --- | --- | --- | --- |
| 2022-01 | Kotak Liquid Fund - Regular - Growth | 120844 | 3193.1976 |
| 2022-01 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 553.7507 |
| 2022-01 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 511.923 |
| 2022-01 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 332.0185 |
| 2022-01 | ABSL Liquid Fund - Regular - Growth | 101208 | 311.6791 |
| 2022-01 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 309.9985 |
| 2022-01 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 287.0638 |
| 2022-01 | Kotak Bluechip Fund - Regular - Growth | 120841 | 276.184 |
| 2022-01 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 205.3006 |
| 2022-01 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 183.0768 |
| 2022-01 | Nippon India ETF Nifty 50 BeES | 118635 | 162.4075 |
| 2022-01 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 139.8886 |
| 2022-01 | UTI Mid Cap Fund - Regular - Growth | 102886 | 122.7674 |
| 2022-01 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 113.6955 |
| 2022-01 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 104.7011 |
| 2022-01 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 98.9478 |
| 2022-01 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 95.5875 |
| 2022-01 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 91.238 |
| 2022-01 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 83.9796 |
| 2022-01 | DSP Small Cap Fund - Regular - Growth | 149324 | 80.894 |
| 2022-01 | DSP Midcap Fund - Regular - Growth | 149323 | 79.3253 |
| 2022-01 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 76.1067 |
| 2022-01 | Axis Midcap Fund - Regular - Growth | 119094 | 67.4752 |
| 2022-01 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 65.1637 |
| 2022-01 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 62.3008 |
| 2022-01 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 61.9065 |
| 2022-01 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 58.8013 |
| 2022-01 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 58.7945 |
| 2022-01 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 55.0386 |
| 2022-01 | Axis Small Cap Fund - Regular - Growth | 119095 | 52.715 |
| 2022-01 | Kotak Flexicap Fund - Regular - Growth | 120843 | 49.2312 |
| 2022-01 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 46.1369 |
| 2022-01 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 44.0709 |
| 2022-01 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 42.4326 |
| 2022-01 | Axis Bluechip Fund - Direct - Growth | 119093 | 40.4955 |
| 2022-01 | Axis Bluechip Fund - Regular - Growth | 119092 | 38.9021 |
| 2022-01 | ABSL Small Cap Fund - Regular - Growth | 101207 | 38.7224 |
| 2022-01 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 30.3266 |
| 2022-01 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 29.355 |
| 2022-01 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 26.2604 |
| 2022-02 | Kotak Liquid Fund - Regular - Growth | 120844 | 3214.0686 |
| 2022-02 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 544.2455 |
| 2022-02 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 514.5381 |
| 2022-02 | ABSL Liquid Fund - Regular - Growth | 101208 | 313.7182 |
| 2022-02 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 311.2782 |
| 2022-02 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 304.8332 |
| 2022-02 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 288.9582 |
| 2022-02 | Kotak Bluechip Fund - Regular - Growth | 120841 | 268.6167 |
| 2022-02 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 215.2019 |
| 2022-02 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 176.9473 |
| 2022-02 | Nippon India ETF Nifty 50 BeES | 118635 | 162.8878 |
| 2022-02 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 154.4916 |
| 2022-02 | UTI Mid Cap Fund - Regular - Growth | 102886 | 128.9792 |
| 2022-02 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 109.9354 |
| 2022-02 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 109.555 |
| 2022-02 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 105.9526 |
| 2022-02 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 92.2937 |
| 2022-02 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 92.1976 |
| 2022-02 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 81.2621 |
| 2022-02 | DSP Midcap Fund - Regular - Growth | 149323 | 81.1739 |
| 2022-02 | DSP Small Cap Fund - Regular - Growth | 149324 | 80.8333 |
| 2022-02 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 79.6865 |
| 2022-02 | Axis Midcap Fund - Regular - Growth | 119094 | 70.066 |
| 2022-02 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.2654 |
| 2022-02 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 62.915 |
| 2022-02 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 61.7086 |
| 2022-02 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 60.3818 |
| 2022-02 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 58.8808 |
| 2022-02 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 52.4312 |
| 2022-02 | Axis Small Cap Fund - Regular - Growth | 119095 | 49.5339 |
| 2022-02 | Kotak Flexicap Fund - Regular - Growth | 120843 | 48.4893 |
| 2022-02 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 47.8156 |
| 2022-02 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 46.2249 |
| 2022-02 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 42.443 |
| 2022-02 | Axis Bluechip Fund - Direct - Growth | 119093 | 41.014 |
| 2022-02 | Axis Bluechip Fund - Regular - Growth | 119092 | 39.8856 |
| 2022-02 | ABSL Small Cap Fund - Regular - Growth | 101207 | 39.6213 |
| 2022-02 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 30.7838 |
| 2022-02 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 29.3306 |
| 2022-02 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 26.4528 |
| 2022-03 | Kotak Liquid Fund - Regular - Growth | 120844 | 3235.7619 |
| 2022-03 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 548.5015 |
| 2022-03 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 522.2865 |
| 2022-03 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 315.994 |
| 2022-03 | ABSL Liquid Fund - Regular - Growth | 101208 | 315.966 |
| 2022-03 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 306.0124 |
| 2022-03 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 290.4607 |
| 2022-03 | Kotak Bluechip Fund - Regular - Growth | 120841 | 269.5571 |
| 2022-03 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 225.3204 |
| 2022-03 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 174.6729 |
| 2022-03 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 171.0289 |
| 2022-03 | Nippon India ETF Nifty 50 BeES | 118635 | 162.9124 |
| 2022-03 | UTI Mid Cap Fund - Regular - Growth | 102886 | 132.2345 |
| 2022-03 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 111.2319 |
| 2022-03 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 105.1616 |
| 2022-03 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 103.7258 |
| 2022-03 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 91.8838 |
| 2022-03 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 85.708 |
| 2022-03 | DSP Small Cap Fund - Regular - Growth | 149324 | 84.4066 |
| 2022-03 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 83.3301 |
| 2022-03 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 80.4925 |
| 2022-03 | DSP Midcap Fund - Regular - Growth | 149323 | 79.661 |
| 2022-03 | Axis Midcap Fund - Regular - Growth | 119094 | 72.7894 |
| 2022-03 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.3032 |
| 2022-03 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 67.0563 |
| 2022-03 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 63.1021 |
| 2022-03 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 62.1624 |
| 2022-03 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 59.0773 |
| 2022-03 | Axis Small Cap Fund - Regular - Growth | 119095 | 52.4921 |
| 2022-03 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 50.837 |
| 2022-03 | Kotak Flexicap Fund - Regular - Growth | 120843 | 49.2229 |
| 2022-03 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 48.9004 |
| 2022-03 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 47.6934 |
| 2022-03 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 42.2394 |
| 2022-03 | ABSL Small Cap Fund - Regular - Growth | 101207 | 40.2075 |
| 2022-03 | Axis Bluechip Fund - Direct - Growth | 119093 | 39.7123 |
| 2022-03 | Axis Bluechip Fund - Regular - Growth | 119092 | 38.1884 |
| 2022-03 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 31.2528 |
| 2022-03 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 30.395 |
| 2022-03 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 26.722 |
| 2022-04 | Kotak Liquid Fund - Regular - Growth | 120844 | 3260.5655 |
| 2022-04 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 578.3661 |
| 2022-04 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 526.1147 |
| 2022-04 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 332.0753 |
| 2022-04 | ABSL Liquid Fund - Regular - Growth | 101208 | 317.6076 |
| 2022-04 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 307.1976 |
| 2022-04 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 291.7194 |
| 2022-04 | Kotak Bluechip Fund - Regular - Growth | 120841 | 259.3801 |
| 2022-04 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 233.2645 |
| 2022-04 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 184.3875 |
| 2022-04 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 171.0904 |
| 2022-04 | Nippon India ETF Nifty 50 BeES | 118635 | 164.554 |
| 2022-04 | UTI Mid Cap Fund - Regular - Growth | 102886 | 128.4215 |
| 2022-04 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 107.057 |
| 2022-04 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 103.1671 |
| 2022-04 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 96.786 |
| 2022-04 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 91.2135 |
| 2022-04 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 88.3619 |
| 2022-04 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 84.9726 |
| 2022-04 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 83.1741 |
| 2022-04 | DSP Small Cap Fund - Regular - Growth | 149324 | 79.7679 |
| 2022-04 | DSP Midcap Fund - Regular - Growth | 149323 | 79.0696 |
| 2022-04 | Axis Midcap Fund - Regular - Growth | 119094 | 74.0708 |
| 2022-04 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 71.0442 |
| 2022-04 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 64.5053 |
| 2022-04 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 63.9535 |
| 2022-04 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.261 |
| 2022-04 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 60.1732 |
| 2022-04 | Axis Small Cap Fund - Regular - Growth | 119095 | 53.2788 |
| 2022-04 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 51.8935 |
| 2022-04 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 51.4092 |
| 2022-04 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 51.0257 |
| 2022-04 | Kotak Flexicap Fund - Regular - Growth | 120843 | 45.6445 |
| 2022-04 | ABSL Small Cap Fund - Regular - Growth | 101207 | 42.7833 |
| 2022-04 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 42.6578 |
| 2022-04 | Axis Bluechip Fund - Direct - Growth | 119093 | 39.2449 |
| 2022-04 | Axis Bluechip Fund - Regular - Growth | 119092 | 36.0476 |
| 2022-04 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 33.4149 |
| 2022-04 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.0028 |
| 2022-04 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.0313 |
| 2022-05 | Kotak Liquid Fund - Regular - Growth | 120844 | 3274.6944 |
| 2022-05 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 597.7736 |
| 2022-05 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 504.3357 |
| 2022-05 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 345.138 |
| 2022-05 | ABSL Liquid Fund - Regular - Growth | 101208 | 319.2234 |
| 2022-05 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 306.2492 |
| 2022-05 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 293.2938 |
| 2022-05 | Kotak Bluechip Fund - Regular - Growth | 120841 | 257.5495 |
| 2022-05 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 226.9038 |
| 2022-05 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 186.9619 |
| 2022-05 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 170.3763 |
| 2022-05 | Nippon India ETF Nifty 50 BeES | 118635 | 160.1274 |
| 2022-05 | UTI Mid Cap Fund - Regular - Growth | 102886 | 127.291 |
| 2022-05 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 102.471 |
| 2022-05 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 100.2928 |
| 2022-05 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 98.7202 |
| 2022-05 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 96.542 |
| 2022-05 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 92.93 |
| 2022-05 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 84.2439 |
| 2022-05 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 83.4524 |
| 2022-05 | DSP Small Cap Fund - Regular - Growth | 149324 | 82.0899 |
| 2022-05 | DSP Midcap Fund - Regular - Growth | 149323 | 82.0495 |
| 2022-05 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 75.8891 |
| 2022-05 | Axis Midcap Fund - Regular - Growth | 119094 | 72.0758 |
| 2022-05 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 65.9852 |
| 2022-05 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 65.7703 |
| 2022-05 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 62.8803 |
| 2022-05 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 60.4265 |
| 2022-05 | Axis Small Cap Fund - Regular - Growth | 119095 | 58.1126 |
| 2022-05 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 54.1248 |
| 2022-05 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 52.3622 |
| 2022-05 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 51.8872 |
| 2022-05 | Kotak Flexicap Fund - Regular - Growth | 120843 | 46.543 |
| 2022-05 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 42.7899 |
| 2022-05 | ABSL Small Cap Fund - Regular - Growth | 101207 | 40.4933 |
| 2022-05 | Axis Bluechip Fund - Direct - Growth | 119093 | 37.9619 |
| 2022-05 | Axis Bluechip Fund - Regular - Growth | 119092 | 36.2173 |
| 2022-05 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 33.336 |
| 2022-05 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.631 |
| 2022-05 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.1765 |
| 2022-06 | Kotak Liquid Fund - Regular - Growth | 120844 | 3291.0795 |
| 2022-06 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 658.0954 |
| 2022-06 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 465.3772 |
| 2022-06 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 338.0698 |
| 2022-06 | ABSL Liquid Fund - Regular - Growth | 101208 | 320.079 |
| 2022-06 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 315.5928 |
| 2022-06 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 295.4965 |
| 2022-06 | Kotak Bluechip Fund - Regular - Growth | 120841 | 258.451 |
| 2022-06 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 226.547 |
| 2022-06 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 180.4984 |
| 2022-06 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 157.8934 |
| 2022-06 | Nippon India ETF Nifty 50 BeES | 118635 | 156.1528 |
| 2022-06 | UTI Mid Cap Fund - Regular - Growth | 102886 | 130.1398 |
| 2022-06 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 104.9787 |
| 2022-06 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 103.7624 |
| 2022-06 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 100.2767 |
| 2022-06 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 99.1645 |
| 2022-06 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 92.5849 |
| 2022-06 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 86.5416 |
| 2022-06 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 83.3397 |
| 2022-06 | DSP Small Cap Fund - Regular - Growth | 149324 | 83.0981 |
| 2022-06 | DSP Midcap Fund - Regular - Growth | 149323 | 83.0694 |
| 2022-06 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 72.6024 |
| 2022-06 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 67.8819 |
| 2022-06 | Axis Midcap Fund - Regular - Growth | 119094 | 66.6196 |
| 2022-06 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 66.0044 |
| 2022-06 | Axis Small Cap Fund - Regular - Growth | 119095 | 65.6451 |
| 2022-06 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 62.7211 |
| 2022-06 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 62.6256 |
| 2022-06 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 53.1347 |
| 2022-06 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 52.981 |
| 2022-06 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 52.6761 |
| 2022-06 | Kotak Flexicap Fund - Regular - Growth | 120843 | 48.4147 |
| 2022-06 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.6172 |
| 2022-06 | ABSL Small Cap Fund - Regular - Growth | 101207 | 39.0659 |
| 2022-06 | Axis Bluechip Fund - Direct - Growth | 119093 | 38.3315 |
| 2022-06 | Axis Bluechip Fund - Regular - Growth | 119092 | 36.916 |
| 2022-06 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 34.9514 |
| 2022-06 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.4409 |
| 2022-06 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.3498 |
| 2022-07 | Kotak Liquid Fund - Regular - Growth | 120844 | 3312.6332 |
| 2022-07 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 646.6987 |
| 2022-07 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 436.7731 |
| 2022-07 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 331.7213 |
| 2022-07 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 325.4345 |
| 2022-07 | ABSL Liquid Fund - Regular - Growth | 101208 | 321.8943 |
| 2022-07 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 297.3988 |
| 2022-07 | Kotak Bluechip Fund - Regular - Growth | 120841 | 251.6201 |
| 2022-07 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 218.5705 |
| 2022-07 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 176.5532 |
| 2022-07 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 159.1607 |
| 2022-07 | Nippon India ETF Nifty 50 BeES | 118635 | 158.7109 |
| 2022-07 | UTI Mid Cap Fund - Regular - Growth | 102886 | 130.391 |
| 2022-07 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 109.8317 |
| 2022-07 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 106.896 |
| 2022-07 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 106.2818 |
| 2022-07 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 104.5506 |
| 2022-07 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 91.5368 |
| 2022-07 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 87.5379 |
| 2022-07 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 82.507 |
| 2022-07 | DSP Midcap Fund - Regular - Growth | 149323 | 81.9429 |
| 2022-07 | DSP Small Cap Fund - Regular - Growth | 149324 | 77.9907 |
| 2022-07 | Axis Small Cap Fund - Regular - Growth | 119095 | 75.6721 |
| 2022-07 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 72.1007 |
| 2022-07 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 70.4813 |
| 2022-07 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 69.3996 |
| 2022-07 | Axis Midcap Fund - Regular - Growth | 119094 | 65.5541 |
| 2022-07 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 64.3436 |
| 2022-07 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 59.4234 |
| 2022-07 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 54.1228 |
| 2022-07 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 52.694 |
| 2022-07 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 51.5161 |
| 2022-07 | Kotak Flexicap Fund - Regular - Growth | 120843 | 48.5021 |
| 2022-07 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.9626 |
| 2022-07 | ABSL Small Cap Fund - Regular - Growth | 101207 | 43.8419 |
| 2022-07 | Axis Bluechip Fund - Regular - Growth | 119092 | 37.6962 |
| 2022-07 | Axis Bluechip Fund - Direct - Growth | 119093 | 35.9974 |
| 2022-07 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 35.6386 |
| 2022-07 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.883 |
| 2022-07 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.5118 |
| 2022-08 | Kotak Liquid Fund - Regular - Growth | 120844 | 3331.1163 |
| 2022-08 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 648.4211 |
| 2022-08 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 420.9213 |
| 2022-08 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 342.3022 |
| 2022-08 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 329.5154 |
| 2022-08 | ABSL Liquid Fund - Regular - Growth | 101208 | 324.0451 |
| 2022-08 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 299.0253 |
| 2022-08 | Kotak Bluechip Fund - Regular - Growth | 120841 | 255.0147 |
| 2022-08 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 222.1511 |
| 2022-08 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 193.5278 |
| 2022-08 | Nippon India ETF Nifty 50 BeES | 118635 | 160.7313 |
| 2022-08 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 155.1472 |
| 2022-08 | UTI Mid Cap Fund - Regular - Growth | 102886 | 122.5064 |
| 2022-08 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 117.5879 |
| 2022-08 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 112.8083 |
| 2022-08 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 107.4412 |
| 2022-08 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 106.2645 |
| 2022-08 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 93.7864 |
| 2022-08 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 87.9246 |
| 2022-08 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 85.4823 |
| 2022-08 | DSP Midcap Fund - Regular - Growth | 149323 | 80.7572 |
| 2022-08 | DSP Small Cap Fund - Regular - Growth | 149324 | 77.8929 |
| 2022-08 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 75.8673 |
| 2022-08 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 71.9688 |
| 2022-08 | Axis Small Cap Fund - Regular - Growth | 119095 | 71.0264 |
| 2022-08 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 70.4881 |
| 2022-08 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 66.0381 |
| 2022-08 | Axis Midcap Fund - Regular - Growth | 119094 | 64.7301 |
| 2022-08 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 60.3854 |
| 2022-08 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 53.8042 |
| 2022-08 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 53.7836 |
| 2022-08 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 53.0576 |
| 2022-08 | Kotak Flexicap Fund - Regular - Growth | 120843 | 48.5039 |
| 2022-08 | ABSL Small Cap Fund - Regular - Growth | 101207 | 48.2908 |
| 2022-08 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 44.1839 |
| 2022-08 | Axis Bluechip Fund - Regular - Growth | 119092 | 38.3575 |
| 2022-08 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 36.5088 |
| 2022-08 | Axis Bluechip Fund - Direct - Growth | 119093 | 35.8062 |
| 2022-08 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.0391 |
| 2022-08 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.6024 |
| 2022-09 | Kotak Liquid Fund - Regular - Growth | 120844 | 3352.7187 |
| 2022-09 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 675.1116 |
| 2022-09 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 422.4281 |
| 2022-09 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 343.8401 |
| 2022-09 | ABSL Liquid Fund - Regular - Growth | 101208 | 325.6589 |
| 2022-09 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 320.8017 |
| 2022-09 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 300.6674 |
| 2022-09 | Kotak Bluechip Fund - Regular - Growth | 120841 | 264.2498 |
| 2022-09 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 224.0224 |
| 2022-09 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 199.4999 |
| 2022-09 | Nippon India ETF Nifty 50 BeES | 118635 | 162.6202 |
| 2022-09 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 156.8233 |
| 2022-09 | UTI Mid Cap Fund - Regular - Growth | 102886 | 122.3763 |
| 2022-09 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 116.7198 |
| 2022-09 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 116.385 |
| 2022-09 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 111.2432 |
| 2022-09 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 106.7618 |
| 2022-09 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 94.916 |
| 2022-09 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 93.8592 |
| 2022-09 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 90.1837 |
| 2022-09 | DSP Small Cap Fund - Regular - Growth | 149324 | 80.8635 |
| 2022-09 | DSP Midcap Fund - Regular - Growth | 149323 | 79.8182 |
| 2022-09 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 77.5312 |
| 2022-09 | Axis Small Cap Fund - Regular - Growth | 119095 | 74.3854 |
| 2022-09 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 73.098 |
| 2022-09 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 71.7158 |
| 2022-09 | Axis Midcap Fund - Regular - Growth | 119094 | 67.8715 |
| 2022-09 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 66.3692 |
| 2022-09 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 62.188 |
| 2022-09 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 56.5077 |
| 2022-09 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 54.8647 |
| 2022-09 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 53.1992 |
| 2022-09 | ABSL Small Cap Fund - Regular - Growth | 101207 | 51.7697 |
| 2022-09 | Kotak Flexicap Fund - Regular - Growth | 120843 | 50.7046 |
| 2022-09 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.9745 |
| 2022-09 | Axis Bluechip Fund - Regular - Growth | 119092 | 39.8699 |
| 2022-09 | Axis Bluechip Fund - Direct - Growth | 119093 | 37.0165 |
| 2022-09 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 35.8925 |
| 2022-09 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.9029 |
| 2022-09 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.5188 |
| 2022-10 | Kotak Liquid Fund - Regular - Growth | 120844 | 3373.9126 |
| 2022-10 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 667.3554 |
| 2022-10 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 431.3465 |
| 2022-10 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 335.0979 |
| 2022-10 | ABSL Liquid Fund - Regular - Growth | 101208 | 327.6417 |
| 2022-10 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 310.1211 |
| 2022-10 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 301.9889 |
| 2022-10 | Kotak Bluechip Fund - Regular - Growth | 120841 | 267.485 |
| 2022-10 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 219.969 |
| 2022-10 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 201.8071 |
| 2022-10 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 164.814 |
| 2022-10 | Nippon India ETF Nifty 50 BeES | 118635 | 158.8745 |
| 2022-10 | UTI Mid Cap Fund - Regular - Growth | 102886 | 123.3811 |
| 2022-10 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 119.8664 |
| 2022-10 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 115.9076 |
| 2022-10 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 115.1668 |
| 2022-10 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 109.2308 |
| 2022-10 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 101.1948 |
| 2022-10 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 95.1083 |
| 2022-10 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 92.9963 |
| 2022-10 | DSP Small Cap Fund - Regular - Growth | 149324 | 81.0944 |
| 2022-10 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 78.0881 |
| 2022-10 | Axis Small Cap Fund - Regular - Growth | 119095 | 77.3488 |
| 2022-10 | DSP Midcap Fund - Regular - Growth | 149323 | 76.989 |
| 2022-10 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 74.399 |
| 2022-10 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 71.2591 |
| 2022-10 | Axis Midcap Fund - Regular - Growth | 119094 | 66.3177 |
| 2022-10 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 64.4048 |
| 2022-10 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 61.8025 |
| 2022-10 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 57.8759 |
| 2022-10 | ABSL Small Cap Fund - Regular - Growth | 101207 | 56.162 |
| 2022-10 | Kotak Flexicap Fund - Regular - Growth | 120843 | 54.6825 |
| 2022-10 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 54.5951 |
| 2022-10 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 53.2597 |
| 2022-10 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.3531 |
| 2022-10 | Axis Bluechip Fund - Regular - Growth | 119092 | 42.7173 |
| 2022-10 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 36.5478 |
| 2022-10 | Axis Bluechip Fund - Direct - Growth | 119093 | 36.4006 |
| 2022-10 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.2768 |
| 2022-10 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.2985 |
| 2022-11 | Kotak Liquid Fund - Regular - Growth | 120844 | 3391.0868 |
| 2022-11 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 663.3705 |
| 2022-11 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 463.8356 |
| 2022-11 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 351.7515 |
| 2022-11 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 329.758 |
| 2022-11 | ABSL Liquid Fund - Regular - Growth | 101208 | 329.4613 |
| 2022-11 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 303.5851 |
| 2022-11 | Kotak Bluechip Fund - Regular - Growth | 120841 | 272.8272 |
| 2022-11 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 215.047 |
| 2022-11 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 207.1322 |
| 2022-11 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 173.11 |
| 2022-11 | Nippon India ETF Nifty 50 BeES | 118635 | 156.6371 |
| 2022-11 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 126.9978 |
| 2022-11 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 124.8921 |
| 2022-11 | UTI Mid Cap Fund - Regular - Growth | 102886 | 122.2474 |
| 2022-11 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 117.3339 |
| 2022-11 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 113.6839 |
| 2022-11 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 109.3641 |
| 2022-11 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 103.9673 |
| 2022-11 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 95.6736 |
| 2022-11 | DSP Small Cap Fund - Regular - Growth | 149324 | 91.6916 |
| 2022-11 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 88.6666 |
| 2022-11 | DSP Midcap Fund - Regular - Growth | 149323 | 77.7575 |
| 2022-11 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 77.218 |
| 2022-11 | Axis Small Cap Fund - Regular - Growth | 119095 | 74.2752 |
| 2022-11 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 69.8138 |
| 2022-11 | Axis Midcap Fund - Regular - Growth | 119094 | 69.5192 |
| 2022-11 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 63.1493 |
| 2022-11 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 60.8367 |
| 2022-11 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 60.8207 |
| 2022-11 | Kotak Flexicap Fund - Regular - Growth | 120843 | 56.2551 |
| 2022-11 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 53.3533 |
| 2022-11 | ABSL Small Cap Fund - Regular - Growth | 101207 | 51.259 |
| 2022-11 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 50.9291 |
| 2022-11 | Axis Bluechip Fund - Regular - Growth | 119092 | 44.4971 |
| 2022-11 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.3747 |
| 2022-11 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 37.7738 |
| 2022-11 | Axis Bluechip Fund - Direct - Growth | 119093 | 36.4243 |
| 2022-11 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.4726 |
| 2022-11 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.399 |
| 2022-12 | Kotak Liquid Fund - Regular - Growth | 120844 | 3405.2862 |
| 2022-12 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 649.6308 |
| 2022-12 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 480.8736 |
| 2022-12 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 358.8231 |
| 2022-12 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 341.3693 |
| 2022-12 | ABSL Liquid Fund - Regular - Growth | 101208 | 331.7651 |
| 2022-12 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 305.0313 |
| 2022-12 | Kotak Bluechip Fund - Regular - Growth | 120841 | 271.697 |
| 2022-12 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 220.0366 |
| 2022-12 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 208.5226 |
| 2022-12 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 175.8494 |
| 2022-12 | Nippon India ETF Nifty 50 BeES | 118635 | 163.0524 |
| 2022-12 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 145.9177 |
| 2022-12 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 130.9587 |
| 2022-12 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 119.3992 |
| 2022-12 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 117.7737 |
| 2022-12 | UTI Mid Cap Fund - Regular - Growth | 102886 | 117.4391 |
| 2022-12 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 114.7847 |
| 2022-12 | DSP Small Cap Fund - Regular - Growth | 149324 | 106.0201 |
| 2022-12 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 102.0756 |
| 2022-12 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 97.9357 |
| 2022-12 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 93.5058 |
| 2022-12 | DSP Midcap Fund - Regular - Growth | 149323 | 86.1296 |
| 2022-12 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 78.8703 |
| 2022-12 | Axis Small Cap Fund - Regular - Growth | 119095 | 74.6317 |
| 2022-12 | Axis Midcap Fund - Regular - Growth | 119094 | 71.866 |
| 2022-12 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 67.8438 |
| 2022-12 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 67.101 |
| 2022-12 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 64.1933 |
| 2022-12 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 61.376 |
| 2022-12 | Kotak Flexicap Fund - Regular - Growth | 120843 | 57.5763 |
| 2022-12 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 54.0255 |
| 2022-12 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 50.7311 |
| 2022-12 | ABSL Small Cap Fund - Regular - Growth | 101207 | 50.5852 |
| 2022-12 | Axis Bluechip Fund - Regular - Growth | 119092 | 45.9983 |
| 2022-12 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.5756 |
| 2022-12 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 41.0743 |
| 2022-12 | Axis Bluechip Fund - Direct - Growth | 119093 | 35.5248 |
| 2022-12 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.687 |
| 2022-12 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.4755 |
| 2023-01 | Kotak Liquid Fund - Regular - Growth | 120844 | 3428.8365 |
| 2023-01 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 645.9216 |
| 2023-01 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 490.8455 |
| 2023-01 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 371.1166 |
| 2023-01 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 346.1082 |
| 2023-01 | ABSL Liquid Fund - Regular - Growth | 101208 | 334.0522 |
| 2023-01 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 306.143 |
| 2023-01 | Kotak Bluechip Fund - Regular - Growth | 120841 | 276.671 |
| 2023-01 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 242.2514 |
| 2023-01 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 206.004 |
| 2023-01 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 171.5405 |
| 2023-01 | Nippon India ETF Nifty 50 BeES | 118635 | 170.6702 |
| 2023-01 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 154.561 |
| 2023-01 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 128.7039 |
| 2023-01 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 128.5753 |
| 2023-01 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 122.5316 |
| 2023-01 | UTI Mid Cap Fund - Regular - Growth | 102886 | 120.0223 |
| 2023-01 | DSP Small Cap Fund - Regular - Growth | 149324 | 116.4076 |
| 2023-01 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 115.5152 |
| 2023-01 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 109.0893 |
| 2023-01 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 101.4433 |
| 2023-01 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 98.1815 |
| 2023-01 | DSP Midcap Fund - Regular - Growth | 149323 | 87.8692 |
| 2023-01 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 79.5594 |
| 2023-01 | Axis Small Cap Fund - Regular - Growth | 119095 | 78.1176 |
| 2023-01 | Axis Midcap Fund - Regular - Growth | 119094 | 77.8484 |
| 2023-01 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 71.3078 |
| 2023-01 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 67.3266 |
| 2023-01 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 65.7721 |
| 2023-01 | Kotak Flexicap Fund - Regular - Growth | 120843 | 60.7443 |
| 2023-01 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 60.2519 |
| 2023-01 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 55.3833 |
| 2023-01 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 53.44 |
| 2023-01 | ABSL Small Cap Fund - Regular - Growth | 101207 | 52.2434 |
| 2023-01 | Axis Bluechip Fund - Regular - Growth | 119092 | 46.3405 |
| 2023-01 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 43.9414 |
| 2023-01 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 42.4169 |
| 2023-01 | Axis Bluechip Fund - Direct - Growth | 119093 | 35.3616 |
| 2023-01 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.8326 |
| 2023-01 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.8574 |
| 2023-02 | Kotak Liquid Fund - Regular - Growth | 120844 | 3446.671 |
| 2023-02 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 657.5074 |
| 2023-02 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 492.4466 |
| 2023-02 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 380.8846 |
| 2023-02 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 353.3149 |
| 2023-02 | ABSL Liquid Fund - Regular - Growth | 101208 | 335.9159 |
| 2023-02 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 307.5217 |
| 2023-02 | Kotak Bluechip Fund - Regular - Growth | 120841 | 281.3342 |
| 2023-02 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 256.7346 |
| 2023-02 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 203.9274 |
| 2023-02 | Nippon India ETF Nifty 50 BeES | 118635 | 176.7309 |
| 2023-02 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 176.6909 |
| 2023-02 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 145.9901 |
| 2023-02 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 139.2487 |
| 2023-02 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 134.6413 |
| 2023-02 | UTI Mid Cap Fund - Regular - Growth | 102886 | 127.9976 |
| 2023-02 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 125.8817 |
| 2023-02 | DSP Small Cap Fund - Regular - Growth | 149324 | 121.891 |
| 2023-02 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 116.5851 |
| 2023-02 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 116.2633 |
| 2023-02 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 102.1093 |
| 2023-02 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 95.4447 |
| 2023-02 | DSP Midcap Fund - Regular - Growth | 149323 | 86.5733 |
| 2023-02 | Axis Midcap Fund - Regular - Growth | 119094 | 82.3499 |
| 2023-02 | Axis Small Cap Fund - Regular - Growth | 119095 | 79.616 |
| 2023-02 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 77.749 |
| 2023-02 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 74.5768 |
| 2023-02 | Kotak Flexicap Fund - Regular - Growth | 120843 | 67.2305 |
| 2023-02 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 66.352 |
| 2023-02 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.7096 |
| 2023-02 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 61.238 |
| 2023-02 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 58.66 |
| 2023-02 | ABSL Small Cap Fund - Regular - Growth | 101207 | 53.0568 |
| 2023-02 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 52.9425 |
| 2023-02 | Axis Bluechip Fund - Regular - Growth | 119092 | 46.6976 |
| 2023-02 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 45.776 |
| 2023-02 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 44.2128 |
| 2023-02 | Axis Bluechip Fund - Direct - Growth | 119093 | 34.7661 |
| 2023-02 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.972 |
| 2023-02 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.1297 |
| 2023-03 | Kotak Liquid Fund - Regular - Growth | 120844 | 3467.4121 |
| 2023-03 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 671.4523 |
| 2023-03 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 545.7361 |
| 2023-03 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 384.3806 |
| 2023-03 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 350.9181 |
| 2023-03 | ABSL Liquid Fund - Regular - Growth | 101208 | 337.3478 |
| 2023-03 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 309.6447 |
| 2023-03 | Kotak Bluechip Fund - Regular - Growth | 120841 | 285.7026 |
| 2023-03 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 266.8131 |
| 2023-03 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 200.4432 |
| 2023-03 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 190.853 |
| 2023-03 | Nippon India ETF Nifty 50 BeES | 118635 | 185.0004 |
| 2023-03 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 143.6692 |
| 2023-03 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 139.9037 |
| 2023-03 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 132.0885 |
| 2023-03 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 125.38 |
| 2023-03 | UTI Mid Cap Fund - Regular - Growth | 102886 | 125.0022 |
| 2023-03 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 123.786 |
| 2023-03 | DSP Small Cap Fund - Regular - Growth | 149324 | 118.7719 |
| 2023-03 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 111.3454 |
| 2023-03 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 104.0342 |
| 2023-03 | DSP Midcap Fund - Regular - Growth | 149323 | 98.0593 |
| 2023-03 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 94.3645 |
| 2023-03 | Axis Small Cap Fund - Regular - Growth | 119095 | 85.3588 |
| 2023-03 | Axis Midcap Fund - Regular - Growth | 119094 | 84.2842 |
| 2023-03 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 80.2166 |
| 2023-03 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 78.4846 |
| 2023-03 | Kotak Flexicap Fund - Regular - Growth | 120843 | 71.8076 |
| 2023-03 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 68.8655 |
| 2023-03 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 64.5104 |
| 2023-03 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.9289 |
| 2023-03 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 60.9074 |
| 2023-03 | ABSL Small Cap Fund - Regular - Growth | 101207 | 56.7666 |
| 2023-03 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 53.0847 |
| 2023-03 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 48.4846 |
| 2023-03 | Axis Bluechip Fund - Regular - Growth | 119092 | 46.2791 |
| 2023-03 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 44.0851 |
| 2023-03 | Axis Bluechip Fund - Direct - Growth | 119093 | 34.7288 |
| 2023-03 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.8824 |
| 2023-03 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.2411 |
| 2023-04 | Kotak Liquid Fund - Regular - Growth | 120844 | 3492.1618 |
| 2023-04 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 684.2132 |
| 2023-04 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 567.0379 |
| 2023-04 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 360.0994 |
| 2023-04 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 359.2466 |
| 2023-04 | ABSL Liquid Fund - Regular - Growth | 101208 | 338.6475 |
| 2023-04 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 310.9974 |
| 2023-04 | Kotak Bluechip Fund - Regular - Growth | 120841 | 289.0393 |
| 2023-04 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 265.7603 |
| 2023-04 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 196.3889 |
| 2023-04 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 194.7713 |
| 2023-04 | Nippon India ETF Nifty 50 BeES | 118635 | 189.4213 |
| 2023-04 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 150.8106 |
| 2023-04 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 138.8261 |
| 2023-04 | DSP Small Cap Fund - Regular - Growth | 149324 | 132.7554 |
| 2023-04 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 132.5497 |
| 2023-04 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 130.4389 |
| 2023-04 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 128.0568 |
| 2023-04 | UTI Mid Cap Fund - Regular - Growth | 102886 | 127.3344 |
| 2023-04 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 118.0149 |
| 2023-04 | DSP Midcap Fund - Regular - Growth | 149323 | 110.2637 |
| 2023-04 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 105.1569 |
| 2023-04 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 92.7388 |
| 2023-04 | Axis Midcap Fund - Regular - Growth | 119094 | 85.8858 |
| 2023-04 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 81.4576 |
| 2023-04 | Axis Small Cap Fund - Regular - Growth | 119095 | 80.4303 |
| 2023-04 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 80.4175 |
| 2023-04 | Kotak Flexicap Fund - Regular - Growth | 120843 | 72.3295 |
| 2023-04 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 69.2187 |
| 2023-04 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 67.3629 |
| 2023-04 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 65.1873 |
| 2023-04 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 62.9627 |
| 2023-04 | ABSL Small Cap Fund - Regular - Growth | 101207 | 54.2032 |
| 2023-04 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 51.5809 |
| 2023-04 | Axis Bluechip Fund - Regular - Growth | 119092 | 47.7005 |
| 2023-04 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 47.1948 |
| 2023-04 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 45.0223 |
| 2023-04 | Axis Bluechip Fund - Direct - Growth | 119093 | 34.9314 |
| 2023-04 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.6274 |
| 2023-04 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.28 |
| 2023-05 | Kotak Liquid Fund - Regular - Growth | 120844 | 3513.073 |
| 2023-05 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 694.246 |
| 2023-05 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 565.4891 |
| 2023-05 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 364.095 |
| 2023-05 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 362.1376 |
| 2023-05 | ABSL Liquid Fund - Regular - Growth | 101208 | 340.4724 |
| 2023-05 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 312.8425 |
| 2023-05 | Kotak Bluechip Fund - Regular - Growth | 120841 | 295.7887 |
| 2023-05 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 252.7523 |
| 2023-05 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 198.3356 |
| 2023-05 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 194.7008 |
| 2023-05 | Nippon India ETF Nifty 50 BeES | 118635 | 187.9773 |
| 2023-05 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 154.3955 |
| 2023-05 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 147.1054 |
| 2023-05 | DSP Small Cap Fund - Regular - Growth | 149324 | 136.4708 |
| 2023-05 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 134.2685 |
| 2023-05 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 133.1763 |
| 2023-05 | UTI Mid Cap Fund - Regular - Growth | 102886 | 124.526 |
| 2023-05 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 118.1343 |
| 2023-05 | DSP Midcap Fund - Regular - Growth | 149323 | 117.6135 |
| 2023-05 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 111.4303 |
| 2023-05 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 106.9168 |
| 2023-05 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 94.4504 |
| 2023-05 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 88.4767 |
| 2023-05 | Axis Midcap Fund - Regular - Growth | 119094 | 83.5645 |
| 2023-05 | Axis Small Cap Fund - Regular - Growth | 119095 | 82.0805 |
| 2023-05 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 79.7675 |
| 2023-05 | Kotak Flexicap Fund - Regular - Growth | 120843 | 74.993 |
| 2023-05 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 66.1959 |
| 2023-05 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 66.1658 |
| 2023-05 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 65.7195 |
| 2023-05 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 60.7248 |
| 2023-05 | ABSL Small Cap Fund - Regular - Growth | 101207 | 59.4111 |
| 2023-05 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 51.8692 |
| 2023-05 | Axis Bluechip Fund - Regular - Growth | 119092 | 49.3689 |
| 2023-05 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 45.657 |
| 2023-05 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 45.5584 |
| 2023-05 | Axis Bluechip Fund - Direct - Growth | 119093 | 33.6343 |
| 2023-05 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.4854 |
| 2023-05 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.5239 |
| 2023-06 | Kotak Liquid Fund - Regular - Growth | 120844 | 3519.4161 |
| 2023-06 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 737.8829 |
| 2023-06 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 570.7095 |
| 2023-06 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 386.6193 |
| 2023-06 | ABSL Liquid Fund - Regular - Growth | 101208 | 342.3194 |
| 2023-06 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 339.0685 |
| 2023-06 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 315.0533 |
| 2023-06 | Kotak Bluechip Fund - Regular - Growth | 120841 | 304.375 |
| 2023-06 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 248.3817 |
| 2023-06 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 215.2728 |
| 2023-06 | Nippon India ETF Nifty 50 BeES | 118635 | 203.0525 |
| 2023-06 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 190.9883 |
| 2023-06 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 149.3755 |
| 2023-06 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 144.5859 |
| 2023-06 | DSP Small Cap Fund - Regular - Growth | 149324 | 141.5841 |
| 2023-06 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 140.7228 |
| 2023-06 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 131.9393 |
| 2023-06 | UTI Mid Cap Fund - Regular - Growth | 102886 | 128.2907 |
| 2023-06 | DSP Midcap Fund - Regular - Growth | 149323 | 126.7957 |
| 2023-06 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 112.0753 |
| 2023-06 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 107.7712 |
| 2023-06 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 102.4429 |
| 2023-06 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 97.2871 |
| 2023-06 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 91.4508 |
| 2023-06 | Axis Small Cap Fund - Regular - Growth | 119095 | 80.7505 |
| 2023-06 | Axis Midcap Fund - Regular - Growth | 119094 | 80.2767 |
| 2023-06 | Kotak Flexicap Fund - Regular - Growth | 120843 | 78.7903 |
| 2023-06 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 78.6815 |
| 2023-06 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 69.5883 |
| 2023-06 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 67.5639 |
| 2023-06 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 64.7208 |
| 2023-06 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 64.3532 |
| 2023-06 | ABSL Small Cap Fund - Regular - Growth | 101207 | 59.9523 |
| 2023-06 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 51.1678 |
| 2023-06 | Axis Bluechip Fund - Regular - Growth | 119092 | 49.2557 |
| 2023-06 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 48.3236 |
| 2023-06 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 45.7222 |
| 2023-06 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.8869 |
| 2023-06 | Axis Bluechip Fund - Direct - Growth | 119093 | 33.7558 |
| 2023-06 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.254 |
| 2023-07 | Kotak Liquid Fund - Regular - Growth | 120844 | 3539.9146 |
| 2023-07 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 728.9379 |
| 2023-07 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 578.383 |
| 2023-07 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 390.8744 |
| 2023-07 | ABSL Liquid Fund - Regular - Growth | 101208 | 344.2101 |
| 2023-07 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 336.3943 |
| 2023-07 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 317.3407 |
| 2023-07 | Kotak Bluechip Fund - Regular - Growth | 120841 | 306.4817 |
| 2023-07 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 239.6542 |
| 2023-07 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 211.7464 |
| 2023-07 | Nippon India ETF Nifty 50 BeES | 118635 | 210.2463 |
| 2023-07 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 188.2008 |
| 2023-07 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 160.2049 |
| 2023-07 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 143.7491 |
| 2023-07 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 140.5135 |
| 2023-07 | DSP Small Cap Fund - Regular - Growth | 149324 | 136.8259 |
| 2023-07 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 129.9983 |
| 2023-07 | DSP Midcap Fund - Regular - Growth | 149323 | 129.6655 |
| 2023-07 | UTI Mid Cap Fund - Regular - Growth | 102886 | 128.9392 |
| 2023-07 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 113.6179 |
| 2023-07 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 107.4782 |
| 2023-07 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 105.5808 |
| 2023-07 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 98.5201 |
| 2023-07 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 90.1543 |
| 2023-07 | Axis Midcap Fund - Regular - Growth | 119094 | 82.6122 |
| 2023-07 | Kotak Flexicap Fund - Regular - Growth | 120843 | 81.6638 |
| 2023-07 | Axis Small Cap Fund - Regular - Growth | 119095 | 77.8666 |
| 2023-07 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 76.9909 |
| 2023-07 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 73.8536 |
| 2023-07 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 70.9299 |
| 2023-07 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 68.4302 |
| 2023-07 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.3607 |
| 2023-07 | ABSL Small Cap Fund - Regular - Growth | 101207 | 60.8845 |
| 2023-07 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 54.9934 |
| 2023-07 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 52.384 |
| 2023-07 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.6077 |
| 2023-07 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 46.2673 |
| 2023-07 | Axis Bluechip Fund - Direct - Growth | 119093 | 34.2177 |
| 2023-07 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.4164 |
| 2023-07 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 27.6648 |
| 2023-08 | Kotak Liquid Fund - Regular - Growth | 120844 | 3565.8079 |
| 2023-08 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 702.6683 |
| 2023-08 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 569.7209 |
| 2023-08 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 395.6066 |
| 2023-08 | ABSL Liquid Fund - Regular - Growth | 101208 | 346.1332 |
| 2023-08 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 343.6398 |
| 2023-08 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 319.3345 |
| 2023-08 | Kotak Bluechip Fund - Regular - Growth | 120841 | 310.8003 |
| 2023-08 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 227.2313 |
| 2023-08 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 226.9988 |
| 2023-08 | Nippon India ETF Nifty 50 BeES | 118635 | 214.663 |
| 2023-08 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 189.3131 |
| 2023-08 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 184.4591 |
| 2023-08 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 142.8968 |
| 2023-08 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 141.8805 |
| 2023-08 | DSP Midcap Fund - Regular - Growth | 149323 | 137.1698 |
| 2023-08 | UTI Mid Cap Fund - Regular - Growth | 102886 | 132.3847 |
| 2023-08 | DSP Small Cap Fund - Regular - Growth | 149324 | 129.3415 |
| 2023-08 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 128.9796 |
| 2023-08 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 113.7844 |
| 2023-08 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 102.9725 |
| 2023-08 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 100.19 |
| 2023-08 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 95.4281 |
| 2023-08 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 88.8519 |
| 2023-08 | Axis Midcap Fund - Regular - Growth | 119094 | 87.0227 |
| 2023-08 | Axis Small Cap Fund - Regular - Growth | 119095 | 85.8194 |
| 2023-08 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 81.6809 |
| 2023-08 | Kotak Flexicap Fund - Regular - Growth | 120843 | 79.7674 |
| 2023-08 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 75.7958 |
| 2023-08 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 73.7764 |
| 2023-08 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 72.2795 |
| 2023-08 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.4514 |
| 2023-08 | ABSL Small Cap Fund - Regular - Growth | 101207 | 60.6729 |
| 2023-08 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 59.036 |
| 2023-08 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 53.5121 |
| 2023-08 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.5629 |
| 2023-08 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 46.6332 |
| 2023-08 | Axis Bluechip Fund - Direct - Growth | 119093 | 35.8786 |
| 2023-08 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.7163 |
| 2023-08 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.199 |
| 2023-09 | Kotak Liquid Fund - Regular - Growth | 120844 | 3583.8979 |
| 2023-09 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 745.6672 |
| 2023-09 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 577.0815 |
| 2023-09 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 382.4651 |
| 2023-09 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 356.9477 |
| 2023-09 | ABSL Liquid Fund - Regular - Growth | 101208 | 346.9055 |
| 2023-09 | Kotak Bluechip Fund - Regular - Growth | 120841 | 340.0807 |
| 2023-09 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 321.0279 |
| 2023-09 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 246.804 |
| 2023-09 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 230.8502 |
| 2023-09 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 212.4083 |
| 2023-09 | Nippon India ETF Nifty 50 BeES | 118635 | 211.3073 |
| 2023-09 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 179.7188 |
| 2023-09 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 150.5427 |
| 2023-09 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 148.1143 |
| 2023-09 | DSP Midcap Fund - Regular - Growth | 149323 | 137.9129 |
| 2023-09 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 133.8593 |
| 2023-09 | UTI Mid Cap Fund - Regular - Growth | 102886 | 131.2295 |
| 2023-09 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 117.8651 |
| 2023-09 | DSP Small Cap Fund - Regular - Growth | 149324 | 117.0547 |
| 2023-09 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 105.5074 |
| 2023-09 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 99.1951 |
| 2023-09 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 92.6843 |
| 2023-09 | Axis Small Cap Fund - Regular - Growth | 119095 | 91.9613 |
| 2023-09 | Axis Midcap Fund - Regular - Growth | 119094 | 91.5658 |
| 2023-09 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 86.3233 |
| 2023-09 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 86.0884 |
| 2023-09 | Kotak Flexicap Fund - Regular - Growth | 120843 | 81.8347 |
| 2023-09 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 80.3787 |
| 2023-09 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 73.9769 |
| 2023-09 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 73.7774 |
| 2023-09 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 72.8241 |
| 2023-09 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 58.784 |
| 2023-09 | ABSL Small Cap Fund - Regular - Growth | 101207 | 56.9123 |
| 2023-09 | Axis Bluechip Fund - Regular - Growth | 119092 | 52.2384 |
| 2023-09 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 50.6866 |
| 2023-09 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 47.583 |
| 2023-09 | Axis Bluechip Fund - Direct - Growth | 119093 | 38.5882 |
| 2023-09 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.5013 |
| 2023-09 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.5432 |
| 2023-10 | Kotak Liquid Fund - Regular - Growth | 120844 | 3609.2203 |
| 2023-10 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 767.2782 |
| 2023-10 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 575.1728 |
| 2023-10 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 379.4159 |
| 2023-10 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 366.0575 |
| 2023-10 | Kotak Bluechip Fund - Regular - Growth | 120841 | 364.851 |
| 2023-10 | ABSL Liquid Fund - Regular - Growth | 101208 | 348.6245 |
| 2023-10 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 322.763 |
| 2023-10 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 276.1812 |
| 2023-10 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 239.1225 |
| 2023-10 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 215.7551 |
| 2023-10 | Nippon India ETF Nifty 50 BeES | 118635 | 208.2839 |
| 2023-10 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 182.2415 |
| 2023-10 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 154.5081 |
| 2023-10 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 148.3811 |
| 2023-10 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 143.2282 |
| 2023-10 | DSP Midcap Fund - Regular - Growth | 149323 | 138.5029 |
| 2023-10 | UTI Mid Cap Fund - Regular - Growth | 102886 | 126.2286 |
| 2023-10 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 120.7745 |
| 2023-10 | DSP Small Cap Fund - Regular - Growth | 149324 | 112.8444 |
| 2023-10 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 110.5292 |
| 2023-10 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 103.6721 |
| 2023-10 | Axis Midcap Fund - Regular - Growth | 119094 | 99.9199 |
| 2023-10 | Axis Small Cap Fund - Regular - Growth | 119095 | 94.3315 |
| 2023-10 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 91.5888 |
| 2023-10 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 86.8783 |
| 2023-10 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 85.6077 |
| 2023-10 | Kotak Flexicap Fund - Regular - Growth | 120843 | 83.153 |
| 2023-10 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 77.0492 |
| 2023-10 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 75.765 |
| 2023-10 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 75.7593 |
| 2023-10 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 71.2205 |
| 2023-10 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 61.1726 |
| 2023-10 | ABSL Small Cap Fund - Regular - Growth | 101207 | 57.4946 |
| 2023-10 | Axis Bluechip Fund - Regular - Growth | 119092 | 53.5109 |
| 2023-10 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 47.7963 |
| 2023-10 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 47.3587 |
| 2023-10 | Axis Bluechip Fund - Direct - Growth | 119093 | 38.0376 |
| 2023-10 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.354 |
| 2023-10 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.6084 |
| 2023-11 | Kotak Liquid Fund - Regular - Growth | 120844 | 3632.9151 |
| 2023-11 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 804.2475 |
| 2023-11 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 572.5955 |
| 2023-11 | Kotak Bluechip Fund - Regular - Growth | 120841 | 395.9413 |
| 2023-11 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 377.3721 |
| 2023-11 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 364.3535 |
| 2023-11 | ABSL Liquid Fund - Regular - Growth | 101208 | 350.6391 |
| 2023-11 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 324.9365 |
| 2023-11 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 277.5348 |
| 2023-11 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 245.0117 |
| 2023-11 | Nippon India ETF Nifty 50 BeES | 118635 | 221.1639 |
| 2023-11 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 198.5728 |
| 2023-11 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 181.3333 |
| 2023-11 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 156.4889 |
| 2023-11 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 147.4172 |
| 2023-11 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 143.2025 |
| 2023-11 | DSP Midcap Fund - Regular - Growth | 149323 | 134.253 |
| 2023-11 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 124.3282 |
| 2023-11 | UTI Mid Cap Fund - Regular - Growth | 102886 | 121.2356 |
| 2023-11 | DSP Small Cap Fund - Regular - Growth | 149324 | 115.1507 |
| 2023-11 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 114.8704 |
| 2023-11 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 109.3251 |
| 2023-11 | Axis Midcap Fund - Regular - Growth | 119094 | 105.6881 |
| 2023-11 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 96.0442 |
| 2023-11 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 91.9895 |
| 2023-11 | Axis Small Cap Fund - Regular - Growth | 119095 | 90.3172 |
| 2023-11 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 86.1263 |
| 2023-11 | Kotak Flexicap Fund - Regular - Growth | 120843 | 85.7092 |
| 2023-11 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 78.2496 |
| 2023-11 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 76.5055 |
| 2023-11 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 74.3046 |
| 2023-11 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 72.9876 |
| 2023-11 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 59.4584 |
| 2023-11 | ABSL Small Cap Fund - Regular - Growth | 101207 | 56.5507 |
| 2023-11 | Axis Bluechip Fund - Regular - Growth | 119092 | 52.3471 |
| 2023-11 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 48.305 |
| 2023-11 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 46.5382 |
| 2023-11 | Axis Bluechip Fund - Direct - Growth | 119093 | 38.6733 |
| 2023-11 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.4424 |
| 2023-11 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.5247 |
| 2023-12 | Kotak Liquid Fund - Regular - Growth | 120844 | 3653.3905 |
| 2023-12 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 833.9235 |
| 2023-12 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 582.917 |
| 2023-12 | Kotak Bluechip Fund - Regular - Growth | 120841 | 409.3585 |
| 2023-12 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 384.3103 |
| 2023-12 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 383.2829 |
| 2023-12 | ABSL Liquid Fund - Regular - Growth | 101208 | 352.7617 |
| 2023-12 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 326.5759 |
| 2023-12 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 278.0219 |
| 2023-12 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 263.7248 |
| 2023-12 | Nippon India ETF Nifty 50 BeES | 118635 | 223.0673 |
| 2023-12 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 191.8341 |
| 2023-12 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 184.1165 |
| 2023-12 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 166.539 |
| 2023-12 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 144.7531 |
| 2023-12 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 141.3829 |
| 2023-12 | DSP Small Cap Fund - Regular - Growth | 149324 | 134.9052 |
| 2023-12 | DSP Midcap Fund - Regular - Growth | 149323 | 132.9172 |
| 2023-12 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 129.0125 |
| 2023-12 | UTI Mid Cap Fund - Regular - Growth | 102886 | 127.282 |
| 2023-12 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 114.0955 |
| 2023-12 | Axis Midcap Fund - Regular - Growth | 119094 | 104.5877 |
| 2023-12 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 102.7484 |
| 2023-12 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 98.8382 |
| 2023-12 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 96.5829 |
| 2023-12 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 87.95 |
| 2023-12 | Kotak Flexicap Fund - Regular - Growth | 120843 | 87.5177 |
| 2023-12 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 80.2421 |
| 2023-12 | Axis Small Cap Fund - Regular - Growth | 119095 | 78.9598 |
| 2023-12 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 74.0353 |
| 2023-12 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 72.123 |
| 2023-12 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.1811 |
| 2023-12 | ABSL Small Cap Fund - Regular - Growth | 101207 | 59.6065 |
| 2023-12 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 58.2032 |
| 2023-12 | Axis Bluechip Fund - Regular - Growth | 119092 | 52.4784 |
| 2023-12 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 49.0373 |
| 2023-12 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 48.5496 |
| 2023-12 | Axis Bluechip Fund - Direct - Growth | 119093 | 40.9998 |
| 2023-12 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.3871 |
| 2023-12 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.4012 |
| 2024-01 | Kotak Liquid Fund - Regular - Growth | 120844 | 3671.0298 |
| 2024-01 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 814.3903 |
| 2024-01 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 598.9849 |
| 2024-01 | Kotak Bluechip Fund - Regular - Growth | 120841 | 422.8967 |
| 2024-01 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 399.9971 |
| 2024-01 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 393.453 |
| 2024-01 | ABSL Liquid Fund - Regular - Growth | 101208 | 354.8359 |
| 2024-01 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 328.6248 |
| 2024-01 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 272.3582 |
| 2024-01 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 269.7795 |
| 2024-01 | Nippon India ETF Nifty 50 BeES | 118635 | 221.8804 |
| 2024-01 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 205.9509 |
| 2024-01 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 194.5646 |
| 2024-01 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 168.1116 |
| 2024-01 | DSP Small Cap Fund - Regular - Growth | 149324 | 150.0543 |
| 2024-01 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 141.5529 |
| 2024-01 | DSP Midcap Fund - Regular - Growth | 149323 | 139.5928 |
| 2024-01 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 135.1226 |
| 2024-01 | UTI Mid Cap Fund - Regular - Growth | 102886 | 131.2151 |
| 2024-01 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 130.2582 |
| 2024-01 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 127.4829 |
| 2024-01 | Axis Midcap Fund - Regular - Growth | 119094 | 104.3186 |
| 2024-01 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 101.812 |
| 2024-01 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 101.3585 |
| 2024-01 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 95.5798 |
| 2024-01 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 91.5995 |
| 2024-01 | Kotak Flexicap Fund - Regular - Growth | 120843 | 85.7306 |
| 2024-01 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 80.1568 |
| 2024-01 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 76.8241 |
| 2024-01 | Axis Small Cap Fund - Regular - Growth | 119095 | 73.7894 |
| 2024-01 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 68.299 |
| 2024-01 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 67.1598 |
| 2024-01 | ABSL Small Cap Fund - Regular - Growth | 101207 | 58.8467 |
| 2024-01 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 53.4305 |
| 2024-01 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.8068 |
| 2024-01 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 49.2949 |
| 2024-01 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 48.7116 |
| 2024-01 | Axis Bluechip Fund - Direct - Growth | 119093 | 42.0692 |
| 2024-01 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 31.9305 |
| 2024-01 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.6261 |
| 2024-02 | Kotak Liquid Fund - Regular - Growth | 120844 | 3689.7344 |
| 2024-02 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 828.245 |
| 2024-02 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 602.8951 |
| 2024-02 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 404.5951 |
| 2024-02 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 399.4777 |
| 2024-02 | Kotak Bluechip Fund - Regular - Growth | 120841 | 398.9666 |
| 2024-02 | ABSL Liquid Fund - Regular - Growth | 101208 | 356.1237 |
| 2024-02 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 330.9784 |
| 2024-02 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 281.0262 |
| 2024-02 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 273.4116 |
| 2024-02 | Nippon India ETF Nifty 50 BeES | 118635 | 218.2548 |
| 2024-02 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 212.8127 |
| 2024-02 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 210.9517 |
| 2024-02 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 171.0001 |
| 2024-02 | DSP Small Cap Fund - Regular - Growth | 149324 | 149.2812 |
| 2024-02 | DSP Midcap Fund - Regular - Growth | 149323 | 142.7909 |
| 2024-02 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 140.1206 |
| 2024-02 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 139.6274 |
| 2024-02 | UTI Mid Cap Fund - Regular - Growth | 102886 | 134.0758 |
| 2024-02 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 130.417 |
| 2024-02 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 119.6769 |
| 2024-02 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 106.0934 |
| 2024-02 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 101.9098 |
| 2024-02 | Axis Midcap Fund - Regular - Growth | 119094 | 101.4073 |
| 2024-02 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 101.2179 |
| 2024-02 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 93.6953 |
| 2024-02 | Kotak Flexicap Fund - Regular - Growth | 120843 | 85.1053 |
| 2024-02 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 80.8069 |
| 2024-02 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 78.8944 |
| 2024-02 | Axis Small Cap Fund - Regular - Growth | 119095 | 71.6118 |
| 2024-02 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 66.7861 |
| 2024-02 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 65.8457 |
| 2024-02 | ABSL Small Cap Fund - Regular - Growth | 101207 | 58.0863 |
| 2024-02 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 52.8127 |
| 2024-02 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.7087 |
| 2024-02 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 49.3747 |
| 2024-02 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 48.4906 |
| 2024-02 | Axis Bluechip Fund - Direct - Growth | 119093 | 42.9556 |
| 2024-02 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 31.5116 |
| 2024-02 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.5086 |
| 2024-03 | Kotak Liquid Fund - Regular - Growth | 120844 | 3712.4585 |
| 2024-03 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 812.1511 |
| 2024-03 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 635.0511 |
| 2024-03 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 421.6727 |
| 2024-03 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 421.038 |
| 2024-03 | Kotak Bluechip Fund - Regular - Growth | 120841 | 378.9413 |
| 2024-03 | ABSL Liquid Fund - Regular - Growth | 101208 | 358.5511 |
| 2024-03 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 332.7402 |
| 2024-03 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 295.7154 |
| 2024-03 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 283.4496 |
| 2024-03 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 228.6481 |
| 2024-03 | Nippon India ETF Nifty 50 BeES | 118635 | 220.6256 |
| 2024-03 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 200.0773 |
| 2024-03 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 176.378 |
| 2024-03 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 149.6436 |
| 2024-03 | UTI Mid Cap Fund - Regular - Growth | 102886 | 145.4636 |
| 2024-03 | DSP Small Cap Fund - Regular - Growth | 149324 | 142.7884 |
| 2024-03 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 134.4478 |
| 2024-03 | DSP Midcap Fund - Regular - Growth | 149323 | 133.9563 |
| 2024-03 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 130.4353 |
| 2024-03 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 112.2968 |
| 2024-03 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 110.7952 |
| 2024-03 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 110.2876 |
| 2024-03 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 106.6789 |
| 2024-03 | Axis Midcap Fund - Regular - Growth | 119094 | 104.253 |
| 2024-03 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 100.8144 |
| 2024-03 | Kotak Flexicap Fund - Regular - Growth | 120843 | 87.4978 |
| 2024-03 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 84.093 |
| 2024-03 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 77.5857 |
| 2024-03 | Axis Small Cap Fund - Regular - Growth | 119095 | 75.5503 |
| 2024-03 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 67.5201 |
| 2024-03 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.7222 |
| 2024-03 | ABSL Small Cap Fund - Regular - Growth | 101207 | 61.4654 |
| 2024-03 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 52.9501 |
| 2024-03 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.9949 |
| 2024-03 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 50.6553 |
| 2024-03 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 49.3987 |
| 2024-03 | Axis Bluechip Fund - Direct - Growth | 119093 | 44.6395 |
| 2024-03 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 31.8708 |
| 2024-03 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.1765 |
| 2024-04 | Kotak Liquid Fund - Regular - Growth | 120844 | 3734.8058 |
| 2024-04 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 818.4924 |
| 2024-04 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 640.1841 |
| 2024-04 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 409.8203 |
| 2024-04 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 403.2031 |
| 2024-04 | Kotak Bluechip Fund - Regular - Growth | 120841 | 385.358 |
| 2024-04 | ABSL Liquid Fund - Regular - Growth | 101208 | 360.2339 |
| 2024-04 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 334.5579 |
| 2024-04 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 303.7262 |
| 2024-04 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 289.1628 |
| 2024-04 | Nippon India ETF Nifty 50 BeES | 118635 | 225.0455 |
| 2024-04 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 222.9047 |
| 2024-04 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 181.8843 |
| 2024-04 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 178.3015 |
| 2024-04 | DSP Small Cap Fund - Regular - Growth | 149324 | 158.505 |
| 2024-04 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 151.2043 |
| 2024-04 | UTI Mid Cap Fund - Regular - Growth | 102886 | 144.7353 |
| 2024-04 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 135.5464 |
| 2024-04 | DSP Midcap Fund - Regular - Growth | 149323 | 129.8605 |
| 2024-04 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 127.9272 |
| 2024-04 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 118.4923 |
| 2024-04 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 117.8475 |
| 2024-04 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 113.6686 |
| 2024-04 | Axis Midcap Fund - Regular - Growth | 119094 | 111.0368 |
| 2024-04 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 108.8462 |
| 2024-04 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 103.0469 |
| 2024-04 | Kotak Flexicap Fund - Regular - Growth | 120843 | 93.7363 |
| 2024-04 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 87.961 |
| 2024-04 | Axis Small Cap Fund - Regular - Growth | 119095 | 76.5462 |
| 2024-04 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 76.0818 |
| 2024-04 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 69.2337 |
| 2024-04 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 62.6771 |
| 2024-04 | ABSL Small Cap Fund - Regular - Growth | 101207 | 60.0773 |
| 2024-04 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 55.7384 |
| 2024-04 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 54.4871 |
| 2024-04 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.449 |
| 2024-04 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 49.2451 |
| 2024-04 | Axis Bluechip Fund - Direct - Growth | 119093 | 45.5719 |
| 2024-04 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.0678 |
| 2024-04 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.1208 |
| 2024-05 | Kotak Liquid Fund - Regular - Growth | 120844 | 3739.4157 |
| 2024-05 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 815.3441 |
| 2024-05 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 634.4635 |
| 2024-05 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 436.2477 |
| 2024-05 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 416.5146 |
| 2024-05 | Kotak Bluechip Fund - Regular - Growth | 120841 | 392.5807 |
| 2024-05 | ABSL Liquid Fund - Regular - Growth | 101208 | 361.5898 |
| 2024-05 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 336.6219 |
| 2024-05 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 296.6547 |
| 2024-05 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 263.3881 |
| 2024-05 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 235.9683 |
| 2024-05 | Nippon India ETF Nifty 50 BeES | 118635 | 225.0339 |
| 2024-05 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 192.5977 |
| 2024-05 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 187.5467 |
| 2024-05 | DSP Small Cap Fund - Regular - Growth | 149324 | 167.282 |
| 2024-05 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 157.148 |
| 2024-05 | UTI Mid Cap Fund - Regular - Growth | 102886 | 141.2194 |
| 2024-05 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 136.7353 |
| 2024-05 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 129.1249 |
| 2024-05 | DSP Midcap Fund - Regular - Growth | 149323 | 125.4031 |
| 2024-05 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 120.4944 |
| 2024-05 | Axis Midcap Fund - Regular - Growth | 119094 | 117.6109 |
| 2024-05 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 117.414 |
| 2024-05 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 115.3437 |
| 2024-05 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 115.0173 |
| 2024-05 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 106.4749 |
| 2024-05 | Kotak Flexicap Fund - Regular - Growth | 120843 | 91.9803 |
| 2024-05 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 90.6673 |
| 2024-05 | Axis Small Cap Fund - Regular - Growth | 119095 | 75.2453 |
| 2024-05 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 73.6776 |
| 2024-05 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 72.8752 |
| 2024-05 | ABSL Small Cap Fund - Regular - Growth | 101207 | 67.1393 |
| 2024-05 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.4091 |
| 2024-05 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 55.8649 |
| 2024-05 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 55.2909 |
| 2024-05 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 49.8077 |
| 2024-05 | Axis Bluechip Fund - Regular - Growth | 119092 | 49.7615 |
| 2024-05 | Axis Bluechip Fund - Direct - Growth | 119093 | 45.7445 |
| 2024-05 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.2071 |
| 2024-05 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.1316 |
| 2024-06 | Kotak Liquid Fund - Regular - Growth | 120844 | 3759.2261 |
| 2024-06 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 798.8378 |
| 2024-06 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 654.603 |
| 2024-06 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 445.7332 |
| 2024-06 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 420.8144 |
| 2024-06 | Kotak Bluechip Fund - Regular - Growth | 120841 | 396.766 |
| 2024-06 | ABSL Liquid Fund - Regular - Growth | 101208 | 363.6386 |
| 2024-06 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 338.0433 |
| 2024-06 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 299.4591 |
| 2024-06 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 257.8977 |
| 2024-06 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 237.9889 |
| 2024-06 | Nippon India ETF Nifty 50 BeES | 118635 | 222.6249 |
| 2024-06 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 211.0274 |
| 2024-06 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 201.2718 |
| 2024-06 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 163.3882 |
| 2024-06 | DSP Small Cap Fund - Regular - Growth | 149324 | 163.294 |
| 2024-06 | UTI Mid Cap Fund - Regular - Growth | 102886 | 141.9577 |
| 2024-06 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 131.729 |
| 2024-06 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 127.548 |
| 2024-06 | DSP Midcap Fund - Regular - Growth | 149323 | 125.7195 |
| 2024-06 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 120.6706 |
| 2024-06 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 119.0473 |
| 2024-06 | Axis Midcap Fund - Regular - Growth | 119094 | 117.2052 |
| 2024-06 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 116.5108 |
| 2024-06 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 113.1221 |
| 2024-06 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 108.8165 |
| 2024-06 | Kotak Flexicap Fund - Regular - Growth | 120843 | 97.8299 |
| 2024-06 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 94.3666 |
| 2024-06 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 73.6868 |
| 2024-06 | Axis Small Cap Fund - Regular - Growth | 119095 | 70.9264 |
| 2024-06 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 70.587 |
| 2024-06 | ABSL Small Cap Fund - Regular - Growth | 101207 | 65.8938 |
| 2024-06 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 64.7439 |
| 2024-06 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 58.1004 |
| 2024-06 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 53.9343 |
| 2024-06 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 50.8264 |
| 2024-06 | Axis Bluechip Fund - Regular - Growth | 119092 | 49.5245 |
| 2024-06 | Axis Bluechip Fund - Direct - Growth | 119093 | 47.8085 |
| 2024-06 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 31.8383 |
| 2024-06 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.5235 |
| 2024-07 | Kotak Liquid Fund - Regular - Growth | 120844 | 3780.6658 |
| 2024-07 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 821.5599 |
| 2024-07 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 645.1311 |
| 2024-07 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 467.3024 |
| 2024-07 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 432.8195 |
| 2024-07 | Kotak Bluechip Fund - Regular - Growth | 120841 | 406.5952 |
| 2024-07 | ABSL Liquid Fund - Regular - Growth | 101208 | 365.4083 |
| 2024-07 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 340.383 |
| 2024-07 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 308.3885 |
| 2024-07 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 264.1773 |
| 2024-07 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 246.0208 |
| 2024-07 | Nippon India ETF Nifty 50 BeES | 118635 | 226.8103 |
| 2024-07 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 216.5939 |
| 2024-07 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 210.1882 |
| 2024-07 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 168.1422 |
| 2024-07 | DSP Small Cap Fund - Regular - Growth | 149324 | 157.0793 |
| 2024-07 | UTI Mid Cap Fund - Regular - Growth | 102886 | 145.159 |
| 2024-07 | DSP Midcap Fund - Regular - Growth | 149323 | 133.4923 |
| 2024-07 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 133.2069 |
| 2024-07 | Axis Midcap Fund - Regular - Growth | 119094 | 125.3481 |
| 2024-07 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 124.5419 |
| 2024-07 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 123.3328 |
| 2024-07 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 118.2246 |
| 2024-07 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 117.2534 |
| 2024-07 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 113.0973 |
| 2024-07 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 111.0935 |
| 2024-07 | Kotak Flexicap Fund - Regular - Growth | 120843 | 96.7357 |
| 2024-07 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 95.1524 |
| 2024-07 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 73.7028 |
| 2024-07 | Axis Small Cap Fund - Regular - Growth | 119095 | 73.1109 |
| 2024-07 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 68.7875 |
| 2024-07 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 64.989 |
| 2024-07 | ABSL Small Cap Fund - Regular - Growth | 101207 | 62.8803 |
| 2024-07 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 61.8616 |
| 2024-07 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 56.7054 |
| 2024-07 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 50.7572 |
| 2024-07 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.4606 |
| 2024-07 | Axis Bluechip Fund - Direct - Growth | 119093 | 45.9378 |
| 2024-07 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.0447 |
| 2024-07 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 28.8833 |
| 2024-08 | Kotak Liquid Fund - Regular - Growth | 120844 | 3796.8573 |
| 2024-08 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 792.4631 |
| 2024-08 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 631.4043 |
| 2024-08 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 489.1792 |
| 2024-08 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 421.5506 |
| 2024-08 | Kotak Bluechip Fund - Regular - Growth | 120841 | 396.5241 |
| 2024-08 | ABSL Liquid Fund - Regular - Growth | 101208 | 366.5901 |
| 2024-08 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 342.052 |
| 2024-08 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 298.2627 |
| 2024-08 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 275.2373 |
| 2024-08 | Nippon India ETF Nifty 50 BeES | 118635 | 243.0912 |
| 2024-08 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 232.1253 |
| 2024-08 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 226.7214 |
| 2024-08 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 214.2356 |
| 2024-08 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 173.3692 |
| 2024-08 | DSP Midcap Fund - Regular - Growth | 149323 | 151.601 |
| 2024-08 | UTI Mid Cap Fund - Regular - Growth | 102886 | 149.4799 |
| 2024-08 | DSP Small Cap Fund - Regular - Growth | 149324 | 140.918 |
| 2024-08 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 137.7049 |
| 2024-08 | Axis Midcap Fund - Regular - Growth | 119094 | 133.0091 |
| 2024-08 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 127.477 |
| 2024-08 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 125.2662 |
| 2024-08 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 123.3471 |
| 2024-08 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 119.2477 |
| 2024-08 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 114.665 |
| 2024-08 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 111.1259 |
| 2024-08 | Kotak Flexicap Fund - Regular - Growth | 120843 | 94.32 |
| 2024-08 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 92.7937 |
| 2024-08 | Axis Small Cap Fund - Regular - Growth | 119095 | 73.3218 |
| 2024-08 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 72.6418 |
| 2024-08 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 69.9839 |
| 2024-08 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 62.4376 |
| 2024-08 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 62.1251 |
| 2024-08 | ABSL Small Cap Fund - Regular - Growth | 101207 | 60.4545 |
| 2024-08 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 59.225 |
| 2024-08 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.4342 |
| 2024-08 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.2716 |
| 2024-08 | Axis Bluechip Fund - Direct - Growth | 119093 | 45.8986 |
| 2024-08 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 32.6807 |
| 2024-08 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.0247 |
| 2024-09 | Kotak Liquid Fund - Regular - Growth | 120844 | 3810.2931 |
| 2024-09 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 775.3309 |
| 2024-09 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 582.9321 |
| 2024-09 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 468.0176 |
| 2024-09 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 435.0419 |
| 2024-09 | Kotak Bluechip Fund - Regular - Growth | 120841 | 415.0703 |
| 2024-09 | ABSL Liquid Fund - Regular - Growth | 101208 | 368.1963 |
| 2024-09 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 344.3942 |
| 2024-09 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 302.4584 |
| 2024-09 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 270.9786 |
| 2024-09 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 257.3816 |
| 2024-09 | Nippon India ETF Nifty 50 BeES | 118635 | 247.1509 |
| 2024-09 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 232.2311 |
| 2024-09 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 215.1316 |
| 2024-09 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 171.3516 |
| 2024-09 | DSP Midcap Fund - Regular - Growth | 149323 | 168.329 |
| 2024-09 | UTI Mid Cap Fund - Regular - Growth | 102886 | 161.0639 |
| 2024-09 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 145.3641 |
| 2024-09 | DSP Small Cap Fund - Regular - Growth | 149324 | 141.2429 |
| 2024-09 | Axis Midcap Fund - Regular - Growth | 119094 | 134.259 |
| 2024-09 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 130.6431 |
| 2024-09 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 126.9933 |
| 2024-09 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 126.9625 |
| 2024-09 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 112.911 |
| 2024-09 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 112.9019 |
| 2024-09 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 111.319 |
| 2024-09 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 96.3206 |
| 2024-09 | Kotak Flexicap Fund - Regular - Growth | 120843 | 95.4429 |
| 2024-09 | Axis Small Cap Fund - Regular - Growth | 119095 | 74.6744 |
| 2024-09 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 73.0163 |
| 2024-09 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 72.9117 |
| 2024-09 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 65.6068 |
| 2024-09 | ABSL Small Cap Fund - Regular - Growth | 101207 | 64.8549 |
| 2024-09 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 61.7408 |
| 2024-09 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 58.607 |
| 2024-09 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 52.2247 |
| 2024-09 | Axis Bluechip Fund - Regular - Growth | 119092 | 49.5088 |
| 2024-09 | Axis Bluechip Fund - Direct - Growth | 119093 | 47.5169 |
| 2024-09 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.032 |
| 2024-09 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.2462 |
| 2024-10 | Kotak Liquid Fund - Regular - Growth | 120844 | 3825.9054 |
| 2024-10 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 763.115 |
| 2024-10 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 550.3791 |
| 2024-10 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 478.651 |
| 2024-10 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 426.4889 |
| 2024-10 | Kotak Bluechip Fund - Regular - Growth | 120841 | 414.9658 |
| 2024-10 | ABSL Liquid Fund - Regular - Growth | 101208 | 370.1052 |
| 2024-10 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 346.3287 |
| 2024-10 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 326.2333 |
| 2024-10 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 270.1275 |
| 2024-10 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 254.3347 |
| 2024-10 | Nippon India ETF Nifty 50 BeES | 118635 | 248.4032 |
| 2024-10 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 246.8395 |
| 2024-10 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 195.1664 |
| 2024-10 | DSP Midcap Fund - Regular - Growth | 149323 | 186.3982 |
| 2024-10 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 176.9747 |
| 2024-10 | UTI Mid Cap Fund - Regular - Growth | 102886 | 155.2044 |
| 2024-10 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 154.3545 |
| 2024-10 | Axis Midcap Fund - Regular - Growth | 119094 | 138.5876 |
| 2024-10 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 132.3941 |
| 2024-10 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 132.3417 |
| 2024-10 | DSP Small Cap Fund - Regular - Growth | 149324 | 131.9666 |
| 2024-10 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 123.434 |
| 2024-10 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 115.2875 |
| 2024-10 | Kotak Flexicap Fund - Regular - Growth | 120843 | 111.5357 |
| 2024-10 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 109.18 |
| 2024-10 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 108.8838 |
| 2024-10 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 99.0025 |
| 2024-10 | Axis Small Cap Fund - Regular - Growth | 119095 | 78.5021 |
| 2024-10 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 72.9762 |
| 2024-10 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 72.5559 |
| 2024-10 | ABSL Small Cap Fund - Regular - Growth | 101207 | 71.1481 |
| 2024-10 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.7618 |
| 2024-10 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 60.0366 |
| 2024-10 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 58.394 |
| 2024-10 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 52.1228 |
| 2024-10 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.7253 |
| 2024-10 | Axis Bluechip Fund - Direct - Growth | 119093 | 48.5079 |
| 2024-10 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.6878 |
| 2024-10 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.2784 |
| 2024-11 | Kotak Liquid Fund - Regular - Growth | 120844 | 3842.4538 |
| 2024-11 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 765.6449 |
| 2024-11 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 564.3039 |
| 2024-11 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 464.9219 |
| 2024-11 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 449.2139 |
| 2024-11 | Kotak Bluechip Fund - Regular - Growth | 120841 | 408.5562 |
| 2024-11 | ABSL Liquid Fund - Regular - Growth | 101208 | 372.0352 |
| 2024-11 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 348.4373 |
| 2024-11 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 332.7993 |
| 2024-11 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 270.7472 |
| 2024-11 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 264.3497 |
| 2024-11 | Nippon India ETF Nifty 50 BeES | 118635 | 255.4211 |
| 2024-11 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 241.8168 |
| 2024-11 | DSP Midcap Fund - Regular - Growth | 149323 | 193.2001 |
| 2024-11 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 187.1101 |
| 2024-11 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 176.7226 |
| 2024-11 | Axis Midcap Fund - Regular - Growth | 119094 | 159.0988 |
| 2024-11 | UTI Mid Cap Fund - Regular - Growth | 102886 | 157.4966 |
| 2024-11 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 153.526 |
| 2024-11 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 147.4748 |
| 2024-11 | Kotak Flexicap Fund - Regular - Growth | 120843 | 130.3638 |
| 2024-11 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 129.6381 |
| 2024-11 | DSP Small Cap Fund - Regular - Growth | 149324 | 127.3216 |
| 2024-11 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 116.5087 |
| 2024-11 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 115.3405 |
| 2024-11 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 112.3513 |
| 2024-11 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 109.5174 |
| 2024-11 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 105.1656 |
| 2024-11 | Axis Small Cap Fund - Regular - Growth | 119095 | 81.0483 |
| 2024-11 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 77.8543 |
| 2024-11 | ABSL Small Cap Fund - Regular - Growth | 101207 | 77.3559 |
| 2024-11 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 71.4867 |
| 2024-11 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 67.1499 |
| 2024-11 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 61.0593 |
| 2024-11 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 59.2215 |
| 2024-11 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.6883 |
| 2024-11 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.0767 |
| 2024-11 | Axis Bluechip Fund - Direct - Growth | 119093 | 48.1009 |
| 2024-11 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.6701 |
| 2024-11 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.4564 |
| 2024-12 | Kotak Liquid Fund - Regular - Growth | 120844 | 3865.4438 |
| 2024-12 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 766.2884 |
| 2024-12 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 587.6417 |
| 2024-12 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 457.6952 |
| 2024-12 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 450.532 |
| 2024-12 | Kotak Bluechip Fund - Regular - Growth | 120841 | 397.0341 |
| 2024-12 | ABSL Liquid Fund - Regular - Growth | 101208 | 373.8166 |
| 2024-12 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 350.6577 |
| 2024-12 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 318.5464 |
| 2024-12 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 266.8319 |
| 2024-12 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 266.2784 |
| 2024-12 | Nippon India ETF Nifty 50 BeES | 118635 | 247.8572 |
| 2024-12 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 247.7606 |
| 2024-12 | DSP Midcap Fund - Regular - Growth | 149323 | 201.5031 |
| 2024-12 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 188.7352 |
| 2024-12 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 171.4934 |
| 2024-12 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 160.006 |
| 2024-12 | UTI Mid Cap Fund - Regular - Growth | 102886 | 159.7557 |
| 2024-12 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 156.6632 |
| 2024-12 | Axis Midcap Fund - Regular - Growth | 119094 | 150.8965 |
| 2024-12 | Kotak Flexicap Fund - Regular - Growth | 120843 | 131.4558 |
| 2024-12 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 130.544 |
| 2024-12 | DSP Small Cap Fund - Regular - Growth | 149324 | 128.5695 |
| 2024-12 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 117.239 |
| 2024-12 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 110.7142 |
| 2024-12 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 107.5121 |
| 2024-12 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 104.3847 |
| 2024-12 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 100.9883 |
| 2024-12 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 79.0401 |
| 2024-12 | Axis Small Cap Fund - Regular - Growth | 119095 | 75.2753 |
| 2024-12 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 74.4956 |
| 2024-12 | ABSL Small Cap Fund - Regular - Growth | 101207 | 71.8948 |
| 2024-12 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 63.9006 |
| 2024-12 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 59.1074 |
| 2024-12 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 57.4828 |
| 2024-12 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.2588 |
| 2024-12 | Axis Bluechip Fund - Regular - Growth | 119092 | 48.4574 |
| 2024-12 | Axis Bluechip Fund - Direct - Growth | 119093 | 47.3882 |
| 2024-12 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.6865 |
| 2024-12 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.5637 |
| 2025-01 | Kotak Liquid Fund - Regular - Growth | 120844 | 3888.7252 |
| 2025-01 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 762.0803 |
| 2025-01 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 589.5285 |
| 2025-01 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 474.2668 |
| 2025-01 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 461.8724 |
| 2025-01 | Kotak Bluechip Fund - Regular - Growth | 120841 | 387.2361 |
| 2025-01 | ABSL Liquid Fund - Regular - Growth | 101208 | 375.4897 |
| 2025-01 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 352.4864 |
| 2025-01 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 290.8228 |
| 2025-01 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 288.5225 |
| 2025-01 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 260.7683 |
| 2025-01 | Nippon India ETF Nifty 50 BeES | 118635 | 249.6788 |
| 2025-01 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 248.944 |
| 2025-01 | DSP Midcap Fund - Regular - Growth | 149323 | 218.3093 |
| 2025-01 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 198.5907 |
| 2025-01 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 169.2332 |
| 2025-01 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 166.9759 |
| 2025-01 | UTI Mid Cap Fund - Regular - Growth | 102886 | 164.5118 |
| 2025-01 | Axis Midcap Fund - Regular - Growth | 119094 | 154.6693 |
| 2025-01 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 151.2294 |
| 2025-01 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 141.2106 |
| 2025-01 | DSP Small Cap Fund - Regular - Growth | 149324 | 133.7441 |
| 2025-01 | Kotak Flexicap Fund - Regular - Growth | 120843 | 130.9566 |
| 2025-01 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 119.5581 |
| 2025-01 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 112.7425 |
| 2025-01 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 109.4888 |
| 2025-01 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 105.9685 |
| 2025-01 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 103.3752 |
| 2025-01 | Axis Small Cap Fund - Regular - Growth | 119095 | 78.8971 |
| 2025-01 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 77.3875 |
| 2025-01 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 76.904 |
| 2025-01 | ABSL Small Cap Fund - Regular - Growth | 101207 | 72.031 |
| 2025-01 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 70.4526 |
| 2025-01 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 62.2575 |
| 2025-01 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 58.0102 |
| 2025-01 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.0947 |
| 2025-01 | Axis Bluechip Fund - Regular - Growth | 119092 | 48.9126 |
| 2025-01 | Axis Bluechip Fund - Direct - Growth | 119093 | 45.4268 |
| 2025-01 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.5162 |
| 2025-01 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.6977 |
| 2025-02 | Kotak Liquid Fund - Regular - Growth | 120844 | 3902.5996 |
| 2025-02 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 784.3465 |
| 2025-02 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 601.0527 |
| 2025-02 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 493.5082 |
| 2025-02 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 456.2907 |
| 2025-02 | ABSL Liquid Fund - Regular - Growth | 101208 | 377.1438 |
| 2025-02 | Kotak Bluechip Fund - Regular - Growth | 120841 | 369.6549 |
| 2025-02 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 355.0943 |
| 2025-02 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 310.7234 |
| 2025-02 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 295.407 |
| 2025-02 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 276.5058 |
| 2025-02 | Nippon India ETF Nifty 50 BeES | 118635 | 258.8199 |
| 2025-02 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 233.5667 |
| 2025-02 | DSP Midcap Fund - Regular - Growth | 149323 | 211.2959 |
| 2025-02 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 204.2184 |
| 2025-02 | Axis Midcap Fund - Regular - Growth | 119094 | 170.0211 |
| 2025-02 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 168.2362 |
| 2025-02 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 164.2545 |
| 2025-02 | UTI Mid Cap Fund - Regular - Growth | 102886 | 156.89 |
| 2025-02 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 153.5505 |
| 2025-02 | DSP Small Cap Fund - Regular - Growth | 149324 | 143.6677 |
| 2025-02 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 141.4505 |
| 2025-02 | Kotak Flexicap Fund - Regular - Growth | 120843 | 134.7962 |
| 2025-02 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 124.2835 |
| 2025-02 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 116.0703 |
| 2025-02 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 115.9698 |
| 2025-02 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 112.7814 |
| 2025-02 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 108.6612 |
| 2025-02 | Axis Small Cap Fund - Regular - Growth | 119095 | 79.4336 |
| 2025-02 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 78.7748 |
| 2025-02 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 78.6389 |
| 2025-02 | ABSL Small Cap Fund - Regular - Growth | 101207 | 77.0485 |
| 2025-02 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 68.4635 |
| 2025-02 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 65.994 |
| 2025-02 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 62.06 |
| 2025-02 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 50.733 |
| 2025-02 | Axis Bluechip Fund - Regular - Growth | 119092 | 48.3892 |
| 2025-02 | Axis Bluechip Fund - Direct - Growth | 119093 | 45.8292 |
| 2025-02 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.1098 |
| 2025-02 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 29.829 |
| 2025-03 | Kotak Liquid Fund - Regular - Growth | 120844 | 3927.8225 |
| 2025-03 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 801.7213 |
| 2025-03 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 619.4219 |
| 2025-03 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 494.4301 |
| 2025-03 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 485.5879 |
| 2025-03 | Kotak Bluechip Fund - Regular - Growth | 120841 | 390.2018 |
| 2025-03 | ABSL Liquid Fund - Regular - Growth | 101208 | 378.7771 |
| 2025-03 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 357.2696 |
| 2025-03 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 338.8452 |
| 2025-03 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 306.7626 |
| 2025-03 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 275.3549 |
| 2025-03 | Nippon India ETF Nifty 50 BeES | 118635 | 262.298 |
| 2025-03 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 224.4081 |
| 2025-03 | DSP Midcap Fund - Regular - Growth | 149323 | 204.558 |
| 2025-03 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 204.0025 |
| 2025-03 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 177.1369 |
| 2025-03 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 169.9071 |
| 2025-03 | Axis Midcap Fund - Regular - Growth | 119094 | 165.0333 |
| 2025-03 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 164.7949 |
| 2025-03 | DSP Small Cap Fund - Regular - Growth | 149324 | 151.41 |
| 2025-03 | UTI Mid Cap Fund - Regular - Growth | 102886 | 150.3796 |
| 2025-03 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 146.3417 |
| 2025-03 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 128.2341 |
| 2025-03 | Kotak Flexicap Fund - Regular - Growth | 120843 | 128.1138 |
| 2025-03 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 118.0338 |
| 2025-03 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 116.4631 |
| 2025-03 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 111.7758 |
| 2025-03 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 102.9555 |
| 2025-03 | Axis Small Cap Fund - Regular - Growth | 119095 | 90.4368 |
| 2025-03 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 81.9144 |
| 2025-03 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 79.0729 |
| 2025-03 | ABSL Small Cap Fund - Regular - Growth | 101207 | 74.4197 |
| 2025-03 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 71.4438 |
| 2025-03 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 68.0345 |
| 2025-03 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 65.8887 |
| 2025-03 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 50.4472 |
| 2025-03 | Axis Bluechip Fund - Direct - Growth | 119093 | 49.767 |
| 2025-03 | Axis Bluechip Fund - Regular - Growth | 119092 | 48.3251 |
| 2025-03 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.4917 |
| 2025-03 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 30.0277 |
| 2025-04 | Kotak Liquid Fund - Regular - Growth | 120844 | 3950.1137 |
| 2025-04 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 854.5394 |
| 2025-04 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 611.9275 |
| 2025-04 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 519.0136 |
| 2025-04 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 492.1419 |
| 2025-04 | Kotak Bluechip Fund - Regular - Growth | 120841 | 401.6535 |
| 2025-04 | ABSL Liquid Fund - Regular - Growth | 101208 | 379.8631 |
| 2025-04 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 359.47 |
| 2025-04 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 344.0483 |
| 2025-04 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 311.6962 |
| 2025-04 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 265.2821 |
| 2025-04 | Nippon India ETF Nifty 50 BeES | 118635 | 263.8041 |
| 2025-04 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 223.691 |
| 2025-04 | DSP Midcap Fund - Regular - Growth | 149323 | 195.1345 |
| 2025-04 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 186.0048 |
| 2025-04 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 182.2514 |
| 2025-04 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 180.9759 |
| 2025-04 | DSP Small Cap Fund - Regular - Growth | 149324 | 164.1492 |
| 2025-04 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 162.6658 |
| 2025-04 | Axis Midcap Fund - Regular - Growth | 119094 | 157.9097 |
| 2025-04 | UTI Mid Cap Fund - Regular - Growth | 102886 | 157.8604 |
| 2025-04 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 153.8413 |
| 2025-04 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 129.4001 |
| 2025-04 | Kotak Flexicap Fund - Regular - Growth | 120843 | 125.2801 |
| 2025-04 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 123.4647 |
| 2025-04 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 122.1725 |
| 2025-04 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 108.5277 |
| 2025-04 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 94.6978 |
| 2025-04 | Axis Small Cap Fund - Regular - Growth | 119095 | 94.2404 |
| 2025-04 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 84.2085 |
| 2025-04 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 79.2676 |
| 2025-04 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 74.4591 |
| 2025-04 | ABSL Small Cap Fund - Regular - Growth | 101207 | 71.5333 |
| 2025-04 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 70.175 |
| 2025-04 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 70.1372 |
| 2025-04 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 50.5416 |
| 2025-04 | Axis Bluechip Fund - Direct - Growth | 119093 | 48.2386 |
| 2025-04 | Axis Bluechip Fund - Regular - Growth | 119092 | 47.6311 |
| 2025-04 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 33.9203 |
| 2025-04 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 30.2213 |
| 2025-05 | Kotak Liquid Fund - Regular - Growth | 120844 | 3972.89 |
| 2025-05 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 916.9949 |
| 2025-05 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 614.5298 |
| 2025-05 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 519.3614 |
| 2025-05 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 512.2594 |
| 2025-05 | Kotak Bluechip Fund - Regular - Growth | 120841 | 414.3499 |
| 2025-05 | ABSL Liquid Fund - Regular - Growth | 101208 | 381.6565 |
| 2025-05 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 361.0402 |
| 2025-05 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 356.9191 |
| 2025-05 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 329.159 |
| 2025-05 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 275.228 |
| 2025-05 | Nippon India ETF Nifty 50 BeES | 118635 | 259.0594 |
| 2025-05 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 221.2971 |
| 2025-05 | DSP Midcap Fund - Regular - Growth | 149323 | 198.3161 |
| 2025-05 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 189.7431 |
| 2025-05 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 181.8323 |
| 2025-05 | DSP Small Cap Fund - Regular - Growth | 149324 | 169.2978 |
| 2025-05 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 167.2471 |
| 2025-05 | Axis Midcap Fund - Regular - Growth | 119094 | 163.9019 |
| 2025-05 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 162.5337 |
| 2025-05 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 155.5257 |
| 2025-05 | UTI Mid Cap Fund - Regular - Growth | 102886 | 154.2901 |
| 2025-05 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 128.7496 |
| 2025-05 | Kotak Flexicap Fund - Regular - Growth | 120843 | 127.4659 |
| 2025-05 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 125.3855 |
| 2025-05 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 120.0677 |
| 2025-05 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 110.2971 |
| 2025-05 | Axis Small Cap Fund - Regular - Growth | 119095 | 102.83 |
| 2025-05 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 94.4866 |
| 2025-05 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 88.8723 |
| 2025-05 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 81.4768 |
| 2025-05 | ABSL Small Cap Fund - Regular - Growth | 101207 | 73.5543 |
| 2025-05 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 70.7721 |
| 2025-05 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 70.6346 |
| 2025-05 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 69.3566 |
| 2025-05 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.0823 |
| 2025-05 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.0844 |
| 2025-05 | Axis Bluechip Fund - Direct - Growth | 119093 | 47.9401 |
| 2025-05 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.1568 |
| 2025-05 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 30.7195 |
| 2025-06 | Kotak Liquid Fund - Regular - Growth | 120844 | 3994.87 |
| 2025-06 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 920.3961 |
| 2025-06 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 602.9657 |
| 2025-06 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 528.3005 |
| 2025-06 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 509.5202 |
| 2025-06 | Kotak Bluechip Fund - Regular - Growth | 120841 | 406.358 |
| 2025-06 | ABSL Liquid Fund - Regular - Growth | 101208 | 383.764 |
| 2025-06 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 363.9987 |
| 2025-06 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 363.177 |
| 2025-06 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 344.0428 |
| 2025-06 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 302.7313 |
| 2025-06 | Nippon India ETF Nifty 50 BeES | 118635 | 265.6117 |
| 2025-06 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 229.3805 |
| 2025-06 | DSP Midcap Fund - Regular - Growth | 149323 | 203.4757 |
| 2025-06 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 200.4599 |
| 2025-06 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 189.169 |
| 2025-06 | DSP Small Cap Fund - Regular - Growth | 149324 | 174.296 |
| 2025-06 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 173.2531 |
| 2025-06 | Axis Midcap Fund - Regular - Growth | 119094 | 162.5486 |
| 2025-06 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 159.6864 |
| 2025-06 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 159.0258 |
| 2025-06 | UTI Mid Cap Fund - Regular - Growth | 102886 | 149.1946 |
| 2025-06 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 134.2831 |
| 2025-06 | Kotak Flexicap Fund - Regular - Growth | 120843 | 126.6784 |
| 2025-06 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 126.4635 |
| 2025-06 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 112.536 |
| 2025-06 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 112.2872 |
| 2025-06 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 99.6928 |
| 2025-06 | Axis Small Cap Fund - Regular - Growth | 119095 | 97.2784 |
| 2025-06 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 93.0492 |
| 2025-06 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 89.3215 |
| 2025-06 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 72.5956 |
| 2025-06 | ABSL Small Cap Fund - Regular - Growth | 101207 | 71.0492 |
| 2025-06 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.0463 |
| 2025-06 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 67.7899 |
| 2025-06 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.4754 |
| 2025-06 | Axis Bluechip Fund - Direct - Growth | 119093 | 49.8289 |
| 2025-06 | Axis Bluechip Fund - Regular - Growth | 119092 | 49.798 |
| 2025-06 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.2219 |
| 2025-06 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.0285 |
| 2025-07 | Kotak Liquid Fund - Regular - Growth | 120844 | 4014.6236 |
| 2025-07 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 923.9481 |
| 2025-07 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 602.3459 |
| 2025-07 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 535.5557 |
| 2025-07 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 513.597 |
| 2025-07 | Kotak Bluechip Fund - Regular - Growth | 120841 | 385.5501 |
| 2025-07 | ABSL Liquid Fund - Regular - Growth | 101208 | 385.5496 |
| 2025-07 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 375.7084 |
| 2025-07 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 365.4743 |
| 2025-07 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 358.062 |
| 2025-07 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 317.6118 |
| 2025-07 | Nippon India ETF Nifty 50 BeES | 118635 | 282.7543 |
| 2025-07 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 236.1366 |
| 2025-07 | DSP Midcap Fund - Regular - Growth | 149323 | 213.5369 |
| 2025-07 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 208.647 |
| 2025-07 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 190.9309 |
| 2025-07 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 189.3536 |
| 2025-07 | DSP Small Cap Fund - Regular - Growth | 149324 | 170.9927 |
| 2025-07 | Axis Midcap Fund - Regular - Growth | 119094 | 164.772 |
| 2025-07 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 160.171 |
| 2025-07 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 159.2121 |
| 2025-07 | UTI Mid Cap Fund - Regular - Growth | 102886 | 157.5782 |
| 2025-07 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 128.3088 |
| 2025-07 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 128.023 |
| 2025-07 | Kotak Flexicap Fund - Regular - Growth | 120843 | 127.2558 |
| 2025-07 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 112.0703 |
| 2025-07 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 106.254 |
| 2025-07 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 103.9067 |
| 2025-07 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 92.8845 |
| 2025-07 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 90.7414 |
| 2025-07 | Axis Small Cap Fund - Regular - Growth | 119095 | 86.7794 |
| 2025-07 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 75.264 |
| 2025-07 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 70.5445 |
| 2025-07 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.6323 |
| 2025-07 | ABSL Small Cap Fund - Regular - Growth | 101207 | 65.2818 |
| 2025-07 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.397 |
| 2025-07 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 51.3266 |
| 2025-07 | Axis Bluechip Fund - Direct - Growth | 119093 | 51.0903 |
| 2025-07 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.1182 |
| 2025-07 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.3451 |
| 2025-08 | Kotak Liquid Fund - Regular - Growth | 120844 | 4034.8981 |
| 2025-08 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 950.8718 |
| 2025-08 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 589.9706 |
| 2025-08 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 566.8467 |
| 2025-08 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 524.8752 |
| 2025-08 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 389.7695 |
| 2025-08 | ABSL Liquid Fund - Regular - Growth | 101208 | 387.6044 |
| 2025-08 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 376.3867 |
| 2025-08 | Kotak Bluechip Fund - Regular - Growth | 120841 | 372.0773 |
| 2025-08 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 367.3783 |
| 2025-08 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 328.5112 |
| 2025-08 | Nippon India ETF Nifty 50 BeES | 118635 | 293.3901 |
| 2025-08 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 258.1158 |
| 2025-08 | DSP Midcap Fund - Regular - Growth | 149323 | 219.253 |
| 2025-08 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 209.6857 |
| 2025-08 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 196.711 |
| 2025-08 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 182.1378 |
| 2025-08 | DSP Small Cap Fund - Regular - Growth | 149324 | 179.6543 |
| 2025-08 | Axis Midcap Fund - Regular - Growth | 119094 | 164.8283 |
| 2025-08 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 158.0301 |
| 2025-08 | UTI Mid Cap Fund - Regular - Growth | 102886 | 148.3734 |
| 2025-08 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 143.9614 |
| 2025-08 | Kotak Flexicap Fund - Regular - Growth | 120843 | 132.6268 |
| 2025-08 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 126.3708 |
| 2025-08 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 125.4125 |
| 2025-08 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 110.8056 |
| 2025-08 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 105.1561 |
| 2025-08 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 101.7303 |
| 2025-08 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 94.5986 |
| 2025-08 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 91.1984 |
| 2025-08 | Axis Small Cap Fund - Regular - Growth | 119095 | 84.9968 |
| 2025-08 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 77.5039 |
| 2025-08 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 73.1967 |
| 2025-08 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 69.5717 |
| 2025-08 | ABSL Small Cap Fund - Regular - Growth | 101207 | 64.3806 |
| 2025-08 | Axis Bluechip Fund - Direct - Growth | 119093 | 53.6958 |
| 2025-08 | Axis Bluechip Fund - Regular - Growth | 119092 | 52.1869 |
| 2025-08 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 52.179 |
| 2025-08 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 34.7824 |
| 2025-08 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.7492 |
| 2025-09 | Kotak Liquid Fund - Regular - Growth | 120844 | 4051.9952 |
| 2025-09 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 947.7989 |
| 2025-09 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 594.8221 |
| 2025-09 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 569.5267 |
| 2025-09 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 542.6897 |
| 2025-09 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 409.0717 |
| 2025-09 | ABSL Liquid Fund - Regular - Growth | 101208 | 389.7323 |
| 2025-09 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 375.608 |
| 2025-09 | Kotak Bluechip Fund - Regular - Growth | 120841 | 374.2751 |
| 2025-09 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 369.5669 |
| 2025-09 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 330.9107 |
| 2025-09 | Nippon India ETF Nifty 50 BeES | 118635 | 293.2405 |
| 2025-09 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 259.7019 |
| 2025-09 | DSP Midcap Fund - Regular - Growth | 149323 | 222.8748 |
| 2025-09 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 219.0156 |
| 2025-09 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 215.9681 |
| 2025-09 | DSP Small Cap Fund - Regular - Growth | 149324 | 198.6365 |
| 2025-09 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 176.6108 |
| 2025-09 | Axis Midcap Fund - Regular - Growth | 119094 | 170.9547 |
| 2025-09 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 164.8453 |
| 2025-09 | UTI Mid Cap Fund - Regular - Growth | 102886 | 149.8194 |
| 2025-09 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 137.4006 |
| 2025-09 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 131.9209 |
| 2025-09 | Kotak Flexicap Fund - Regular - Growth | 120843 | 131.8359 |
| 2025-09 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 125.776 |
| 2025-09 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 110.9952 |
| 2025-09 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 110.6154 |
| 2025-09 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 104.2862 |
| 2025-09 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 94.7015 |
| 2025-09 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 90.677 |
| 2025-09 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 78.0391 |
| 2025-09 | Axis Small Cap Fund - Regular - Growth | 119095 | 73.6795 |
| 2025-09 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 72.9715 |
| 2025-09 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 69.8867 |
| 2025-09 | ABSL Small Cap Fund - Regular - Growth | 101207 | 61.9497 |
| 2025-09 | Axis Bluechip Fund - Direct - Growth | 119093 | 53.1544 |
| 2025-09 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 52.8083 |
| 2025-09 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.0357 |
| 2025-09 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 35.0621 |
| 2025-09 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.2081 |
| 2025-10 | Kotak Liquid Fund - Regular - Growth | 120844 | 4076.6981 |
| 2025-10 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 995.3368 |
| 2025-10 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 617.653 |
| 2025-10 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 574.2006 |
| 2025-10 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 556.7206 |
| 2025-10 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 400.8721 |
| 2025-10 | ABSL Liquid Fund - Regular - Growth | 101208 | 391.9345 |
| 2025-10 | Kotak Bluechip Fund - Regular - Growth | 120841 | 390.4703 |
| 2025-10 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 385.2031 |
| 2025-10 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 371.7279 |
| 2025-10 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 330.0963 |
| 2025-10 | Nippon India ETF Nifty 50 BeES | 118635 | 291.9411 |
| 2025-10 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 264.4966 |
| 2025-10 | DSP Midcap Fund - Regular - Growth | 149323 | 228.1889 |
| 2025-10 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 224.5118 |
| 2025-10 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 222.6148 |
| 2025-10 | DSP Small Cap Fund - Regular - Growth | 149324 | 216.8197 |
| 2025-10 | Axis Midcap Fund - Regular - Growth | 119094 | 187.5786 |
| 2025-10 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 181.7519 |
| 2025-10 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 163.2698 |
| 2025-10 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 148.5981 |
| 2025-10 | UTI Mid Cap Fund - Regular - Growth | 102886 | 143.9248 |
| 2025-10 | Kotak Flexicap Fund - Regular - Growth | 120843 | 136.4404 |
| 2025-10 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 129.8011 |
| 2025-10 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 129.048 |
| 2025-10 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 113.6678 |
| 2025-10 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 107.0676 |
| 2025-10 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 105.6551 |
| 2025-10 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 97.4038 |
| 2025-10 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 82.8465 |
| 2025-10 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 81.8853 |
| 2025-10 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 79.345 |
| 2025-10 | Axis Small Cap Fund - Regular - Growth | 119095 | 72.4156 |
| 2025-10 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 68.8981 |
| 2025-10 | ABSL Small Cap Fund - Regular - Growth | 101207 | 60.4472 |
| 2025-10 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 52.994 |
| 2025-10 | Axis Bluechip Fund - Direct - Growth | 119093 | 52.9139 |
| 2025-10 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.5654 |
| 2025-10 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 35.1597 |
| 2025-10 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.6493 |
| 2025-11 | Kotak Liquid Fund - Regular - Growth | 120844 | 4108.0005 |
| 2025-11 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 968.5558 |
| 2025-11 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 601.6754 |
| 2025-11 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 588.7595 |
| 2025-11 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 573.9966 |
| 2025-11 | Kotak Bluechip Fund - Regular - Growth | 120841 | 420.6887 |
| 2025-11 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 399.4685 |
| 2025-11 | ABSL Liquid Fund - Regular - Growth | 101208 | 394.7572 |
| 2025-11 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 374.03 |
| 2025-11 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 373.227 |
| 2025-11 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 346.4392 |
| 2025-11 | Nippon India ETF Nifty 50 BeES | 118635 | 303.792 |
| 2025-11 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 259.7536 |
| 2025-11 | DSP Small Cap Fund - Regular - Growth | 149324 | 247.1194 |
| 2025-11 | DSP Midcap Fund - Regular - Growth | 149323 | 241.2563 |
| 2025-11 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 231.2701 |
| 2025-11 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 223.0935 |
| 2025-11 | Axis Midcap Fund - Regular - Growth | 119094 | 198.8225 |
| 2025-11 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 186.6392 |
| 2025-11 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 169.4293 |
| 2025-11 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 160.2232 |
| 2025-11 | Kotak Flexicap Fund - Regular - Growth | 120843 | 148.3773 |
| 2025-11 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 133.3927 |
| 2025-11 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 128.2945 |
| 2025-11 | UTI Mid Cap Fund - Regular - Growth | 102886 | 126.6312 |
| 2025-11 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 113.5099 |
| 2025-11 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 112.5105 |
| 2025-11 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 110.5353 |
| 2025-11 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 97.4104 |
| 2025-11 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 83.961 |
| 2025-11 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 81.5502 |
| 2025-11 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 77.5761 |
| 2025-11 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 74.6011 |
| 2025-11 | Axis Small Cap Fund - Regular - Growth | 119095 | 73.0901 |
| 2025-11 | ABSL Small Cap Fund - Regular - Growth | 101207 | 64.5792 |
| 2025-11 | Axis Bluechip Fund - Direct - Growth | 119093 | 56.1586 |
| 2025-11 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 53.4804 |
| 2025-11 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.9512 |
| 2025-11 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 35.8555 |
| 2025-11 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 32.3849 |
| 2025-12 | Kotak Liquid Fund - Regular - Growth | 120844 | 4134.5339 |
| 2025-12 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 1007.9422 |
| 2025-12 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 618.3523 |
| 2025-12 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 616.8204 |
| 2025-12 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 561.6454 |
| 2025-12 | Kotak Bluechip Fund - Regular - Growth | 120841 | 434.8407 |
| 2025-12 | ABSL Liquid Fund - Regular - Growth | 101208 | 397.5444 |
| 2025-12 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 392.587 |
| 2025-12 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 390.7785 |
| 2025-12 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 374.8525 |
| 2025-12 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 362.8311 |
| 2025-12 | Nippon India ETF Nifty 50 BeES | 118635 | 314.418 |
| 2025-12 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 273.8729 |
| 2025-12 | DSP Small Cap Fund - Regular - Growth | 149324 | 253.557 |
| 2025-12 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 249.3207 |
| 2025-12 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 231.6107 |
| 2025-12 | DSP Midcap Fund - Regular - Growth | 149323 | 225.1673 |
| 2025-12 | Axis Midcap Fund - Regular - Growth | 119094 | 201.6537 |
| 2025-12 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 184.6655 |
| 2025-12 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 173.9167 |
| 2025-12 | Kotak Flexicap Fund - Regular - Growth | 120843 | 164.1016 |
| 2025-12 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 157.1546 |
| 2025-12 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 150.5511 |
| 2025-12 | UTI Mid Cap Fund - Regular - Growth | 102886 | 135.7931 |
| 2025-12 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 130.7504 |
| 2025-12 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 121.2432 |
| 2025-12 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 113.8015 |
| 2025-12 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 110.6449 |
| 2025-12 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 96.0467 |
| 2025-12 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 93.4877 |
| 2025-12 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 79.3529 |
| 2025-12 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 75.0795 |
| 2025-12 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 73.6773 |
| 2025-12 | Axis Small Cap Fund - Regular - Growth | 119095 | 68.908 |
| 2025-12 | ABSL Small Cap Fund - Regular - Growth | 101207 | 65.487 |
| 2025-12 | Axis Bluechip Fund - Direct - Growth | 119093 | 57.7009 |
| 2025-12 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 53.7532 |
| 2025-12 | Axis Bluechip Fund - Regular - Growth | 119092 | 53.3357 |
| 2025-12 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 36.5452 |
| 2025-12 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 32.4208 |
| 2026-01 | Kotak Liquid Fund - Regular - Growth | 120844 | 4155.1329 |
| 2026-01 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 1049.8884 |
| 2026-01 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 634.9168 |
| 2026-01 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 632.0801 |
| 2026-01 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 594.178 |
| 2026-01 | Kotak Bluechip Fund - Regular - Growth | 120841 | 434.0718 |
| 2026-01 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 407.2707 |
| 2026-01 | ABSL Liquid Fund - Regular - Growth | 101208 | 399.8416 |
| 2026-01 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 391.3388 |
| 2026-01 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 377.9214 |
| 2026-01 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 370.3469 |
| 2026-01 | Nippon India ETF Nifty 50 BeES | 118635 | 326.706 |
| 2026-01 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 295.0782 |
| 2026-01 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 260.812 |
| 2026-01 | DSP Small Cap Fund - Regular - Growth | 149324 | 253.408 |
| 2026-01 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 229.257 |
| 2026-01 | DSP Midcap Fund - Regular - Growth | 149323 | 226.2017 |
| 2026-01 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 197.7986 |
| 2026-01 | Axis Midcap Fund - Regular - Growth | 119094 | 190.9612 |
| 2026-01 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 177.4214 |
| 2026-01 | Kotak Flexicap Fund - Regular - Growth | 120843 | 164.2575 |
| 2026-01 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 159.2432 |
| 2026-01 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 156.9472 |
| 2026-01 | UTI Mid Cap Fund - Regular - Growth | 102886 | 142.2224 |
| 2026-01 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 132.402 |
| 2026-01 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 126.863 |
| 2026-01 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 109.1682 |
| 2026-01 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 108.0825 |
| 2026-01 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 97.5942 |
| 2026-01 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 89.4147 |
| 2026-01 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 82.5268 |
| 2026-01 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 74.7622 |
| 2026-01 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 69.3294 |
| 2026-01 | Axis Small Cap Fund - Regular - Growth | 119095 | 66.7387 |
| 2026-01 | ABSL Small Cap Fund - Regular - Growth | 101207 | 63.9546 |
| 2026-01 | Axis Bluechip Fund - Regular - Growth | 119092 | 55.6395 |
| 2026-01 | Axis Bluechip Fund - Direct - Growth | 119093 | 55.5213 |
| 2026-01 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 54.3601 |
| 2026-01 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 37.1215 |
| 2026-01 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 32.1394 |
| 2026-02 | Kotak Liquid Fund - Regular - Growth | 120844 | 4181.709 |
| 2026-02 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 1099.2502 |
| 2026-02 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 659.706 |
| 2026-02 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 628.2176 |
| 2026-02 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 593.424 |
| 2026-02 | Kotak Bluechip Fund - Regular - Growth | 120841 | 447.5266 |
| 2026-02 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 433.0175 |
| 2026-02 | ABSL Liquid Fund - Regular - Growth | 101208 | 402.1108 |
| 2026-02 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 393.826 |
| 2026-02 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 392.1432 |
| 2026-02 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 379.982 |
| 2026-02 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 329.7697 |
| 2026-02 | Nippon India ETF Nifty 50 BeES | 118635 | 327.4978 |
| 2026-02 | DSP Small Cap Fund - Regular - Growth | 149324 | 249.4504 |
| 2026-02 | DSP Midcap Fund - Regular - Growth | 149323 | 245.694 |
| 2026-02 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 244.0047 |
| 2026-02 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 225.5904 |
| 2026-02 | Axis Midcap Fund - Regular - Growth | 119094 | 202.9856 |
| 2026-02 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 193.8288 |
| 2026-02 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 181.13 |
| 2026-02 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 168.2192 |
| 2026-02 | Kotak Flexicap Fund - Regular - Growth | 120843 | 166.3105 |
| 2026-02 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 155.2564 |
| 2026-02 | UTI Mid Cap Fund - Regular - Growth | 102886 | 137.5087 |
| 2026-02 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 135.5922 |
| 2026-02 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 124.8342 |
| 2026-02 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 102.8202 |
| 2026-02 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 100.5364 |
| 2026-02 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 100.4291 |
| 2026-02 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 89.9668 |
| 2026-02 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 86.2047 |
| 2026-02 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 77.7433 |
| 2026-02 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 67.8868 |
| 2026-02 | Axis Small Cap Fund - Regular - Growth | 119095 | 66.5923 |
| 2026-02 | ABSL Small Cap Fund - Regular - Growth | 101207 | 59.0096 |
| 2026-02 | Axis Bluechip Fund - Regular - Growth | 119092 | 55.0476 |
| 2026-02 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 54.7665 |
| 2026-02 | Axis Bluechip Fund - Direct - Growth | 119093 | 52.4642 |
| 2026-02 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 37.3361 |
| 2026-02 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.9793 |
| 2026-03 | Kotak Liquid Fund - Regular - Growth | 120844 | 4204.8957 |
| 2026-03 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 1158.784 |
| 2026-03 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 733.1982 |
| 2026-03 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 612.0151 |
| 2026-03 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 588.3734 |
| 2026-03 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 447.0392 |
| 2026-03 | Kotak Bluechip Fund - Regular - Growth | 120841 | 433.8545 |
| 2026-03 | ABSL Liquid Fund - Regular - Growth | 101208 | 404.4728 |
| 2026-03 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 403.0965 |
| 2026-03 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 381.8889 |
| 2026-03 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 372.92 |
| 2026-03 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 340.9029 |
| 2026-03 | Nippon India ETF Nifty 50 BeES | 118635 | 323.0834 |
| 2026-03 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 263.9734 |
| 2026-03 | DSP Small Cap Fund - Regular - Growth | 149324 | 263.092 |
| 2026-03 | DSP Midcap Fund - Regular - Growth | 149323 | 242.0508 |
| 2026-03 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 232.7202 |
| 2026-03 | Axis Midcap Fund - Regular - Growth | 119094 | 200.5583 |
| 2026-03 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 190.8932 |
| 2026-03 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 180.5553 |
| 2026-03 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 172.1597 |
| 2026-03 | Kotak Flexicap Fund - Regular - Growth | 120843 | 161.9051 |
| 2026-03 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 158.8155 |
| 2026-03 | UTI Mid Cap Fund - Regular - Growth | 102886 | 142.4235 |
| 2026-03 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 136.6254 |
| 2026-03 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 130.0495 |
| 2026-03 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 110.7804 |
| 2026-03 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 106.2123 |
| 2026-03 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 104.159 |
| 2026-03 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 95.3254 |
| 2026-03 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 86.0774 |
| 2026-03 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 80.2019 |
| 2026-03 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 71.7423 |
| 2026-03 | Axis Small Cap Fund - Regular - Growth | 119095 | 67.9901 |
| 2026-03 | ABSL Small Cap Fund - Regular - Growth | 101207 | 59.3687 |
| 2026-03 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 54.627 |
| 2026-03 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.4386 |
| 2026-03 | Axis Bluechip Fund - Direct - Growth | 119093 | 51.4375 |
| 2026-03 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 37.1525 |
| 2026-03 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.5663 |
| 2026-04 | Kotak Liquid Fund - Regular - Growth | 120844 | 4227.0248 |
| 2026-04 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 1238.8934 |
| 2026-04 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 771.6019 |
| 2026-04 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 609.8956 |
| 2026-04 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 605.5012 |
| 2026-04 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 453.9026 |
| 2026-04 | Kotak Bluechip Fund - Regular - Growth | 120841 | 439.3757 |
| 2026-04 | ABSL Liquid Fund - Regular - Growth | 101208 | 406.435 |
| 2026-04 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 398.9505 |
| 2026-04 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 384.6639 |
| 2026-04 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 376.0224 |
| 2026-04 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 359.9597 |
| 2026-04 | Nippon India ETF Nifty 50 BeES | 118635 | 321.5367 |
| 2026-04 | DSP Small Cap Fund - Regular - Growth | 149324 | 305.8018 |
| 2026-04 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 277.7281 |
| 2026-04 | DSP Midcap Fund - Regular - Growth | 149323 | 247.4074 |
| 2026-04 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 244.4083 |
| 2026-04 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 201.4538 |
| 2026-04 | Axis Midcap Fund - Regular - Growth | 119094 | 193.2068 |
| 2026-04 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 179.7737 |
| 2026-04 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 179.4287 |
| 2026-04 | Kotak Flexicap Fund - Regular - Growth | 120843 | 176.706 |
| 2026-04 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 156.4203 |
| 2026-04 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 137.6774 |
| 2026-04 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 135.5198 |
| 2026-04 | UTI Mid Cap Fund - Regular - Growth | 102886 | 127.3016 |
| 2026-04 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 125.7904 |
| 2026-04 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 112.6007 |
| 2026-04 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 111.9964 |
| 2026-04 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 98.5555 |
| 2026-04 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 86.1852 |
| 2026-04 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 85.2645 |
| 2026-04 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 76.2261 |
| 2026-04 | Axis Small Cap Fund - Regular - Growth | 119095 | 64.0152 |
| 2026-04 | ABSL Small Cap Fund - Regular - Growth | 101207 | 55.6294 |
| 2026-04 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 54.7349 |
| 2026-04 | Axis Bluechip Fund - Direct - Growth | 119093 | 52.8938 |
| 2026-04 | Axis Bluechip Fund - Regular - Growth | 119092 | 51.8856 |
| 2026-04 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 37.1062 |
| 2026-04 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.9156 |
| 2026-05 | Kotak Liquid Fund - Regular - Growth | 120844 | 4254.0005 |
| 2026-05 | HDFC Top 100 Fund - Direct Plan - Growth | 125497 | 1202.9618 |
| 2026-05 | ABSL Frontline Equity Fund - Regular - Growth | 101206 | 780.4739 |
| 2026-05 | DSP Top 100 Equity Fund - Regular - Growth | 149322 | 614.1199 |
| 2026-05 | HDFC Top 100 Fund - Regular Plan - Growth | 100016 | 592.3666 |
| 2026-05 | ICICI Pru Midcap Fund - Regular - Growth | 120505 | 467.6264 |
| 2026-05 | Kotak Bluechip Fund - Regular - Growth | 120841 | 465.6312 |
| 2026-05 | ABSL Liquid Fund - Regular - Growth | 101208 | 408.8293 |
| 2026-05 | ICICI Pru Value Discovery Fund - Regular - Growth | 120506 | 396.1871 |
| 2026-05 | ICICI Pru Liquid Fund - Regular - Growth | 120507 | 387.446 |
| 2026-05 | UTI Flexi Cap Fund - Regular - Growth | 102887 | 366.2445 |
| 2026-05 | HDFC Mid-Cap Opportunities Fund - Regular - Growth | 100033 | 352.1477 |
| 2026-05 | Nippon India ETF Nifty 50 BeES | 118635 | 326.3993 |
| 2026-05 | SBI Small Cap Fund - Regular Plan - Growth | 119598 | 309.9404 |
| 2026-05 | DSP Small Cap Fund - Regular - Growth | 149324 | 304.867 |
| 2026-05 | DSP Midcap Fund - Regular - Growth | 149323 | 250.2751 |
| 2026-05 | Mirae Asset Large Cap Fund - Regular - Growth | 148567 | 238.7739 |
| 2026-05 | Mirae Asset Emerging Bluechip Fund - Regular - Growth | 148568 | 200.0251 |
| 2026-05 | Axis Midcap Fund - Regular - Growth | 119094 | 197.5096 |
| 2026-05 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | 125498 | 187.9973 |
| 2026-05 | UTI Nifty 50 Index Fund - Regular - Growth | 102885 | 184.5136 |
| 2026-05 | Kotak Flexicap Fund - Regular - Growth | 120843 | 171.5853 |
| 2026-05 | ICICI Pru Bluechip Fund - Direct - Growth | 120504 | 151.7633 |
| 2026-05 | SBI Bluechip Fund - Regular Plan - Growth | 119551 | 148.1715 |
| 2026-05 | Nippon India Small Cap Fund - Regular - Growth | 118634 | 135.6112 |
| 2026-05 | SBI Bluechip Fund - Direct Plan - Growth | 119552 | 134.4602 |
| 2026-05 | UTI Mid Cap Fund - Regular - Growth | 102886 | 125.4806 |
| 2026-05 | ICICI Pru Bluechip Fund - Regular - Growth | 120503 | 114.7507 |
| 2026-05 | Nippon India Large Cap Fund - Regular - Growth | 118632 | 109.5629 |
| 2026-05 | SBI Small Cap Fund - Direct Plan - Growth | 119599 | 101.639 |
| 2026-05 | Mirae Asset Tax Saver Fund - Regular - Growth | 148569 | 90.6994 |
| 2026-05 | Nippon India Large Cap Fund - Direct - Growth | 118633 | 89.4791 |
| 2026-05 | Kotak Emerging Equity Fund - Regular - Growth | 120842 | 79.6063 |
| 2026-05 | Axis Bluechip Fund - Direct - Growth | 119093 | 56.1706 |
| 2026-05 | Axis Small Cap Fund - Regular - Growth | 119095 | 54.5126 |
| 2026-05 | SBI Magnum Gilt Fund - Regular Plan - Growth | 119120 | 54.4541 |
| 2026-05 | ABSL Small Cap Fund - Regular - Growth | 101207 | 53.1598 |
| 2026-05 | Axis Bluechip Fund - Regular - Growth | 119092 | 50.7831 |
| 2026-05 | Nippon India Gilt Securities Fund - Regular - Growth | 118636 | 37.485 |
| 2026-05 | HDFC Short Term Debt Fund - Regular - Growth | 100025 | 31.9019 |

---

## Query 3: 3. SIP YoY Growth | Calculates the YoY growth percentage of total SIP transaction amounts from fact_transactions. | It groups by year and month, then joins the monthly amounts with the same month in the previous year.
```sql
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
```

### Results
| current_month | current_amount | prev_year_month | prev_amount | yoy_growth_pct |
| --- | --- | --- | --- | --- |
| 2025-01 | 13082145.0 | 2024-01 | 12635349.0 | 3.54 |
| 2025-02 | 11363922.0 | 2024-02 | 12613376.0 | -9.91 |
| 2025-03 | 13449360.0 | 2024-03 | 12088413.0 | 11.26 |
| 2025-04 | 12132001.0 | 2024-04 | 13512385.0 | -10.22 |
| 2025-05 | 13973011.0 | 2024-05 | 13218606.0 | 5.71 |

---

## Query 4: 4. Transactions by State | Aggregates transaction counts and total transaction amount per state from fact_transactions.
```sql
SELECT 
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_transaction_amount_inr,
    ROUND(AVG(amount_inr), 2) AS average_transaction_amount_inr
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount_inr DESC;
```

### Results
| state | transaction_count | total_transaction_amount_inr | average_transaction_amount_inr |
| --- | --- | --- | --- |
| Punjab | 2965 | 315780459.0 | 106502.68 |
| Tamil Nadu | 2806 | 315177237.0 | 112322.61 |
| Madhya Pradesh | 2931 | 308312493.0 | 105190.21 |
| Rajasthan | 2577 | 298645822.0 | 115888.95 |
| Gujarat | 2780 | 298358940.0 | 107323.36 |
| West Bengal | 2748 | 297182514.0 | 108145.02 |
| Telangana | 2718 | 290219284.0 | 106776.78 |
| Delhi | 2677 | 289633404.0 | 108193.28 |
| Uttar Pradesh | 2695 | 285368873.0 | 105888.26 |
| Haryana | 2736 | 279634354.0 | 102205.54 |
| Karnataka | 2621 | 273753570.0 | 104446.23 |
| Maharashtra | 2524 | 269513480.0 | 106780.3 |

---

## Query 5: 5. Funds with Expense Ratio < 1% | Lists funds with low expense ratios from dim_fund.
```sql
SELECT 
    amfi_code,
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;
```

### Results
| amfi_code | scheme_name | fund_house | category | expense_ratio_pct |
| --- | --- | --- | --- | --- |
| 118636 | Nippon India Gilt Securities Fund - Regular - Growth | Nippon India MF | Debt | 0.55 |
| 100025 | HDFC Short Term Debt Fund - Regular - Growth | HDFC Mutual Fund | Debt | 0.56 |
| 120844 | Kotak Liquid Fund - Regular - Growth | Kotak Mahindra MF | Debt | 0.6 |
| 119552 | SBI Bluechip Fund - Direct Plan - Growth | SBI Mutual Fund | Equity | 0.66 |
| 118633 | Nippon India Large Cap Fund - Direct - Growth | Nippon India MF | Equity | 0.72 |
| 119599 | SBI Small Cap Fund - Direct Plan - Growth | SBI Mutual Fund | Equity | 0.72 |
| 120507 | ICICI Pru Liquid Fund - Regular - Growth | ICICI Prudential MF | Debt | 0.74 |
| 119093 | Axis Bluechip Fund - Direct - Growth | Axis Mutual Fund | Equity | 0.75 |
| 119120 | SBI Magnum Gilt Fund - Regular Plan - Growth | SBI Mutual Fund | Debt | 0.77 |
| 125498 | HDFC Mid-Cap Opportunities Fund - Direct - Growth | HDFC Mutual Fund | Equity | 0.78 |
| 101208 | ABSL Liquid Fund - Regular - Growth | Aditya Birla Sun Life MF | Debt | 0.79 |
| 120504 | ICICI Pru Bluechip Fund - Direct - Growth | ICICI Prudential MF | Equity | 0.8 |
| 118635 | Nippon India ETF Nifty 50 BeES | Nippon India MF | Equity | 0.89 |
| 125497 | HDFC Top 100 Fund - Direct Plan - Growth | HDFC Mutual Fund | Equity | 0.92 |

---

## Query 6: 6. Top 5 Sectors by Portfolio Holdings Market Value | Groups portfolio holdings by sector to find the highest market value in crores.
```sql
SELECT 
    sector,
    COUNT(DISTINCT stock_symbol) AS unique_stocks_count,
    ROUND(SUM(market_value_cr), 2) AS total_market_value_cr,
    ROUND(AVG(weight_pct), 2) AS average_weight_pct
FROM fact_portfolio_holdings
GROUP BY sector
ORDER BY total_market_value_cr DESC
LIMIT 5;
```

### Results
| sector | unique_stocks_count | total_market_value_cr | average_weight_pct |
| --- | --- | --- | --- |
| Banking | 6 | 62840.29 | 10.87 |
| IT | 4 | 38477.11 | 11.39 |
| Pharma | 4 | 34606.1 | 10.72 |
| Automobile | 3 | 34296.97 | 9.81 |
| Utilities | 2 | 25108.63 | 11.06 |

---

## Query 7: 7. Transactions and Income Stats by Age Group and Transaction Type | Shows transaction count, total volume, and average investor annual income grouped by transaction type and age group.
```sql
SELECT 
    transaction_type,
    age_group,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount_inr,
    ROUND(AVG(annual_income_lakh), 2) AS average_annual_income_lakh
FROM fact_transactions
GROUP BY transaction_type, age_group
ORDER BY transaction_type ASC, transaction_count DESC;
```

### Results
| transaction_type | age_group | transaction_count | total_amount_inr | average_annual_income_lakh |
| --- | --- | --- | --- | --- |
| Lumpsum | 26-35 | 3372 | 862283467.0 | 15.48 |
| Lumpsum | 36-45 | 1976 | 498898372.0 | 35.17 |
| Lumpsum | 18-25 | 1205 | 307670734.0 | 5.45 |
| Lumpsum | 46-55 | 924 | 238466416.0 | 56.44 |
| Lumpsum | 56+ | 618 | 152502459.0 | 43.73 |
| Redemption | 26-35 | 2028 | 500729411.0 | 15.71 |
| Redemption | 36-45 | 1244 | 319125909.0 | 36.52 |
| Redemption | 18-25 | 762 | 191668045.0 | 5.36 |
| Redemption | 46-55 | 555 | 141325497.0 | 57.31 |
| Redemption | 56+ | 378 | 91676629.0 | 46.31 |
| SIP | 26-35 | 8063 | 88587340.0 | 15.64 |
| SIP | 36-45 | 4926 | 53623247.0 | 36.1 |
| SIP | 18-25 | 2949 | 32300613.0 | 5.47 |
| SIP | 46-55 | 2300 | 25614556.0 | 58.52 |
| SIP | 56+ | 1478 | 17107735.0 | 44.3 |

---

## Query 8: 8. Monthly Net Inflows by Scheme Category | Details monthly net inflows for Large Cap, Mid Cap, Small Cap, etc. from category inflows.
```sql
SELECT 
    strftime('%Y-%m', month) AS year_month,
    category,
    net_inflow_crore
FROM fact_category_inflows
ORDER BY year_month ASC, net_inflow_crore DESC;
```

### Results
| year_month | category | net_inflow_crore |
| --- | --- | --- |
| 2024-04 | Liquid | 37537.0 |
| 2024-04 | Sectoral/Thematic | 8052.0 |
| 2024-04 | Flexi Cap | 4947.0 |
| 2024-04 | Short Duration | 4400.0 |
| 2024-04 | Large & Mid Cap | 4214.0 |
| 2024-04 | Mid Cap | 3897.0 |
| 2024-04 | Small Cap | 3533.0 |
| 2024-04 | Hybrid | 2955.0 |
| 2024-04 | Large Cap | 2413.0 |
| 2024-04 | Value/Contra | 1328.0 |
| 2024-04 | Gilt | 784.0 |
| 2024-04 | ELSS | 466.0 |
| 2024-05 | Liquid | 41872.0 |
| 2024-05 | Sectoral/Thematic | 8354.0 |
| 2024-05 | Flexi Cap | 5529.0 |
| 2024-05 | Mid Cap | 5300.0 |
| 2024-05 | Short Duration | 4833.0 |
| 2024-05 | Large & Mid Cap | 4368.0 |
| 2024-05 | Small Cap | 4092.0 |
| 2024-05 | Hybrid | 3487.0 |
| 2024-05 | Large Cap | 2076.0 |
| 2024-05 | Value/Contra | 1361.0 |
| 2024-05 | Gilt | 836.0 |
| 2024-05 | ELSS | 553.0 |
| 2024-06 | Liquid | 40486.0 |
| 2024-06 | Sectoral/Thematic | 10030.0 |
| 2024-06 | Mid Cap | 5047.0 |
| 2024-06 | Large & Mid Cap | 4610.0 |
| 2024-06 | Flexi Cap | 4478.0 |
| 2024-06 | Short Duration | 4321.0 |
| 2024-06 | Small Cap | 3535.0 |
| 2024-06 | Hybrid | 3163.0 |
| 2024-06 | Large Cap | 2519.0 |
| 2024-06 | Value/Contra | 1386.0 |
| 2024-06 | Gilt | 864.0 |
| 2024-06 | ELSS | 472.0 |
| 2024-07 | Liquid | 34643.0 |
| 2024-07 | Sectoral/Thematic | 9896.0 |
| 2024-07 | Large & Mid Cap | 5023.0 |
| 2024-07 | Flexi Cap | 4869.0 |
| 2024-07 | Mid Cap | 4548.0 |
| 2024-07 | Short Duration | 4170.0 |
| 2024-07 | Small Cap | 3582.0 |
| 2024-07 | Hybrid | 3291.0 |
| 2024-07 | Large Cap | 2574.0 |
| 2024-07 | Value/Contra | 1582.0 |
| 2024-07 | Gilt | 959.0 |
| 2024-07 | ELSS | 471.0 |
| 2024-08 | Liquid | 41952.0 |
| 2024-08 | Sectoral/Thematic | 8360.0 |
| 2024-08 | Flexi Cap | 5562.0 |
| 2024-08 | Large & Mid Cap | 5411.0 |
| 2024-08 | Short Duration | 4658.0 |
| 2024-08 | Mid Cap | 3899.0 |
| 2024-08 | Hybrid | 3684.0 |
| 2024-08 | Small Cap | 3376.0 |
| 2024-08 | Large Cap | 1940.0 |
| 2024-08 | Value/Contra | 1308.0 |
| 2024-08 | Gilt | 952.0 |
| 2024-08 | ELSS | 499.0 |
| 2024-09 | Liquid | 35308.0 |
| 2024-09 | Sectoral/Thematic | 8518.0 |
| 2024-09 | Flexi Cap | 5397.0 |
| 2024-09 | Short Duration | 5327.0 |
| 2024-09 | Mid Cap | 4960.0 |
| 2024-09 | Large & Mid Cap | 4528.0 |
| 2024-09 | Small Cap | 4137.0 |
| 2024-09 | Hybrid | 3015.0 |
| 2024-09 | Large Cap | 1879.0 |
| 2024-09 | Value/Contra | 1334.0 |
| 2024-09 | Gilt | 925.0 |
| 2024-09 | ELSS | 537.0 |
| 2024-10 | Liquid | 39091.0 |
| 2024-10 | Sectoral/Thematic | 7680.0 |
| 2024-10 | Flexi Cap | 6004.0 |
| 2024-10 | Short Duration | 4675.0 |
| 2024-10 | Large & Mid Cap | 4581.0 |
| 2024-10 | Small Cap | 4444.0 |
| 2024-10 | Mid Cap | 4106.0 |
| 2024-10 | Hybrid | 3314.0 |
| 2024-10 | Large Cap | 2255.0 |
| 2024-10 | Value/Contra | 1595.0 |
| 2024-10 | Gilt | 898.0 |
| 2024-10 | ELSS | 537.0 |
| 2024-11 | Liquid | 40506.0 |
| 2024-11 | Sectoral/Thematic | 7397.0 |
| 2024-11 | Flexi Cap | 6111.0 |
| 2024-11 | Large & Mid Cap | 5556.0 |
| 2024-11 | Short Duration | 5316.0 |
| 2024-11 | Mid Cap | 4336.0 |
| 2024-11 | Hybrid | 3264.0 |
| 2024-11 | Small Cap | 3256.0 |
| 2024-11 | Large Cap | 1870.0 |
| 2024-11 | Value/Contra | 1436.0 |
| 2024-11 | Gilt | 704.0 |
| 2024-11 | ELSS | 571.0 |
| 2024-12 | Liquid | 34933.0 |
| 2024-12 | Sectoral/Thematic | 9820.0 |
| 2024-12 | Mid Cap | 5023.0 |
| 2024-12 | Large & Mid Cap | 4878.0 |
| 2024-12 | Flexi Cap | 4654.0 |
| 2024-12 | Small Cap | 4249.0 |
| 2024-12 | Short Duration | 4159.0 |
| 2024-12 | Hybrid | 3538.0 |
| 2024-12 | Large Cap | 1923.0 |
| 2024-12 | Value/Contra | 1414.0 |
| 2024-12 | Gilt | 831.0 |
| 2024-12 | ELSS | 521.0 |
| 2025-01 | Liquid | 33892.0 |
| 2025-01 | Sectoral/Thematic | 7893.0 |
| 2025-01 | Flexi Cap | 5603.0 |
| 2025-01 | Large & Mid Cap | 4816.0 |
| 2025-01 | Short Duration | 4752.0 |
| 2025-01 | Small Cap | 4554.0 |
| 2025-01 | Mid Cap | 4316.0 |
| 2025-01 | Hybrid | 2967.0 |
| 2025-01 | Large Cap | 2025.0 |
| 2025-01 | Value/Contra | 1339.0 |
| 2025-01 | Gilt | 744.0 |
| 2025-01 | ELSS | 516.0 |
| 2025-02 | Liquid | 32374.0 |
| 2025-02 | Sectoral/Thematic | 9215.0 |
| 2025-02 | Flexi Cap | 6068.0 |
| 2025-02 | Large & Mid Cap | 5524.0 |
| 2025-02 | Mid Cap | 4819.0 |
| 2025-02 | Short Duration | 4033.0 |
| 2025-02 | Small Cap | 3534.0 |
| 2025-02 | Hybrid | 3360.0 |
| 2025-02 | Large Cap | 1925.0 |
| 2025-02 | Value/Contra | 1400.0 |
| 2025-02 | Gilt | 942.0 |
| 2025-02 | ELSS | 437.0 |
| 2025-03 | Liquid | 38681.0 |
| 2025-03 | Sectoral/Thematic | 8614.0 |
| 2025-03 | Mid Cap | 5061.0 |
| 2025-03 | Short Duration | 4886.0 |
| 2025-03 | Flexi Cap | 4767.0 |
| 2025-03 | Small Cap | 4304.0 |
| 2025-03 | Large & Mid Cap | 4243.0 |
| 2025-03 | Hybrid | 2830.0 |
| 2025-03 | Large Cap | 2234.0 |
| 2025-03 | Value/Contra | 1497.0 |
| 2025-03 | Gilt | 956.0 |
| 2025-03 | ELSS | 500.0 |

---

## Query 9: 9. Index vs. Fund NAV Performance Comparison | Compares the daily close value of the NIFTY100 index to the NAV of SBI Bluechip Fund (AMFI: 119551) which benchmarks against it. | This shows how the fund tracks the index value day-to-day.
```sql
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
```

### Results
| date | scheme_name | fund_nav | index_name | index_close_value |
| --- | --- | --- | --- | --- |
| 2022-01-03 | SBI Bluechip Fund - Regular Plan - Growth | 54.3856 | NIFTY100 | 17778.24 |
| 2022-01-04 | SBI Bluechip Fund - Regular Plan - Growth | 54.3474 | NIFTY100 | 17537.52 |
| 2022-01-05 | SBI Bluechip Fund - Regular Plan - Growth | 54.6869 | NIFTY100 | 17607.73 |
| 2022-01-06 | SBI Bluechip Fund - Regular Plan - Growth | 55.455 | NIFTY100 | 17556.05 |
| 2022-01-07 | SBI Bluechip Fund - Regular Plan - Growth | 55.3692 | NIFTY100 | 17664.02 |
| 2022-01-10 | SBI Bluechip Fund - Regular Plan - Growth | 55.2835 | NIFTY100 | 17516.51 |
| 2022-01-11 | SBI Bluechip Fund - Regular Plan - Growth | 56.0878 | NIFTY100 | 17603.08 |
| 2022-01-12 | SBI Bluechip Fund - Regular Plan - Growth | 56.4978 | NIFTY100 | 17763.76 |
| 2022-01-13 | SBI Bluechip Fund - Regular Plan - Growth | 56.2934 | NIFTY100 | 17830.3 |
| 2022-01-14 | SBI Bluechip Fund - Regular Plan - Growth | 56.5926 | NIFTY100 | 17578.93 |
| 2022-01-17 | SBI Bluechip Fund - Regular Plan - Growth | 56.3908 | NIFTY100 | 17945.01 |
| 2022-01-18 | SBI Bluechip Fund - Regular Plan - Growth | 56.1887 | NIFTY100 | 18041.24 |
| 2022-01-19 | SBI Bluechip Fund - Regular Plan - Growth | 56.3378 | NIFTY100 | 18014.52 |
| 2022-01-20 | SBI Bluechip Fund - Regular Plan - Growth | 55.4237 | NIFTY100 | 18115.34 |
| 2022-01-21 | SBI Bluechip Fund - Regular Plan - Growth | 54.6151 | NIFTY100 | 18440.19 |

---

## Query 10: 10. AUM Growth by Fund House over Time | Shows quarterly AUM changes and active schemes counts for each AMC.
```sql
SELECT 
    date,
    fund_house,
    aum_crore,
    num_schemes
FROM fact_aum
ORDER BY fund_house ASC, date ASC;
```

### Results
| date | fund_house | aum_crore | num_schemes |
| --- | --- | --- | --- |
| 2022-03-31 | Aditya Birla Sun Life MF | 278000.0 | 199 |
| 2022-09-30 | Aditya Birla Sun Life MF | 285000.0 | 199 |
| 2023-03-31 | Aditya Birla Sun Life MF | 275000.0 | 199 |
| 2023-09-30 | Aditya Birla Sun Life MF | 308000.0 | 199 |
| 2024-03-31 | Aditya Birla Sun Life MF | 340000.0 | 199 |
| 2024-09-30 | Aditya Birla Sun Life MF | 362000.0 | 199 |
| 2024-12-31 | Aditya Birla Sun Life MF | 384000.0 | 199 |
| 2025-03-31 | Aditya Birla Sun Life MF | 385000.0 | 199 |
| 2025-12-31 | Aditya Birla Sun Life MF | 460000.0 | 199 |
| 2022-03-31 | Axis Mutual Fund | 250000.0 | 95 |
| 2022-09-30 | Axis Mutual Fund | 240000.0 | 95 |
| 2023-03-31 | Axis Mutual Fund | 241000.0 | 95 |
| 2023-09-30 | Axis Mutual Fund | 260000.0 | 95 |
| 2024-03-31 | Axis Mutual Fund | 280000.0 | 95 |
| 2024-09-30 | Axis Mutual Fund | 290000.0 | 95 |
| 2024-12-31 | Axis Mutual Fund | 300000.0 | 95 |
| 2025-03-31 | Axis Mutual Fund | 310000.0 | 95 |
| 2025-12-31 | Axis Mutual Fund | 350000.0 | 95 |
| 2022-03-31 | DSP Mutual Fund | 110000.0 | 88 |
| 2022-09-30 | DSP Mutual Fund | 112000.0 | 88 |
| 2023-03-31 | DSP Mutual Fund | 115000.0 | 88 |
| 2023-09-30 | DSP Mutual Fund | 132000.0 | 88 |
| 2024-03-31 | DSP Mutual Fund | 155000.0 | 88 |
| 2024-09-30 | DSP Mutual Fund | 172000.0 | 88 |
| 2024-12-31 | DSP Mutual Fund | 188000.0 | 88 |
| 2025-03-31 | DSP Mutual Fund | 195000.0 | 88 |
| 2025-12-31 | DSP Mutual Fund | 230000.0 | 88 |
| 2022-03-31 | HDFC Mutual Fund | 435000.0 | 195 |
| 2022-09-30 | HDFC Mutual Fund | 445000.0 | 195 |
| 2023-03-31 | HDFC Mutual Fund | 450000.0 | 195 |
| 2023-09-30 | HDFC Mutual Fund | 535000.0 | 195 |
| 2024-03-31 | HDFC Mutual Fund | 645000.0 | 195 |
| 2024-09-30 | HDFC Mutual Fund | 710000.0 | 195 |
| 2024-12-31 | HDFC Mutual Fund | 787000.0 | 195 |
| 2025-03-31 | HDFC Mutual Fund | 795000.0 | 195 |
| 2025-12-31 | HDFC Mutual Fund | 930000.0 | 195 |
| 2022-03-31 | ICICI Prudential MF | 465000.0 | 216 |
| 2022-09-30 | ICICI Prudential MF | 488000.0 | 216 |
| 2023-03-31 | ICICI Prudential MF | 500000.0 | 216 |
| 2023-09-30 | ICICI Prudential MF | 590000.0 | 216 |
| 2024-03-31 | ICICI Prudential MF | 680000.0 | 216 |
| 2024-09-30 | ICICI Prudential MF | 742000.0 | 216 |
| 2024-12-31 | ICICI Prudential MF | 874000.0 | 216 |
| 2025-03-31 | ICICI Prudential MF | 880000.0 | 216 |
| 2025-12-31 | ICICI Prudential MF | 1074000.0 | 216 |
| 2022-03-31 | Kotak Mahindra MF | 270000.0 | 168 |
| 2022-09-30 | Kotak Mahindra MF | 272000.0 | 168 |
| 2023-03-31 | Kotak Mahindra MF | 289000.0 | 168 |
| 2023-09-30 | Kotak Mahindra MF | 325000.0 | 168 |
| 2024-03-31 | Kotak Mahindra MF | 380000.0 | 168 |
| 2024-09-30 | Kotak Mahindra MF | 405000.0 | 168 |
| 2024-12-31 | Kotak Mahindra MF | 489000.0 | 168 |
| 2025-03-31 | Kotak Mahindra MF | 492000.0 | 168 |
| 2025-12-31 | Kotak Mahindra MF | 580000.0 | 168 |
| 2022-03-31 | Mirae Asset MF | 105000.0 | 56 |
| 2022-09-30 | Mirae Asset MF | 108000.0 | 56 |
| 2023-03-31 | Mirae Asset MF | 116000.0 | 56 |
| 2023-09-30 | Mirae Asset MF | 142000.0 | 56 |
| 2024-03-31 | Mirae Asset MF | 175000.0 | 56 |
| 2024-09-30 | Mirae Asset MF | 190000.0 | 56 |
| 2024-12-31 | Mirae Asset MF | 210000.0 | 56 |
| 2025-03-31 | Mirae Asset MF | 225000.0 | 56 |
| 2025-12-31 | Mirae Asset MF | 290000.0 | 56 |
| 2022-03-31 | Nippon India MF | 270000.0 | 177 |
| 2022-09-30 | Nippon India MF | 278000.0 | 177 |
| 2023-03-31 | Nippon India MF | 293000.0 | 177 |
| 2023-09-30 | Nippon India MF | 340000.0 | 177 |
| 2024-03-31 | Nippon India MF | 430000.0 | 177 |
| 2024-09-30 | Nippon India MF | 468000.0 | 177 |
| 2024-12-31 | Nippon India MF | 570000.0 | 177 |
| 2025-03-31 | Nippon India MF | 560000.0 | 177 |
| 2025-12-31 | Nippon India MF | 700000.0 | 177 |
| 2022-03-31 | SBI Mutual Fund | 605000.0 | 186 |
| 2022-09-30 | SBI Mutual Fund | 630000.0 | 186 |
| 2023-03-31 | SBI Mutual Fund | 717000.0 | 186 |
| 2023-09-30 | SBI Mutual Fund | 845000.0 | 186 |
| 2024-03-31 | SBI Mutual Fund | 1000000.0 | 186 |
| 2024-09-30 | SBI Mutual Fund | 1080000.0 | 186 |
| 2024-12-31 | SBI Mutual Fund | 1114000.0 | 186 |
| 2025-03-31 | SBI Mutual Fund | 1250000.0 | 186 |
| 2025-12-31 | SBI Mutual Fund | 1250000.0 | 186 |
| 2022-03-31 | UTI Mutual Fund | 230000.0 | 142 |
| 2022-09-30 | UTI Mutual Fund | 232000.0 | 142 |
| 2023-03-31 | UTI Mutual Fund | 239000.0 | 142 |
| 2023-09-30 | UTI Mutual Fund | 265000.0 | 142 |
| 2024-03-31 | UTI Mutual Fund | 290000.0 | 142 |
| 2024-09-30 | UTI Mutual Fund | 308000.0 | 142 |
| 2024-12-31 | UTI Mutual Fund | 352000.0 | 142 |
| 2025-03-31 | UTI Mutual Fund | 355000.0 | 142 |
| 2025-12-31 | UTI Mutual Fund | 410000.0 | 142 |

---

