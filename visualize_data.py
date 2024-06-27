import matplotlib.pyplot as plt
import seaborn as sns

# Sales trend over time
plt.figure(figsize=(10, 6))
sales_trend.plot(kind='line')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.show()

# Top products sales
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Sales Amount')
plt.xlabel('Product')
plt.ylabel('Sales Amount')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()
