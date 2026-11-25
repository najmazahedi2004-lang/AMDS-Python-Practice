numbers = [14, 8, 21, 21, 5, 17, 14]

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

if second_largest is None:
    print("There are fewer than two distinct values.")
else:
    print("Largest distinct value:", largest)
    print("Second-largest distinct value:", second_largest)