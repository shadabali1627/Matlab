# Correlation matrix
correlation_matrix = data.corr()

# Trending analysis (e.g., sales over time)
sales_trend = data.groupby(data['Date'].dt.to_period('M'))['Sales_Amount'].sum()

print("Correlation Matrix:\n", correlation_matrix)
print("Sales Trend:\n", sales_trend)
