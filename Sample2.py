n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")

else:
    sum_even = 0
    count_odd = 0
    sum_divisible = 0
    total = 0

    for i in range(1, n + 1):

        total = total + i

        if i % 2 == 0:
            sum_even = sum_even + i

        else:
            count_odd = count_odd + 1

        if i % 3 == 0 and i % 5 == 0:
            sum_divisible = sum_divisible + i

    average = total / n

    print("Sum of even numbers:", sum_even)
    print("Number of odd numbers:", count_odd)
    print("Sum of numbers divisible by both 3 and 5:", sum_divisible)
    print("Average:", average)
