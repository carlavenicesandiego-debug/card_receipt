allowed_users = ["raven", "carla", "jaren", "romero", "chin"]
correct_password = "12345"

max_attempts = 3
attempts = 0

username = input("Enter username: ")


if username in allowed_users: # In - Checks the value if it is inside the list.
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
    exit()

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
