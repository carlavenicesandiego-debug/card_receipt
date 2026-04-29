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
