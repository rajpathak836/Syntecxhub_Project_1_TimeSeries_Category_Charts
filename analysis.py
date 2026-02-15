import pandas as pd
import matplotlib.pyplot as plt

print("🚀 Starting Project-1: Time Series & Category Charts")

# Load data
df = pd.read_csv("sales_data.csv")
df['date'] = pd.to_datetime(df['date'])

print("✅ Data loaded successfully")
print(f"📊 Total records: {len(df)}")

# Monthly aggregation
monthly_sales = df.groupby(pd.Grouper(key='date', freq='ME'))['sales'].sum()
print("📈 Monthly aggregation completed")

plt.figure()
monthly_sales.plot(title="Monthly Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Category bar chart
category_sales = df.groupby('category')['sales'].sum()
print("📊 Category-wise aggregation completed")

plt.figure()
category_sales.plot(kind='bar', title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# Pie chart
plt.figure()
category_sales.plot(kind='pie', autopct='%1.1f%%', title="Category Share")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_share.png")
plt.show()

print("✅ All charts generated successfully")
print("📁 Output files saved in current folder")
