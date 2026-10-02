# Mini Spreadsheet

print("================================")
print("       MINI SPREADSHEET")
print("================================")

numbers = []

n = int(input("\nHow many numbers do you want to enter? "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("\nYour Spreadsheet:")
print(numbers)

while True:

    print("\n----------- MENU -----------")
    print("1. Add Number")
    print("2. Display Numbers")
    print("3. Find SUM")
    print("4. Find AVERAGE")
    print("5. Find MAXIMUM")
    print("6. Find MINIMUM")
    print("7. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        value = int(input("Enter number to add: "))
        numbers.append(value)
        print("Number added successfully.")

    elif choice == 2:

        print("\nSpreadsheet:")
        print(numbers)

    elif choice == 3:

        total = sum(numbers)
        print("SUM =", total)

    elif choice == 4:

        average = sum(numbers) / len(numbers)
        print("AVERAGE =", average)

    elif choice == 5:

        print("MAXIMUM =", max(numbers))

    elif choice == 6:

        print("MINIMUM =", min(numbers))

    elif choice == 7:

        print("Thank you for using Mini Spreadsheet!")
        break

    else:

        print("Invalid choice.")