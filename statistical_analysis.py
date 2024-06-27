# Total sales amount
total_sales = data['Sales_Amount'].sum()

# Average sales amount
average_sales = data['Sales_Amount'].mean()

# Top product sales
top_products = data.groupby('Product')['Sales_Amount'].sum().sort_values(ascending=False).head(10)

# Summary statistics
summary_stats = data.describe()

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Top Products:\n", top_products)
print("Summary Statistics:\n", summary_stats)
