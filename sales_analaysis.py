import pandas as pd
import matplotlib.pyplot as plt

# Load Excel dataset
df = pd.read_excel("sales_data_sample.xlsx")
print("Dataset loaded successfully!")

# First 5 rows
print("\n========== FIRST 5 ROWS ==========")
print(df.head())

# Dataset shape
print("\n========== DATASET SHAPE ==========")
print(df.shape)

# Column names
print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Sales statistics
print("\n========== SALES STATISTICS ==========")

print("Total Sales   :", df["SALES"].sum())
print("Average Sales :", df["SALES"].mean())
print("Maximum Sales :", df["SALES"].max())
print("Minimum Sales :", df["SALES"].min())

# Product line sales
product_sales = df.groupby("PRODUCTLINE")["SALES"].sum()
product_sales = product_sales.sort_values(ascending=False)

print("\n========== SALES BY PRODUCT LINE ==========")
print(product_sales)

# Top 5
print("\n========== TOP 5 PRODUCT LINES ==========")
print(product_sales.head(5))

# Bar chart
plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")

plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("sales_by_product.png")
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
product_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales Distribution by Product Line")
plt.ylabel("")
plt.tight_layout()

plt.savefig("sales_distribution.png")
plt.show()

# Country sales
country_sales = df.groupby("COUNTRY")["SALES"].sum()
country_sales = country_sales.sort_values(ascending=False)

print("\n========== TOP 5 COUNTRIES ==========")
print(country_sales.head(5))

# Country chart
plt.figure(figsize=(12, 6))
country_sales.head(10).plot(kind="bar")

plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_countries.png")
plt.show()

print("\n================================")
print("       PROJECT COMPLETED!")
print("================================")