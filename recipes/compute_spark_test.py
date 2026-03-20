# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
shopping_behavior_updated = dataiku.Dataset("shopping_behavior_updated")
shopping_behavior_updated_df = dkuspark.get_dataframe(sqlContext, shopping_behavior_updated)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
spark_test_df = shopping_behavior_updated_df # For this sample code, simply copy input to output

# Write recipe outputs
spark_test = dataiku.Dataset("spark_test")
dkuspark.write_with_schema(spark_test, spark_test_df)
