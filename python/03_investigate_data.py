import pandas as pd

categories = pd.read_csv("../data/raw/categories.csv")
shipments = pd.read_csv("../data/raw/shipments.csv")
orders = pd.read_csv("../data/raw/orders.csv")

print("/n=========Categories=========")
print(categories.to_string(index=False))

print("/n=========Shipment Status=========")
print(shipments["status"].value_counts())

print("/n=========Missing Delivery dates by Status=========")
missing_delivery = shipments["delivery_date"].isnull()
print(shipments.loc[missing_delivery, "status"].value_counts())

print("\n=========Order Date Sample=========")
print(orders["order_date"].head(10))