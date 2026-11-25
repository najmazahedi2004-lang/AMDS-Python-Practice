sales = [
    {"product": "Pen", "quantity": 3, "price": 15},
    {"product": "Book", "quantity": 2, "price": 120},
    {"product": "Pen", "quantity": 5, "price": 15},
    {"product": "Bag", "quantity": 1, "price": 850},
    {"product": "Book", "quantity": -1, "price": 120},
    {"product": "Ruler", "quantity": 4, "price": 20}
]

revenue = {}
total_revenue = 0
high_revenue = []
invalid = 0

for record in sales:
    product = record["product"]
    quantity = record["quantity"]
    price = record["price"]

    if quantity <= 0 or price < 0:
        invalid += 1
        continue

    amount = quantity * price

    revenue[product] = revenue.get(product, 0) + amount
    total_revenue += amount

    if amount >= 200:
        high_revenue.append(record)

print("Revenue by product:", revenue)
print("Total revenue: Tk", total_revenue)

best_product = max(revenue, key=revenue.get)
print("Highest revenue product:", best_product)

print("Transactions with revenue >= Tk 200:", high_revenue)
print("Invalid records:", invalid)
