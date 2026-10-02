#       SURVIVAL CITY SIMULATOR


import random


# ---------- PLAYER DATA ----------

player = {
    "name": "",
    "health": 100,
    "energy": 100,
    "coins": 100,
    "level": 1,
    "xp": 0
}

inventory = {
    "food": 3,
    "water": 3,
    "medicine": 1,
    "weapon": 1
}


# ---------- FUNCTIONS ----------

def show_status():

    print("\n========== PLAYER STATUS ==========")

    print("Name   :", player["name"])
    print("Health :", player["health"])
    print("Energy :", player["energy"])
    print("Coins  :", player["coins"])
    print("Level  :", player["level"])
    print("XP     :", player["xp"])


def show_inventory():

    print("\n========== INVENTORY ==========")

    for item, quantity in inventory.items():
        print(item, ":", quantity)


def eat_food():

    if inventory["food"] > 0:

        inventory["food"] -= 1
        player["health"] += 20

        if player["health"] > 100:
            player["health"] = 100

        print("\nYou ate food.")
        print("Health:", player["health"])

    else:

        print("\nYou don't have food.")


def drink_water():

    if inventory["water"] > 0:

        inventory["water"] -= 1
        player["energy"] += 20

        if player["energy"] > 100:
            player["energy"] = 100

        print("\nYou drank water.")
        print("Energy:", player["energy"])

    else:

        print("\nYou don't have water.")


def use_medicine():

    if inventory["medicine"] > 0:

        inventory["medicine"] -= 1
        player["health"] += 40

        if player["health"] > 100:
            player["health"] = 100

        print("\nMedicine used.")
        print("Health:", player["health"])

    else:

        print("\nYou don't have medicine.")


def explore():

    if player["energy"] < 20:

        print("\nNot enough energy to explore.")
        return

    player["energy"] -= 20

    print("\nYou are exploring the city...")

    event = random.randint(1, 5)

    if event == 1:

        coins = random.randint(20, 50)
        player["coins"] += coins

        print("You found", coins, "coins!")

    elif event == 2:

        food = random.randint(1, 3)
        inventory["food"] += food

        print("You found", food, "food.")

    elif event == 3:

        water = random.randint(1, 3)
        inventory["water"] += water

        print("You found", water, "water bottles.")

    elif event == 4:

        inventory["medicine"] += 1

        print("You found medicine.")

    else:

        print("A zombie attacked you!")
                
        damage = random.randint(10, 30)

        player["health"] -= damage

        print("You lost", damage, "health.")

        if player["health"] < 0:
            player["health"] = 0


def fight():

    if inventory["weapon"] <= 0:

        print("\nYou don't have a weapon.")
        return

    if player["energy"] < 20:

        print("\nNot enough energy.")
        return

    player["energy"] -= 20

    enemy_health = random.randint(30, 60)

    print("\nEnemy appeared!")
    print("Enemy health:", enemy_health)

    while enemy_health > 0 and player["health"] > 0:

        print("\n1. Attack")
        print("2. Run")

        choice = input("Enter choice: ")

        if choice == "1":

            damage = random.randint(15, 30)

            enemy_health -= damage

            print("You attacked!")
            print("Damage:", damage)

            if enemy_health > 0:

                enemy_damage = random.randint(5, 20)

                player["health"] -= enemy_damage

                print("Enemy attacked!")
                print("You lost:", enemy_damage, "health")

        elif choice == "2":

            print("You escaped.")
            break

        else:

            print("Invalid choice.")

    if enemy_health <= 0:

        reward = random.randint(30, 70)

        player["coins"] += reward
        player["xp"] += 20

        print("\nYou defeated the enemy!")
        print("Coins earned:", reward)
        print("XP earned: 20")

        check_level()


def check_level():

    if player["xp"] >= 100:

        player["level"] += 1
        player["xp"] = 0

        print("\nLEVEL UP!")
        print("Your level is now:", player["level"])


def shop():

    while True:

        print("\n========== SHOP ==========")

        print("Coins:", player["coins"])

        print("\n1. Food     - 10 coins")
        print("2. Water    - 10 coins")
        print("3. Medicine - 30 coins")
        print("4. Weapon   - 50 coins")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":

            if player["coins"] >= 10:

                player["coins"] -= 10
                inventory["food"] += 1

                print("Food purchased.")

            else:

                print("Not enough coins.")

        elif choice == "2":

            if player["coins"] >= 10:

                player["coins"] -= 10
                inventory["water"] += 1

                print("Water purchased.")

            else:

                print("Not enough coins.")

        elif choice == "3":

            if player["coins"] >= 30:

                player["coins"] -= 30
                inventory["medicine"] += 1

                print("Medicine purchased.")

            else:

                print("Not enough coins.")

        elif choice == "4":

            if player["coins"] >= 50:

                player["coins"] -= 50
                inventory["weapon"] += 1

                print("Weapon purchased.")

            else:

                print("Not enough coins.")

        elif choice == "5":

            break

        else:

            print("Invalid choice.")


def mission():

    print("\n========== MISSION ==========")

    print("Mission: Collect at least 5 food items.")

    if inventory["food"] >= 5:

        player["coins"] += 50
        player["xp"] += 30

        print("Mission completed!")
        print("Reward: 50 coins")
        print("XP: 30")

        check_level()

    else:

        print("Mission not completed.")
        print("Current food:", inventory["food"])


def random_event():

    event = random.randint(1, 4)

    if event == 1:

        player["coins"] += 20

        print("\nYou found 20 coins!")

    elif event == 2:

        player["health"] -= 10

        print("\nYou lost 10 health!")

        if player["health"] < 0:
            player["health"] = 0

    elif event == 3:

        inventory["water"] += 1

        print("\nYou found a water bottle!")

    else:

        print("\nNothing happened.")


# ---------- START GAME ----------

print("========================================")
print("       SURVIVAL CITY SIMULATOR")
print("========================================")

player["name"] = input("Enter your name: ")

print("\nWelcome", player["name"] + "!")
print("Try to survive as long as possible.")


# ---------- MAIN MENU ----------

while player["health"] > 0:

    print("\n================================")
    print("             MENU")
    print("================================")

    print("1. Player Status")
    print("2. Inventory")
    print("3. Explore City")
    print("4. Fight Enemy")
    print("5. Shop")
    print("6. Eat Food")
    print("7. Drink Water")
    print("8. Use Medicine")
    print("9. Mission")
    print("10. Random Event")
    print("11. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        show_status()

    elif choice == "2":

        show_inventory()

    elif choice == "3":

        explore()

    elif choice == "4":

        fight()

    elif choice == "5":

        shop()

    elif choice == "6":

        eat_food()

    elif choice == "7":

        drink_water()

    elif choice == "8":

        use_medicine()

    elif choice == "9":

        mission()

    elif choice == "10":

        random_event()

    elif choice == "11":

        print("\nGame ended.")
        break

    else:

        print("\nInvalid choice.")


# ---------- GAME OVER ----------

if player["health"] <= 0:

    print("\n================================")
    print("           GAME OVER")
    print("================================")

    print("You ran out of health.")

print("\nThank you for playing!")