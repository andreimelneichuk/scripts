import csv
import json

products = {}
with open("products.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        products[row['product_id']] = row['product_name']

with open("sales.json", "r") as json_file:
    sales_data = json.load(json_file)

sales_summary = {}
for sale in sales_data:
    product_id = sale['product_id']
    amount = sale['amount']
    
    if product_id in products:
        product_name = products[product_id]
        if product_name in sales_summary:
            sales_summary[product_name] += amount
        else:
            sales_summary[product_name] = amount

for product_name, total_sales in sales_summary.items():
    print(f"Product: {product_name}, Total Sales: {total_sales}")