n = int(input("Enter the value of n: "))

numbers = list(range(1, n + 1))

while len(numbers) > 1:
    numbers = numbers[1::2]
    print(numbers)
