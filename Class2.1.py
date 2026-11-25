while True:
    x = input("Enter your mark: ")

    if x.isdigit():
        x = int(x)
        break
    else:
        print("Please enter an integer.")

if 97 <= x <= 100:
    print("A+")
elif 93 <= x <= 96:
    print("A")
elif 90 <= x <= 92:
    print("A-")
elif 86 <= x <= 88:
    print("B+")
else:
    print("No grade assigned")

