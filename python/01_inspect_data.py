import pandas as pd

customers = pd.read_csv("../data/raw/customers.csv")
products = pd.read_csv("../data/raw/products.csv")
orders = pd.read_csv("../data/raw/orders.csv")

print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)

print("First 5 customers: ")
print(customers.head())

print("\nDataset shape: ")
print(customers.shape)

print("\nDataset info: ")
print(customers.info)

print("\nMissing values: ")
print(customers.isnull().sum())

print("\nDuplicate rows")
print(customers.duplicated().sum())