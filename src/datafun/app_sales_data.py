"""
app_sales_data.py
Author: Justice Tefera
Purpose: Run a complete EDA workflow on the sales_data.csv dataset.
"""

import logging
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

logging.basicConfig(
    filename="project.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("=== Sales Data EDA Script Started ===")

sns.set_theme(style="whitegrid")

# Ensure output folder exists
os.makedirs("docs/images", exist_ok=True)

# -----------------------------------------------------------------------------
# Load Data
# -----------------------------------------------------------------------------

DATA_PATH = "data/raw/sales_data.csv"

logging.info(f"Loading dataset from {DATA_PATH}")
df = pd.read_csv(DATA_PATH)

logging.info(f"Loaded dataset with shape: {df.shape}")

# -----------------------------------------------------------------------------
# Clean Data
# -----------------------------------------------------------------------------

logging.info("Cleaning dataset...")

# Convert SaleAmount to numeric
df["SaleAmount"] = pd.to_numeric(df["SaleAmount"], errors="coerce")

# Clean CampaignID
df["CampaignID"] = df["CampaignID"].replace("", pd.NA)
df["CampaignID"] = pd.to_numeric(df["CampaignID"], errors="coerce").astype("Int64")

# Convert SaleDate to datetime
df["SaleDate"] = pd.to_datetime(df["SaleDate"], errors="coerce")

logging.info("Data cleaning complete.")
logging.info(f"Updated dtypes:\n{df.dtypes}")

# -----------------------------------------------------------------------------
# Summary Statistics
# -----------------------------------------------------------------------------

logging.info("Computing summary statistics...")

stats = df.describe(include="all")
logging.info(f"Summary statistics:\n{stats}")

# -----------------------------------------------------------------------------
# Grouped Summaries
# -----------------------------------------------------------------------------

logging.info("Computing grouped summaries...")

sales_by_store = df.groupby("StoreID")["SaleAmount"].sum().sort_values(ascending=False)
avg_sale_by_product = (
    df.groupby("ProductID")["SaleAmount"].mean().sort_values(ascending=False)
)

logging.info("Grouped summaries computed successfully.")

# -----------------------------------------------------------------------------
# Visualizations
# -----------------------------------------------------------------------------

logging.info("Generating visualizations...")

# Correlation Matrix
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.savefig("docs/images/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# Total Sales by Store
plt.figure(figsize=(10, 5))
sns.barplot(x=sales_by_store.index, y=sales_by_store.values, palette="Blues_d")
plt.title("Total Sales by Store")
plt.xlabel("Store ID")
plt.ylabel("Total Sales")
plt.savefig("docs/images/total_sales_by_store.png", dpi=300, bbox_inches="tight")
plt.close()

# Distribution of Sale Amounts
plt.figure(figsize=(10, 5))
sns.histplot(df["SaleAmount"], kde=True, bins=30, color="purple")
plt.title("Distribution of Sale Amounts")
plt.xlabel("Sale Amount")
plt.ylabel("Frequency")
plt.savefig("docs/images/distribution_saleamount.png", dpi=300, bbox_inches="tight")
plt.close()

# Scatterplot: SaleAmount vs ProductID
plt.figure(figsize=(8, 5))
sns.regplot(x="ProductID", y="SaleAmount", data=df, scatter_kws={"alpha": 0.5})
plt.title("SaleAmount vs ProductID (Regression Line)")
plt.xlabel("Product ID")
plt.ylabel("Sale Amount")
plt.savefig("docs/images/saleamount_vs_productid.png", dpi=300, bbox_inches="tight")
plt.close()

# Scatterplot: SaleAmount vs StoreID
plt.figure(figsize=(8, 5))
sns.regplot(
    x="StoreID", y="SaleAmount", data=df, scatter_kws={"alpha": 0.5}, color="green"
)
plt.title("SaleAmount vs StoreID (Regression Line)")
plt.xlabel("Store ID")
plt.ylabel("Sale Amount")
plt.savefig("docs/images/saleamount_vs_storeid.png", dpi=300, bbox_inches="tight")
plt.close()

logging.info("All visualizations generated and saved.")

# -----------------------------------------------------------------------------
# Final Summary
# -----------------------------------------------------------------------------

logging.info("=== Sales Data EDA Script Completed Successfully ===")

print(
    "Sales Data EDA complete. Check docs/images/ for charts and project.log for details."
)
