# Notebooks

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://justicetefera.github.io/datafun-04-notebooks/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: exploratory data analysis with Jupyter notebooks.

# Sales Data Exploratory Analysis

This project performs a complete exploratory data analysis (EDA) on a retail sales dataset.
It includes data cleaning, aggregation, visualization, insights, and business recommendations.

## Key Features
- Data cleaning with type correction and invalid value handling
- Aggregations (store-level, product-level, monthly sales)
- Visualizations saved to `docs/images/`
- Correlation heatmap
- Regression-based scatterplots
- Insights and business recommendations
- Full logging to `project.log` for traceability

## Project Structure
project/
│
├── data/
│   └── sales_data.csv
│
├── docs/
│   └── images/
│       ├── correlation_heatmap.png
│       ├── total_sales_by_store.png
│       ├── distribution_saleamount.png
│       ├── saleamount_vs_productid.png
│       └── saleamount_vs_storeid.png
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── src/
│   └── datafun/
│       ├── __init__.py
│       ├── data_cleaning.py
│       ├── visualizations.py
│       └── analysis_utils.py
│
├── project.log
├── pyproject.toml
├── README.md
└── LICENSE


## This Project

This project provides a complete **Exploratory Data Analysis (EDA)** workflow for a retail sales dataset.
It demonstrates how to understand a new dataset quickly and professionally by combining narrative explanation, Python code, and visual analytics inside a Jupyter notebook.

The analysis includes structured data validation, descriptive statistics, grouped summaries, and multiple visualizations that reveal patterns in store performance, product behavior, and transaction values.
All generated figures are saved to `docs/images/`, and every major step is recorded in `project.log` to ensure transparency and reproducibility.

The project also delivers clear insights and business recommendations based on observed trends, making it useful not only as a technical example but also as a practical decision‑support tool.
Overall, it serves as a model for how to explore, document, and communicate findings from tabular data in a professional analytics environment.



## Example Output

2026-05-31 08:13:42,024 INFO ***** Notebook Execution Started Successfully *****
2026-05-31 08:13:42,149 INFO Notebook execution started.
2026-05-31 08:13:42,152 INFO Imported pandas, seaborn, matplotlib, and set visualization theme.
2026-05-31 08:13:42,183 INFO Notebook execution started.
2026-05-31 08:13:42,185 INFO Imported pandas, seaborn, matplotlib, and set visualization theme.
2026-05-31 08:13:42,226 INFO Loaded dataset from ../data/raw/sales_data.csv
2026-05-31 08:13:42,265 INFO Inspected DataFrame structure: shape, columns, dtypes, missing values, info, and preview.
2026-05-31 08:13:42,313 INFO Cleaned dataset: converted SaleAmount to numeric, fixed CampaignID blanks, standardized CampaignID type, and converted SaleDate to datetime.
2026-05-31 08:13:42,381 INFO Computed total sales by store using groupby and sorted results.
2026-05-31 08:13:42,414 INFO Computed average sale amount by product using groupby and sorted results.
2026-05-31 08:13:42,453 INFO Computed total sales by month: extracted SaleMonth period and aggregated SaleAmount.
2026-05-31 08:13:42,530 INFO Computed numeric-only correlation matrix for the dataset.
2026-05-31 08:13:43,140 INFO Generated and saved correlation_heatmap.png
2026-05-31 08:13:43,314 INFO Using categorical units to plot a list of strings that are all parsable as floats or dates. If these strings should be plotted as numbers, cast to the appropriate data type before plotting.
2026-05-31 08:13:43,328 INFO Using categorical units to plot a list of strings that are all parsable as floats or dates. If these strings should be plotted as numbers, cast to the appropriate data type before plotting.
2026-05-31 08:13:43,585 INFO Generated and saved total_sales_by_store.png
2026-05-31 08:13:44,100 INFO Generated and saved distribution_saleamount.png
2026-05-31 08:13:44,810 INFO Generated and saved saleamount_vs_productid.png
2026-05-31 08:13:45,491 INFO Generated and saved saleamount_vs_storeid.png
2026-05-31 08:13:45,624 INFO Printed final insights and conclusions for the analysis.
2026-05-31 08:13:45,659 INFO Added final summary markdown section to the notebook.
2026-05-31 08:13:45,694 INFO Added business recommendations markdown section to the notebook.
2026-05-31 08:13:45,728 INFO ***** Notebook Executed Successfully *****

## Visualizations

### 🔹 Correlation Heatmap
![Correlation Heatmap](notebooks/docs/correlation_heatmap.png)

### 🔹 Distribution of SaleAmount
![Distribution of SaleAmount](notebooks/docs/distribution_saleamount.png)

### 🔹 SaleAmount vs ProductID
![SaleAmount vs ProductID](notebooks/docs/saleamount_vs_productid.png)
