# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
shopping_behavior_updated = dataiku.Dataset("shopping_behavior_updated")
shopping_behavior_updated_df = shopping_behavior_updated.get_dataframe()


# Compute recipe outputs from inputs
# We group by Category to see the average Review Rating and total Spend
py_shopping_df = shopping_behavior_updated_df.groupby("Category").agg({
    "Review Rating": "mean",
    "Purchase Amount (USD)": "sum",
    "Customer ID": "count"
}).reset_index()

# Rename columns to be more descriptive for the output dataset
py_shopping_df.columns = ["Category", "Avg_Review_Rating", "Total_Sales_USD", "Customer_Count"]


# Write recipe outputs
py_shopping = dataiku.Dataset("py_shopping")
py_shopping.write_with_schema(py_shopping_df)
