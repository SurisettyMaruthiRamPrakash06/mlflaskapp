#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\ADWS\Day_8_sales_data.csv")

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

# --- Data Filtering ---

# Extract rows where Sales > 1000
high_sales_df = df[df["Sales"] > 1000]
print("\nRows where Sales > 1000:")
print(high_sales_df)

# Find all sales records for a specific region (e.g., "East")
region_sales_df = df[df["Region"] == "East"]
print("\nSales records for the East region:")
print(region_sales_df)

# --- Data Processing ---

# Add a new column, Profit_Per_Unit
df["Profit_Per_Unit"] = df["Profit"] / df["Quantity"]

# Create a column, High_Sales, labeling rows as "Yes" if Sales > 1000, else "No"
df["High_Sales"] = df["Sales"].apply(lambda x: "Yes" if x > 1000 else "No")

print("\nDataset after adding new columns:")
print(df.head())

