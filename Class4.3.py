items = ["pen", "book", "pen", "bag", "book", "ruler", "pen"]

unique_items = []
repeated_occurrences = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)
    else:
        repeated_occurrences.append(item)

print("Unique items:", unique_items)
print("Repeated occurrences:", repeated_occurrences)