# 📌 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 📌 Load Dataset
df = pd.read_csv("data.csv", encoding='ISO-8859-1')

# 📌 Show Basic Info
print(df.head())
print(df.info())

# 📌 Data Cleaning
# Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# Remove negative or zero values
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Convert date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# 📌 EDA (Exploratory Data Analysis)

# Top 10 Products
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print(top_products)

# Top Countries
top_countries = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print(top_countries)

# Monthly Sales
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

# 📊 Plot Monthly Sales
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()