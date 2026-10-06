import pandas as pd
import os

customers = pd.read_csv("../data/raw/customers.csv")
products = pd.read_csv("../data/raw/products.csv")
categories = pd.read_csv("../data/raw/categories.csv")
orders = pd.read_csv("../data/raw/orders.csv")
order_items = pd.read_csv("../data/raw/order_items.csv")
payments = pd.read_csv("../data/raw/payments.csv")
shipments = pd.read_csv("../data/raw/shipments.csv")

customers["signup_date"] = pd.to_datetime(customers["signup_date"])
orders["order_date"] = pd.to_datetime(orders["order_date"])
payments["payment_date"] = pd.to_datetime(payments["payment_date"])
shipments["ship_date"] = pd.to_datetime(shipments["ship_date"])
shipments["delivery_date"] = pd.to_datetime(shipments['delivery_date'])

print("\n=========Date Data Types =========")
print("Customer signup:",customers["signup_date"].dtype)
print("Order date:", orders["order_date"].dtype)
print("Payment date:", payments["payment_date"].dtype)
print("Ship date:",shipments["ship_date"].dtype)
print("Delivery date:", shipments["delivery_date"].dtype)

print("\n=========Numeric Data Check=========")

print("\nProducts:")
print(products[["price", "cost", "stock"]].describe())

print("\nOrder Items:")
print(order_items[["quantity", "unit_price", "total_price"]].describe())

print("\nPayments:")
print(payments[["amount"]].describe())

print("\n=========Invalid Product Prices =========")
print(products.loc[products["price"] <= 0])

print("\n=========Invalid Product Costs=========")
print(products.loc[products["cost"] < 0])

print("\n=========Invalid Stock=========")
print(products.loc[products["stock"] < 0])

calculated_total = (
    order_items["quantity"] * order_items["unit_price"]
)

print("\n=========Total Price Check=========")
price_difference = (
    order_items["total_price"] - calculated_total
)

print(price_difference.describe())

os.makedirs("../data/cleaned",exist_ok=True)

customers.to_csv("../data/cleaned/customers.csv", index=False)
products.to_csv("../data/cleaned/products.csv", index=False)
categories.to_csv("../data/cleaned/categories.csv", index=False)
orders.to_csv("../data/cleaned/orders.csv", index=False)
order_items.to_csv("../data/cleaned/order_items.csv", index=False)
payments.to_csv("../data/cleaned/payments.csv", index=False)
shipments.to_csv("../data/cleaned/shipments.csv", index=False)

print("\nCleaned datasets saved successfully")



