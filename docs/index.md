## Custom Project

### Dataset
For this custom project, I selected a real‑world style retail dataset named **sales_data.csv**.
The dataset contains 2,001 sales transactions with fields such as TransactionID, SaleDate, CustomerID, ProductID, StoreID, CampaignID, and SaleAmount.
The dataset required cleaning due to inconsistent data types (SaleAmount stored as strings, missing CampaignID values, and date formatting issues). After cleaning, the dataset was ready for full exploratory data analysis.

---

## Phase 4: Technical Modification

As part of Phase 4, I created a new Python application script **`app_sales_data.py`**

`uv run python -m src.datafun.app_sales_data`

This script performs a complete EDA workflow outside the notebook environment.
It includes:
- Loading the dataset from `data/raw/sales_data.csv`
- Cleaning invalid values
  - SaleAmount → numeric
  - CampaignID → Int64
  - SaleDate → datetime
- Computing grouped summaries
  - Total sales by store
  - Average sale amount by product
  - Total sales by month
- Generating multiple visualizations
  - Correlation heatmap
  - Distribution of SaleAmount
  - Total sales by store (bar chart)
  - Regression plots (SaleAmount vs ProductID, SaleAmount vs StoreID)
- Automatically saving all images to: `docs/images/`

---

During Phase 4, I implemented several technical modifications to demonstrate a professional and repeatable EDA workflow:

- Converted **SaleAmount** to numeric and handled invalid entries
- Cleaned **CampaignID** by replacing blanks and converting to integer type
- Converted **SaleDate** to proper datetime format
- Added logging to track notebook execution and data processing steps
- Created grouped summaries:
  - Total sales by store
  - Average sale amount by product
  - Total sales by month
- Generated multiple visualizations and saved them to `notebooks/docs/images/`:
  - Correlation heatmap
  - Distribution of SaleAmount
  - Total sales by store (bar chart)
  - Regression scatterplots (SaleAmount vs ProductID, SaleAmount vs StoreID)

These modifications improved data quality, reproducibility, and interpretability.

---

## Phase 5: Apply the Skills to a New Dataset

In Phase 5, I applied the full EDA workflow to the cleaned dataset using both a Jupyter Notebook and the new Python script.
My notebook (`notebooks/eda_sales_data.ipynb`) and script work together to demonstrate a complete, reproducible analysis pipeline.
Key components of the custom project include:

- Setting the correct `.venv` kernel in VS Code
- Running the notebook top‑to‑bottom to ensure reproducibility
- Saving all generated charts to `notebooks/docs/images/`
- Adding a complete narrative explaining:
  - Data cleaning steps
  - Summary statistics
  - Grouped insights
  - Visual interpretations
  - Business recommendations

### Summary of Findings
- Store **404** generated the highest total sales.
- Product‑level averages varied significantly, revealing high‑value and low‑value items.
- SaleAmount distribution was right‑skewed, indicating many small purchases and fewer large ones.
- Correlation values were generally weak across numeric fields.
- Regression plots helped visualize how product and store IDs relate to sales value.

### Business Recommendations
- Focus on high‑performing stores to replicate successful practices.
- Prioritize inventory for high‑value products.
- Investigate low‑performing products for pricing or promotion opportunities.
- Expand data collection beyond a single month to enable trend analysis.
- Strengthen data validation to reduce future cleaning needs.

---

## Reflection: Analyst Insights

This project strengthened my ability to perform structured exploratory data analysis using Python, Pandas, Seaborn, and Jupyter Notebooks.
I gained experience in:

- Cleaning and preparing real‑world datasets
- Building reproducible workflows
- Automating EDA with Python scripts
- Creating meaningful visualizations
- Interpreting business‑relevant insights
- Documenting results professionally

The addition of **`app_sales_data.py`** made the workflow more robust and reusable, and the automatic generation of images and logs improved traceability and organization. This process highlighted the importance of data quality, clear narrative, and visual storytelling in analytics.
