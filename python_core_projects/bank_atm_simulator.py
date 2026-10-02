# Program: Banking & ATM Simulator


class BankAccount:

    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def show_balance(self):
        print("\nCurrent Balance: ₹", self.balance)

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            self.transactions.append("Deposited ₹" + str(amount))
            print("\n₹", amount, "deposited successfully.")
            print("Current Balance: ₹", self.balance)

        else:
            print("\nInvalid amount.")

    def withdraw(self, amount):

        if amount <= 0:
            print("\nInvalid amount.")

        elif amount > self.balance:
            print("\nInsufficient balance.")

        else:
            self.balance -= amount
            self.transactions.append("Withdrawn ₹" + str(amount))
            print("\n₹", amount, "withdrawn successfully.")
            print("Current Balance: ₹", self.balance)

    def show_transactions(self):

        print("\n----- TRANSACTION HISTORY -----")

        if len(self.transactions) == 0:
            print("No transactions yet.")

        else:
            for transaction in self.transactions:
                print(transaction)


# Creating account

print("================================")
print("       WELCOME TO PYTHON BANK")
print("================================")

name = input("Enter your name: ")
account_number = input("Enter account number: ")
pin = input("Set your 4-digit PIN: ")

account = BankAccount(name, account_number, pin, 5000)

print("\nAccount created successfully!")
print("Initial Balance: ₹5000")


# ATM Login

print("\n================================")
print("           ATM LOGIN")
print("================================")

entered_pin = input("Enter your PIN: ")

if account.check_pin(entered_pin):

    print("\nLogin successful!")
    print("Welcome,", account.name)

    while True:

        print("\n================================")
        print("           ATM MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Account Details")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            account.show_balance()

        elif choice == "2":

            amount = float(input("Enter deposit amount: ₹"))
            account.deposit(amount)

        elif choice == "3":

            amount = float(input("Enter withdrawal amount: ₹"))
            account.withdraw(amount)

        elif choice == "4":

            account.show_transactions()

        elif choice == "5":

            print("\n----- ACCOUNT DETAILS -----")
            print("Name:", account.name)
            print("Account Number:", account.account_number)
            print("Balance: ₹", account.balance)

        elif choice == "6":

            print("\nThank you for using Python Bank.")
            print("Have a nice day!")
            break

        else:

            print("\nInvalid choice. Please try again.")

else:

    print("\nIncorrect PIN.")
    print("Access denied.")