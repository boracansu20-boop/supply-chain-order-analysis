import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("orders.csv")

# Convert date column to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create revenue column
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Key Performance Indicators
total_quantity = df["Quantity"].sum()
total_revenue = df["Revenue"].sum()
average_delivery_days = df["Delivery_Days"].mean()

# Best-selling product
product_sales = df.groupby("Product")["Quantity"].sum()
best_selling_product = product_sales.idxmax()
best_selling_quantity = product_sales.max()

# Delayed orders
delayed_orders = df[df["Status"] == "Delayed"]
number_of_delayed_orders = len(delayed_orders)
delayed_rate = (number_of_delayed_orders / len(df)) * 100

# Print KPI results
print("=== SUPPLY CHAIN ORDER ANALYSIS ===")
print(f"Total Products Sold: {total_quantity}")
print(f"Total Revenue: €{total_revenue:,.2f}")
print(f"Best Selling Product: {best_selling_product}")
print(f"Units Sold: {best_selling_quantity}")
print(f"Average Delivery Time: {average_delivery_days:.2f} days")
print(f"Delayed Order Rate: {delayed_rate:.2f}%")

# Revenue by Category
category_revenue = df.groupby("Category")["Revenue"].sum()

print("\nRevenue by Category:")
print(category_revenue)

category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_revenue.png")
plt.show()

# Monthly Revenue Trend
df["Month"] = df["Order_Date"].dt.month_name()

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August"
]

monthly_revenue = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reindex(month_order)
)

print("\nMonthly Revenue:")
print(monthly_revenue)

monthly_revenue.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()
