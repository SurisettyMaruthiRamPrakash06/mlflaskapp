#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the dataset
df = pd.read_csv("C:\ADWS\dataset.csv")

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Print basic statistics
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Calculate total sales for each region
total_sales_region = df.groupby("Region")["Sales"].sum()
print("\nTotal sales for each region:")
print(total_sales_region)

# Find the most sold product (based on quantity)
most_sold_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("\nMost sold product:", most_sold_product)

# Compute the average profit margin for each product
df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100
avg_profit_margin = df.groupby("Product")["Profit Margin"].mean()
print("\nAverage profit margin for each product:")
print(avg_profit_margin)

