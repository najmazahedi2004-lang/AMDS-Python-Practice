products = {
    "rice": 75,
    "milk": 90,
    "bread": 55,
    "egg": 15,
    "apple": 180,
    "oil": 190,
    "sugar": 130,
    "salt": 45,
    "soap": 60,
    "tea": 220
}

print("Available Products:")
for product, price in products.items():
    print(product, ":", price)

orders = {}

while True:
    name = input("\nEnter product name (or 'done' to finish): ").lower()

    if name == "done":
        break

    if name not in products:
        print("Product not available")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity. Please enter a positive quantity.")
        continue

    if name in orders:
        orders[name] = orders[name] + quantity
    else:
        orders[name] = quantity

print("\nItemised Bill")
print("---------------------------------------------")
print("Product\t\tUnit Price\tQuantity\tItem Total")
print("---------------------------------------------")

grand_total = 0

for name, quantity in orders.items():
    price = products[name]
    item_total = price * quantity
    grand_total = grand_total + item_total

    print(name, "\t\t", price, "\t\t", quantity, "\t\t", item_total)

print("---------------------------------------------")
print("Grand Total:", grand_total)
