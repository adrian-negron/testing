# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
shopping_behavior_updated = dataiku.Dataset("shopping_behavior_updated")
shopping_behavior_updated_df = shopping_behavior_updated.get_dataframe()


# Compute recipe outputs from inputs
# We group by Category to see metrics and added a new 'Percentage of Total' calculation
py_shopping_df = shopping_behavior_updated_df.groupby("Category").agg({
    "Review Rating": "mean",
    "Purchase Amount (USD)": "sum",
    "Customer ID": "count"
}).reset_index()

# NEW CHANGE FOR MERGE TEST: Calculate the % of total transactions per category
total_transactions = py_shopping_df["Customer ID"].sum()
py_shopping_df["Transaction_Volume_Pct"] = (py_shopping_df["Customer ID"] / total_transactions) * 100

# Rename columns to be more descriptive for the output dataset
py_shopping_df.columns = ["Category", "Avg_Review_Rating", "Total_Sales_USD", "Customer_Count", "Transaction_Volume_Pct"]


# Write recipe outputs
py_shopping = dataiku.Dataset("py_shopping")
py_shopping.write_with_schema(py_shopping_df)