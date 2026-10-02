# Cyber Security Simulation

print("====================================")
print("      CYBER SECURITY SIMULATION")
print("====================================")

correct_username = "admin"
correct_password = "admin@123"

attempts = 3

print("\nLogin System")
print("You have 3 attempts.")

while attempts > 0:

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("\nLogin successful!")
        print("Welcome to the secure system.")
        break

    else:
        attempts -= 1
        print("\nWrong username or password.")
        print("Attempts remaining:", attempts)

if attempts == 0:

    print("\n⚠️ SECURITY ALERT!")
    print("Account has been locked.")
    print("Too many failed login attempts.")

else:

    print("\n--- Security Check ---")

    password = correct_password

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in "@#$%!" for char in password):
        score += 1

    print("Password security score:", score, "/ 5")

    if score == 5:
        print("Password strength: Strong")
    elif score >= 3:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

print("\nThank you for using Cyber Security Simulation.")