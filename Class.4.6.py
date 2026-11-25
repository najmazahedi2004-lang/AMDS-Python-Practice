items = ["Notebook", "Pen", "Calculator", "Folder"]
prices = [120.0, 15.0, 850.0, 80.0]
quantities = [2, 5, 1, 3]

subtotal = 0

for i in range(len(items)):
    line_total = prices[i] * quantities[i]
    subtotal += line_total

    print(items[i], ":", format(line_total, ".2f"))

if subtotal >= 1000:
    discount = subtotal * 0.10
elif subtotal >= 500:
    discount = subtotal * 0.05
else:
    discount = 0

amount_after_discount = subtotal - discount

if amount_after_discount >= 1000:
    delivery_charge = 0
else:
    delivery_charge = 60

final_total = amount_after_discount + delivery_charge

print("Subtotal:", format(subtotal, ".2f"))
print("Discount:", format(discount, ".2f"))
print("Delivery charge:", format(delivery_charge, ".2f"))
print("Final total:", format(final_total, ".2f"))