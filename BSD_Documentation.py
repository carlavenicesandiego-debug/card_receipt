ThisS CODE IS THE FIRST TRIAL 
print("Please log in to your account to proceed.\n")

user = input("Enter your account: ")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter your password: ")

    if password != " ":
        print(f"Welcome back, {user}!!\n")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.\n")
if attempts == max_attempts:
    print("Too many attempts, access denied!")

print("Please choose if you want to convert your money")

STILL PROCESSING THE CODE
allowed_users = ["raven", "carla", "jaren", "romero", "chin"]
correct_password = "12345"

max_attempts = 3
attempts = 0

username = input("Enter username: ")

# In - Checks the value if it is inside the list.
if username in allowed_users:
    while attempts < max_attempts:
        password = input("Enter password: ")

        if password == correct_password:
            print("Access granted! Welcome to the domain.\n")
            break
        else:
            attempts += 1
            print("Incorrect password. Attempts left:", max_attempts - attempts)

    if attempts == max_attempts:
        print("Too many failed attempts. Access denied.")
else:
    print("Username not found.")

print("Welcome to -- UniCash -- The most convinient and trusted for your money!!\n")

print("Please choose if you want to convert your money")

choices = [
    ["Check_the_balance"],
    ["Money Convertion"],
    ["Cash_In"],
    ["Padala_Pay"]
]
for i in range(len(choices)):
    print(i + 1, "-", choices[i][0])

php_balance = 0.0
transactions = []
usd_balance = 0.0

print("\n")
while True:
    Selection = int(input("Enter your choice (1-4): "))
    if Selection == 1:
        print(f"Your current balance is ₱{php_balance}")
        print(f"Your current balance in ${usd_balance}\n")

    if Selection == 0:
        print("The System is exiting...")
        break

    elif Selection == 2:
        print("Digital Money Convertion 2026\n")
        print("1.PHP - USD")
        choose = int(input("Choose: "))
        if choose == 1:
            currency = float(
                input("Enter the amount you want to convert: "))
            usd = currency * 0.018
            # once the balance is converted, it deletes and replace the new.
            print(f"You converted your ₱{currency} into ${usd}\n")
            php_balance -= currency
            usd_balance += usd
            transactions.append(f"PHP {currency} > USD {usd}")

    if Selection == 3:
        amount = float(input("Enter the amount you want to add: "))
        php_balance += amount  # It adds to the existing value.
        transactions.append(amount)  # It save the previous transactions.
        print(f"Your New Current Balance now is ₱{php_balance}, Thank you!\n")
        continue

    elif Selection == 4:
        print("Welcome to Padala_Pay\n")  # Only PHP can use.

        receiver = input("Enter receiver name: ")
        total_amount = float(input("Enter the amount: "))

        if total_amount <= php_balance:
            php_balance -= total_amount  # It subracts to the existing value.
            transactions.append(f"Sent ₱{total_amount} to {receiver}\n") # It saves it to the transactions.

            print("Transfer Successfully!")
            print(f"Your new balance now is ₱{php_balance}\n")
        else:
            print("Insufficient Balance!")

The only thing missing from this code is how to increase the balance when sending pay and then asking what you want to send, 
php or usd, the same goes for selection 2.

# Project Programming
# Objectives - Create a log in account, create money converter and print a receipt.
from datetime import datetime
while True:
    allowed_users = ["raven", "carla", "jaren", "romero", "chin"]
    correct_password = "12345"

    max_attempts = 3
    attempts = 0

    username = input("Enter username: ")

    # IN Function: Tinitignan niya if merong kapareho sa loob ng list at kung tama mag proceed ito.
    if username in allowed_users:

        while attempts < max_attempts:
            password = input("Enter password: ")

            if password == correct_password:
                print("Access granted! Welcome to the domain.\n")
                break

            else:
                attempts += 1
                print("Incorrect password. Attempts left:",
                      max_attempts - attempts)

        if attempts == max_attempts:
            print("Too many failed attempts. Access denied.\n")
            exit()

    else:
        print("Username not found.\n")
        exit()

    print("Welcome to -- UniCash -- The most convenient and trusted for your money!!\n")

    choices = [
        ["Check the balance"],
        ["Money Conversion"],
        ["Cash In"],
        ["Padala Pay"]
    ]

    for i in range(len(choices)):
        print(i + 1, "-", choices[i][0])

    php_balance = 0.0
    usd_balance = 0.0

    print("\n")

    while True:

        Selection = int(input("Enter your choice (1-4) or 0 to Exit: "))

        if Selection == 0:
            print("Logging Out...\n")
            break

        elif Selection == 1:
            print("\n======================================")
            print("            UNI CASH WALLET           ")
            print("======================================")
            print(f"Account Holder : {username}")
            print("--------------------------------------")
            # 2F is a formatting and para sa 2 Decimal Places.
            print(f"PHP Balance    : ₱{php_balance:.2f}")
            print(f"USD Balance    : ${usd_balance:.2f}")
            print("======================================\n")

        elif Selection == 2:
            print("\nDigital Money Conversion 2026")
            print("1. PHP - USD")

            choose = int(input("Choose: "))

            if choose == 1:
                currency = float(input("Enter amount to convert: "))

                if currency <= php_balance:
                    usd = currency * 0.018

                    php_balance -= currency
                    usd_balance += usd

                    print(f"You converted ₱{currency} into ${usd:.2f}\n")

                else:
                    print("Insufficient PHP balance!")
                    print("Please add balance to your account first!\n")

        elif Selection == 3:
            amount = float(input("Enter amount to Cash In: "))

            php_balance += amount

            print(f"Your new balance is ₱{php_balance}\n")

        elif Selection == 4:
            print("\nWelcome to Padala Pay\n")

            receiver = input("Enter receiver name: ")
            total_amount = float(input("Enter amount to transfer: "))

            if total_amount <= php_balance:

                php_balance -= total_amount

                current_time = datetime.now()
                date = current_time.strftime("%Y-%m-%d")

                print("\n========== BANK RECEIPT ==========")
                print(" UniCash")
                print("==================================")
                print(f"Sender Name   : {username}")
                print(f"Receiver Name : {receiver}")
                print(f"Amount Sent   : ₱{total_amount}")
                print(f"Balance Left  : ₱{php_balance}")
                print(f"Date          : {date}")
                print("==================================")
                print(f"Your current balance now: ₱{php_balance}")
                print("==================================\n")
                choose = input("Do you want to continue? (yes/no): ")
                if choose.lower() == "no":
                    print("Logging Out...\n")
                    break
                else:
                    print("\n")
                    continue
            else:
                print("Insufficient Balance!\n")

        else:
            print("Invalid choice!\n")


ALMOST DONE BUT WE NEED TO ADD SOMETHING HERETO FINISH  THIS PART 


from datetime import datetime

allowed_users = ["Raven", "Carla", "Jaren", "Romero", "Chin"]
correct_password = "12345"

# ===== ADDED CODE START =====
accounts = {
    "Raven": {"PHP": 0.0, "USD": 0.0},
    "Carla": {"PHP": 0.0, "USD": 0.0},
    "Jaren": {"PHP": 0.0, "USD": 0.0},
    "Romero": {"PHP": 0.0, "USD": 0.0},
    "Chin": {"PHP": 0.0, "USD": 0.0}
}
# ===== ADDED CODE END =====


while True:

    max_attempts = 3
    username_attempts = 0

    while username_attempts < max_attempts:

        username = input("Enter username: ").title()

        if username in allowed_users:
            print("Username accepted!\n")
            break

        else:
            username_attempts += 1
            print(f"Incorrect username. Attempts left: {max_attempts - username_attempts}\n")

    if username_attempts == max_attempts:
        print("Too many failed username attempts. Access denied.\n")
        exit()

    attempts = 0

    while attempts < max_attempts:

        password = input("Enter password: ")

        if password == correct_password:
            print("Access granted! Welcome to the domain.\n")
            break

        else:
            attempts += 1
            print("Incorrect password. Attempts left:",
                  max_attempts - attempts)

    if attempts == max_attempts:
        print("Too many failed attempts. Access denied.\n")
        exit()

    print("Welcome to -- UniCash -- The most convenient and trusted for your money!!\n")

    choices = [
        ["Check the balance"],
        ["Money Conversion"],
        ["Cash In"],
        ["Padala Pay"]
    ]

    for i in range(len(choices)):
        print(i + 1, "-", choices[i][0])

    print("\n")

    while True:

        Selection = int(input("Enter your choice (1-4) or 0 to Exit: "))

        if Selection == 0:
            print(f"Logging out {username}...\n")
            break

        elif Selection == 1:

            print("\n======================================")
            print("            UNI CASH WALLET           ")
            print("======================================")
            print(f"Account Holder : {username}")
            print("--------------------------------------")

            # ===== CHANGED CODE START =====
            print(f"PHP Balance    : ₱{accounts[username]['PHP']:.2f}")
            print(f"USD Balance    : ${accounts[username]['USD']:.2f}")
            # ===== CHANGED CODE END =====

            print("======================================\n")

        elif Selection == 2:

            print("\nDigital Money Conversion 2026")
            print("1. PHP - USD")
            print("2. USD - PHP")

            choose = int(input("Choose: "))

            if choose == 1:

                currency = float(input("Enter PHP amount to convert: "))

                # ===== CHANGED CODE START =====
                if currency <= accounts[username]["PHP"]:

                    usd = currency * 0.018

                    accounts[username]["PHP"] -= currency
                    accounts[username]["USD"] += usd
                # ===== CHANGED CODE END =====

                    print(f"You converted ₱{currency} into ${usd:.2f}\n")

                else:
                    print("Insufficient PHP balance!")

            elif choose == 2:

                currency = float(input("Enter USD amount to convert: "))

                # ===== CHANGED CODE START =====
                if currency <= accounts[username]["USD"]:

                    php = currency * 62

                    accounts[username]["USD"] -= currency
                    accounts[username]["PHP"] += php
                # ===== CHANGED CODE END =====

                    print(f"You converted ${currency} into ₱{php:.2f}\n")

                else:
                    print("Insufficient USD balance!")

        elif Selection == 3:

            print("What balance do you want to add?")
            print("1. PHP")
            print("2. USD\n")

            select = int(input("Choose (1-2): "))

            if select == 1:

                amount = float(input("Enter amount to Cash In: "))

                # ===== CHANGED CODE START =====
                accounts[username]["PHP"] += amount
                print(f"Your new balance is ₱{accounts[username]['PHP']:.2f}\n")
                # ===== CHANGED CODE END =====

            elif select == 2:

                amount = float(input("Enter amount to Cash In: "))

                # ===== CHANGED CODE START =====
                accounts[username]["USD"] += amount
                print(f"Your new balance is ${accounts[username]['USD']:.2f}\n")
                # ===== CHANGED CODE END =====

        elif Selection == 4:

            print("\nWelcome to Padala Pay\n")

            print("What currency do you want to send?")
            print("1. PHP")
            print("2. USD\n")

            currency_choice = int(input("Choose (1-2): "))
            receiver = input("Enter receiver name: ").title()

            # ===== ADDED CODE START =====
            if receiver not in allowed_users:
                print("Receiver not found!\n")
                continue
            # ===== ADDED CODE END =====

            if currency_choice == 1:

                total_amount = float(input("Enter amount to transfer: "))

                # ===== ADDED CODE START =====
                if total_amount <= accounts[username]["PHP"]:

                    accounts[username]["PHP"] -= total_amount
                    accounts[receiver]["PHP"] += total_amount

                    print(f"{username} Balance : ₱{accounts[username]['PHP']:.2f}")
                    print(f"{receiver} Balance : ₱{accounts[receiver]['PHP']:.2f}")
                # ===== ADDED CODE END =====

                else:
                    print("Insufficient PHP balance!")

            elif currency_choice == 2:

                total_amount = float(input("Enter amount to transfer: "))

                # ===== ADDED CODE START =====
                if total_amount <= accounts[username]["USD"]:

                    accounts[username]["USD"] -= total_amount
                    accounts[receiver]["USD"] += total_amount

                    print(f"{username} Balance : ${accounts[username]['USD']:.2f}")
                    print(f"{receiver} Balance : ${accounts[receiver]['USD']:.2f}")
                # ===== ADDED CODE END =====

                else:
                    print("Insufficient USD balance!")
