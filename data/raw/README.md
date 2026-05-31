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



## Visualizations

## Findings and Visuals

### 🔹 Correlation Heatmap

![Correlation Heatmap](notebooks/docs/correlation_heatmap.png)

### 🔹 Distribution of SaleAmount

![Distribution of SaleAmount](notebooks/docs/distribution_saleamount.png)

### 🔹 SaleAmount vs ProductID

![SaleAmount vs ProductID](notebooks/docs/saleamount_vs_productid.png)
