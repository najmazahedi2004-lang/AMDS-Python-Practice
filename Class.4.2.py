numbers = [4, 7, 2, 7, 9, 7, 1]
target = 7

positions = []

for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i)

print("Target:", target)
print("Positions:", positions)
print("Number of occurrences:", len(positions))

first_occurrence = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        first_occurrence = i
        break

if first_occurrence != -1:
    print("First occurrence:", first_occurrence)
else:
    print("First occurrence: Not found")