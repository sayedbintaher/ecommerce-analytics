import pandas as pd

orders = pd.read_csv("../data/cleaned/orders.csv")
order_items = pd.read_csv("../data/cleaned/order_items.csv")
products = pd.read_csv("../data/cleaned/products.csv")
categories = pd.read_csv("../data/cleaned/categories.csv")
customers = pd.read_csv("../data/cleaned/customers.csv")
payments = pd.read_csv("../data/cleaned/payments.csv")
shipments = pd.read_csv("../data/cleaned/shipments.csv")

print("Orders:", len(orders))
print("Order Items:", len(order_items))

print(orders[["order_id", "customer_id"]].head())
print(order_items[["order_id","quantity"]].head())

missing_orders = order_items[~order_items["order_id"].isin(orders["order_id"])]
print("Order items with invalid order_id:",len(missing_orders))

missing_products = order_items[~order_items["product_id"].isin(products["product_id"])]
print("Order items with invalid product_id:", len(missing_products))

missing_categories = products[~products["category_id"].isin(categories["category_id"])]
print("Products with invalid category_id:",len(missing_categories))

missing_customers = orders[~orders["customer_id"].isin(customers["customer_id"])]
print("Orders with invalid customer_id:",len(missing_customers))

missing_orders_for_payments = payments[~payments["order_id"].isin(orders["order_id"])]
print("Payments with invalid order_id:",len(missing_orders_for_payments))

missing_orders_for_shipments = shipments[~shipments["order_id"].isin(orders["order_id"])]
print("Shipments with invalid order_id",len(missing_orders_for_shipments))
