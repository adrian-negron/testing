# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
shopping_behavior_updated = dataiku.Dataset("shopping_behavior_updated")
shopping_behavior_updated_df = shopping_behavior_updated.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

dsafdsf_df = shopping_behavior_updated_df # For this sample code, simply copy input to output


# Write recipe outputs
dsafdsf = dataiku.Dataset("dsafdsf")
dsafdsf.write_with_schema(dsafdsf_df)
