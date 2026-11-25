delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}

combined = {}

for product in delivery_1:
    combined[product] = delivery_1[product]

for product in delivery_2:
    combined[product] = combined.get(product, 0) + delivery_2[product]

total = 0

for quantity in combined.values():
    total = total + quantity

print("Combined delivery:", combined)
print("Grand total:", total)
