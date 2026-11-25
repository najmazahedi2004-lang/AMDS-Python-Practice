prices = {
    "rice": 75,
    "oil": 185,
    "sugar": 120,
    "milk": 95,
    "egg": 12,
    "flour": 65,
    "salt": 40,
    "lentil": 130,
    "potato": 45,
    "onion": 80,
    "tea": 250,
    "coffee": 450,
    "biscuit": 50,
    "soap": 70,
    "shampoo": 180
}

DISCOUNT_LIMIT = 1000
DISCOUNT_RATE = 0.05
VAT_RATE = 0.02

print("=" * 36)
print("      AVAILABLE PRODUCTS")
print("=" * 36)
print(f"{'Product':<20}{'Unit Price (Tk)':>16}")
print("-" * 36)
for product, unit_price in prices.items():
    print(f"{product:<20}{unit_price:>16.2f}")
print("=" * 36)
print()

order = {}

while True:
    try:
        number_of_entries = int(input("How many order entries? "))
        if number_of_entries > 0:
            break
        print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

for entry_number in range(1, number_of_entries + 1):
    item = input(f"Enter product {entry_number}: ").strip().lower()

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Entry ignored.")
        continue

    if item not in prices:
        print(f"{item} is not available.")
        continue

    if quantity <= 0:
        print("Quantity must be positive. Entry ignored.")
        continue

    order[item] = order.get(item, 0) + quantity

print()
print("Final order:")
print(order)
print()

if not order:
    print("No valid items were ordered. No bill generated.")
else:
    bill = {}
    for item, quantity in order.items():
        unit_price = prices[item]
        bill[item] = {
            "quantity": quantity,
            "unit_price": unit_price,
            "total": quantity * unit_price
        }

    subtotal = 0
    for details in bill.values():
        subtotal += details["total"]

    if subtotal >= DISCOUNT_LIMIT:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0

    vat = VAT_RATE * (subtotal - discount)
    final_amount = subtotal - discount + vat

    line_width = 52
    print("=" * 16 + " GROCERY SHOP BILL " + "=" * 16)
    print()
    print(f"{'Item':<16}{'Quantity':>8}{'Unit Price':>14}{'Total':>14}")
    print("-" * line_width)

    for item, details in bill.items():
        print(f"{item:<16}{details['quantity']:>8}"
              f"{details['unit_price']:>14.2f}{details['total']:>14.2f}")

    print("-" * line_width)
    print(f"{'Subtotal:':<38}Tk {subtotal:>8.2f}")
    print(f"{'Discount (5%):':<38}Tk {discount:>8.2f}")
    print(f"{'VAT (2%):':<38}Tk {vat:>8.2f}")
    print("-" * line_width)
    print(f"{'Final amount:':<38}Tk {final_amount:>8.2f}")
    print("=" * line_width)
