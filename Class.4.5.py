items = []

while True:
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter the item you want to add: ")
        items.append(item)
        print(item, "has been added to the list.")

    elif choice == "2":
        item = input("Enter the item you want to remove: ")

        if item in items:
            items.remove(item)
            print(item, "has been removed from the list.")
        else:
            print("Item not found in the list.")

    elif choice == "3":
        print("Current list:", items)

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice.")