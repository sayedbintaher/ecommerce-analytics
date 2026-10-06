import pandas as pd

customers = pd.read_csv("../data/raw/customers.csv")
categories = pd.read_csv("../data/raw/categories.csv")
products = pd.read_csv("../data/raw/products.csv")
orders = pd.read_csv("../data/raw/orders.csv")
order_items = pd.read_csv("../data/raw/order_items.csv")
payments = pd.read_csv("../data/raw/payments.csv")
shipments = pd.read_csv("../data/raw/shipments.csv")

print("All datasets loaded successfully!")

print("\n========= Missing values =========")
print("\nCustomers")
print(customers.isnull().sum())

print("\nCategories")
print(categories.isnull().sum())

print("\nProducts")
print(products.isnull().sum())

print("\nOrders")
print(orders.isnull().sum())

print("\nOrder Items")
print(order_items.isnull().sum())

print("\nPayments")
print(payments.isnull().sum())

print("\nShipments")
print(shipments.isnull().sum())

print("\n=========Duplicates=========")

print("\nCustomers:", customers.duplicated().sum())
print("\nProducts:", products.duplicated().sum())
print("\nCategories:", categories.duplicated().sum())
print("\nOrders:",orders.duplicated().sum())
print("\nOrder Items:",order_items.duplicated().sum())
print("\nPayments:",payments.duplicated().sum())
print("\nShipments:",shipments.duplicated().sum())

print("\n=========Data Types=========")
print("\nCustomers")
print(customers.dtypes)

print("\nOrders")
print(orders.dtypes)

print("\nOrder Items")
print(order_items.dtypes)

print("\nPayments")
print(payments.dtypes)

print("\n=========Order Status=========")
print(orders["status"].value_counts())

print("\n=========Payment Methods=========")
print(payments["payment_method"].value_counts())

print("\n=========Product Categories=========")
print(products["category_id"].value_counts())