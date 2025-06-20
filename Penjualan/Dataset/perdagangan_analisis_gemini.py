# -*- coding: utf-8 -*-
"""Perdagangan Analisis Gemini

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QJBGQRvDiymFVSw9HuZ4hGCYCjV_H15_

# Task
berdasarkan dataset perdagangan yang berisi tentang ketiga tabel ini, buat beberapa data analitik sederhana lengkap dengan kode dan visualisasi hasil grafiknya dengan menarik dan 3D (data-code-grafik)

Here is all the data you need:
"inventory.csv"
"production.csv"
"sales.csv"

## Data loading

### Subtask:
Load the three datasets ("inventory.csv", "production.csv", and "sales.csv") into pandas DataFrames.

**Reasoning**:
Import pandas and load the three datasets into DataFrames as instructed.
"""

import pandas as pd

df_inventory = pd.read_csv('inventory.csv')
df_production = pd.read_csv('production.csv')
df_sales = pd.read_csv('sales.csv')

print("Inventory DataFrame head:")
display(df_inventory.head())

print("\nProduction DataFrame head:")
display(df_production.head())

print("\nSales DataFrame head:")
display(df_sales.head())

"""## Data exploration

### Subtask:
Explore the datasets to understand their structure, columns, and data types.

**Reasoning**:
Use the `.info()`, `.describe()`, `.columns`, and `.shape` methods/attributes to explore the structure, data types, and basic statistics of each DataFrame as per the instructions.
"""

print("Inventory DataFrame Info:")
df_inventory.info()
print("\nInventory DataFrame Description:")
display(df_inventory.describe())
print("\nInventory DataFrame Columns:")
print(df_inventory.columns)
print("\nInventory DataFrame Shape:")
print(df_inventory.shape)

print("\nProduction DataFrame Info:")
df_production.info()
print("\nProduction DataFrame Description:")
display(df_production.describe())
print("\nProduction DataFrame Columns:")
print(df_production.columns)
print("\nProduction DataFrame Shape:")
print(df_production.shape)

print("\nSales DataFrame Info:")
df_sales.info()
print("\nSales DataFrame Description:")
display(df_sales.describe())
print("\nSales DataFrame Columns:")
print(df_sales.columns)
print("\nSales DataFrame Shape:")
print(df_sales.shape)

"""## Data wrangling

### Subtask:
Merge the relevant datasets based on common columns to create a unified dataset for analysis.

**Reasoning**:
Merge the production and sales dataframes, then merge the result with the inventory dataframe to create a unified dataset. Finally, display the head of the merged dataframe.
"""

df_merged = pd.merge(df_production, df_sales, on=['product_id', 'product_name'], how='inner')
df_merged = pd.merge(df_merged, df_inventory, on=['product_id', 'product_name'], how='inner')
display(df_merged.head())

"""## Data analysis

### Subtask:
Perform simple data analytics on the merged dataset, such as calculating total inventory, production, and sales, and potentially analyzing trends or relationships between them.

**Reasoning**:
Calculate the total quantity for inventory, production, and sales, total revenue, total production cost, and profit from the merged dataframe as requested in the instructions and print the results.
"""

total_inventory = df_merged['stock_quantity'].sum()
total_production = df_merged['quantity_produced'].sum()
total_sales_quantity = df_merged['quantity_sold'].sum()

total_revenue = (df_merged['quantity_sold'] * df_merged['sale_price']).sum()
total_production_cost = (df_merged['quantity_produced'] * df_merged['production_cost']).sum()

profit = total_revenue - total_production_cost

print(f"Total Inventory: {total_inventory}")
print(f"Total Production: {total_production}")
print(f"Total Sales Quantity: {total_sales_quantity}")
print(f"Total Revenue: {total_revenue:.2f}")
print(f"Total Production Cost: {total_production_cost:.2f}")
print(f"Profit: {profit:.2f}")

"""## Data visualization

### Subtask:
Create compelling 3D visualizations to represent the results of the data analysis.

**Reasoning**:
Import the necessary libraries for 3D plotting.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

"""**Reasoning**:
Create a 3D bar chart to visualize total inventory, production, and sales quantities, and add labels, titles, and legends.


"""

# Aggregate the total quantities
total_inventory = df_merged['stock_quantity'].sum()
total_production = df_merged['quantity_produced'].sum()
total_sales_quantity = df_merged['quantity_sold'].sum()

# Create the data for the 3D bar chart
categories = ['Inventory', 'Production', 'Sales']
quantities = [total_inventory, total_production, total_sales_quantity]
x_pos = np.arange(len(categories))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D bars
# Use a constant y value (0) for simplicity for a 2D-like comparison in 3D space
# and vary the z value for the height of the bars.
ax.bar(x_pos, [0] * len(categories), quantities, zdir='y', color=['skyblue', 'lightgreen', 'salmon'], alpha=0.8)

# Set labels and title
ax.set_xlabel('Category')
ax.set_ylabel('') # No y-label as all bars are at y=0
ax.set_zlabel('Total Quantity')
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_title('Total Inventory, Production, and Sales Quantities (3D)')

# Add legend (manual approach since zdir='y' makes auto-legend tricky)
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='skyblue', label='Inventory'),
                   Patch(facecolor='lightgreen', label='Production'),
                   Patch(facecolor='salmon', label='Sales')]
ax.legend(handles=legend_elements)

plt.show()

"""**Reasoning**:
Create a 3D scatter plot to visualize the relationship between production cost, sale price, and profit, and add labels, titles, and legends. Calculate profit for each row before plotting.


"""

# Calculate profit for each row
df_merged['profit_per_unit'] = df_merged['sale_price'] - df_merged['production_cost']
df_merged['total_profit'] = df_merged['profit_per_unit'] * df_merged['quantity_sold']

# Prepare data for 3D scatter plot
# We can group by product to see the relationship per product
df_product_summary = df_merged.groupby('product_name').agg(
    avg_production_cost=('production_cost', 'mean'),
    avg_sale_price=('sale_price', 'mean'),
    total_profit=('total_profit', 'sum')
).reset_index()

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create the 3D scatter plot
scatter = ax.scatter(df_product_summary['avg_production_cost'],
                     df_product_summary['avg_sale_price'],
                     df_product_summary['total_profit'],
                     c=df_product_summary['total_profit'],  # Use profit for color mapping
                     cmap='viridis', # Colormap
                     s=df_product_summary['total_profit'].abs() / 10) # Use absolute profit for size

# Set labels and title
ax.set_xlabel('Average Production Cost')
ax.set_ylabel('Average Sale Price')
ax.set_zlabel('Total Profit')
ax.set_title('Relationship between Production Cost, Sale Price, and Total Profit by Product (3D)')

# Add color bar for profit
cbar = fig.colorbar(scatter, pad=0.1)
cbar.set_label('Total Profit')

# Add product names as annotations (optional, can make plot cluttered with many points)
# for i, row in df_product_summary.iterrows():
#     ax.text(row['avg_production_cost'], row['avg_sale_price'], row['total_profit'], row['product_name'])

plt.show()

"""## Summary:

### Data Analysis Key Findings

*   The total inventory across all products is 155 units.
*   The total quantity produced across all products is 160 units.
*   The total quantity sold across all products is 145 units.
*   The total revenue generated from sales is \$1585.00.
*   The total production cost for the produced items is \$810.00.
*   The overall profit calculated is \$775.00.
*   A 3D bar chart visually represents the total quantities of inventory, production, and sales, showing that production quantity is slightly higher than sales quantity, and both are close to the current inventory level.
*   A 3D scatter plot shows the relationship between average production cost, average sale price, and total profit for each product. Products with higher average sale prices relative to their production costs tend to have higher total profits, as indicated by the color and size of the points in the scatter plot.

### Insights or Next Steps

*   The current inventory levels seem manageable relative to production and sales quantities, but monitoring the difference between production and sales over time is crucial to avoid overstocking or shortages.
*   Further analysis could investigate which specific products contribute most significantly to the total profit and analyze their individual production costs and sale prices to optimize pricing strategies or production efficiency.

"""