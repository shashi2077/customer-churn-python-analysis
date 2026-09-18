# Customer Churn Analysis with Python

## Project Overview

This project analyzes **800 synthetic customer records** using Python and Pandas to understand churn patterns across contract type, tenure, support tickets, satisfaction, payment behavior and monthly charges.

## Tools

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Exploratory Data Analysis (EDA)
- Data segmentation and aggregation

## Dataset

The dataset contains:

- **800 customers**
- Contract type
- Tenure
- Internet service
- Support-ticket count
- Satisfaction score
- Monthly charges
- Monthly usage
- AutoPay status
- Payment method
- Churn flag

The dataset is synthetic. No real customer, employer or client data is used.

## Main Result

Overall churn rate: **24.5%**

The analysis compares churn across customer segments rather than building a predictive model.

## Repository Structure

```text
customer-churn-python-analysis/
├── README.md
├── DATA_DICTIONARY.md
├── FINDINGS.md
├── analysis.py
├── customer_churn_analysis.ipynb
├── requirements.txt
└── data/
    └── customer_churn.csv
```

## Analysis Steps

1. Load the CSV dataset with Pandas.
2. Check row count, missing values and duplicates.
3. Calculate overall churn rate.
4. Compare churn by contract type.
5. Create tenure bands and compare churn.
6. Segment customers by support-ticket count.
7. Compare churn by satisfaction score.
8. Compare AutoPay groups.
9. Plot the main churn-rate comparisons.

## Python Techniques Used

- `read_csv()`
- `isna()`
- `duplicated()`
- `groupby()`
- `mean()`
- `sort_values()`
- `pd.cut()`
- Pandas method chaining
- Matplotlib bar charts

## Files

- [Python Script](analysis.py)
- [Jupyter Notebook](customer_churn_analysis.ipynb)
- [Dataset](data/customer_churn.csv)
- [Data Dictionary](DATA_DICTIONARY.md)
- [Analysis Findings](FINDINGS.md)

## Scope

This project is an exploratory churn analysis. It does **not** include machine-learning churn prediction or claim causal relationships.
