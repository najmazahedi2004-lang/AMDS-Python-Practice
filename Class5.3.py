stock = {
    "pen": 12,"book": 3,"bag": 2,"ruler": 9, "calculator": 1
}

total = 0
low_stock = {}

for item, quantity in stock.items():
    total = total + quantity

    if quantity < 5:
        low_stock[item] = quantity

print("Total units:", total)
print("Low stock:", low_stock)
