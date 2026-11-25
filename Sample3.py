numbers = [12, 7, -4, 12, 18, 5, -3, 8, 18]

# Initialize the lists and variables
non_negative = []
unique_non_negative = []
sum_even = 0
count_negative = 0


for i in numbers:

    
    if i < 0:
        count_negative = count_negative + 1
        continue

   
    non_negative.append(i)

    
    if i not in unique_non_negative:
        unique_non_negative.append(i)

   
    if i % 2 == 0:
        sum_even = sum_even + i

selected_elements = numbers[1:8:2]

print("Original list:", numbers)
print("Non-negative values:", non_negative)
print("Unique non-negative values:", unique_non_negative)
print("Sum of even non-negative numbers:", sum_even)
print("Number of negative numbers:", count_negative)
print("Elements at indices 1, 3, 5 and 7:", selected_elements)
