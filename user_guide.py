Banking Card  System User Guide"


Introduction

The Banking Card System is a Python based console application designed to help users manage their digital money transactions securely and conveniently. The system allows users to log in using authorized accounts, check balances, convert currencies between PHP and USD, cash in funds, and transfer money using the Padala Pay feature. It also records transactions and displays receipts for successful operations.



Objectives

The system aims to:

* Provide secure login authentication

* Manage PHP and USD balances

* Convert money between currencies

* Allow users to cash in funds

* Send money through Padala Pay

* Generate transaction receipts

* Record and display account balances accurately



System Requirements

Before running the system, make sure the following are installed:

* Python

* Terminal or Command Prompt

* Text Editor or IDE (VS Code, PyCharm, etc.)


Files Included


| File Name      | Description         |

| -------------- | ------------------- |

| `Banking_Card.py`   | Main Python Program |

| `README.md`    | Project Description |

| `UserGuide.md` | User Manual         |



How to Run the System


Step 1: Open Terminal or Command Prompt

Navigate to the folder containing the Python file.

Example:


```bash

cd Desktop/Banking Card

```


Step 2: Run the Program

Type the following command:


```bash

py Banking_Card.py

```


or


```bash

python Banking_Card.py

```


Using the System

Step 1: Login Authentication


The system asks for:

* Username

* Password


Allowed Users:

* Raven

* Carla

* Jaren

* Romero

* Chin


Example:

```text

Enter username: Romero

Enter password: 12345

```

If the username and password are correct:


```text

Access granted! Welcome to the domain.

```


The system only allows 3 login attempts.

Main Menu
After logging in successfully, the system displays the following menu:

```text
1 - Check the balance
2 - Money Conversion
3 - Cash In
4 - Padala Pay
0 - Exit
```
Choose the desired option by entering the corresponding number.


1. Check the Balance

This feature displays the user’s current PHP and USD balances.

Example Output:

```text
======================================
            UNI CASH WALLET
======================================
Account Holder : Romero
--------------------------------------
PHP Balance : ₱5000.00
USD Balance : $100.00
======================================
```

2. Money Conversion
This feature allows users to convert money between PHP and USD.

Conversion Options

```text
1. PHP - USD
2. USD - PHP
```

PHP to USD Conversion

The system converts PHP to USD using the exchange rate:

```text
1 PHP = 0.018 USD
```

Example:

```text
Enter PHP amount to convert: 1000
You converted ₱1000 into $18.00
```


USD to PHP Conversion

The system converts USD to PHP using the exchange rate:

```text
1 USD = 62 PHP
```

Example:

```text
Enter USD amount to convert: 20
You converted $20 into ₱1240.00
```

If the balance is insufficient, the system displays:

```text
Insufficient balance!
Please add balance to your account first!
```



3. Cash In

This feature allows users to add money to their account balance.

 Cash In Options

```text
1. PHP
2. USD
```

Example:

```text
Enter amount to Cash In: 500
Your new balance is ₱500.00
```

or

```text
Enter amount to Cash In: 50
Your new balance is $50.00
```

4. Padala Pay

This feature allows users to transfer money to another person.

The system asks for:

* Currency Type
* Receiver Name
* Amount to Transfer


Example:

```text
Welcome to Padala Pay

What currency do you want to send?
1. PHP
2. USD

Choose (1-2): 1
Enter receiver name: Carla
Enter amount to transfer: 1000
```

If the balance is sufficient, the transfer becomes successful.


Receipt Generation

After every successful transaction, the system generates a digital receipt containing:

* Sender Name
* Receiver Name
* Transaction Type
* Currency Used
* Amount Sent
* Date and Time
* Remaining Balance


Example Receipt

```text
========================================
              UNI CASH RECEIPT
========================================
Sender Name : Romero
Receiver Name : Carla
Transaction Type : Padala Pay
Currency : PHP
Amount Sent : ₱1000.00
Date and Time : 2026-05-18 19:30:00
Remaining Balance: ₱4000.00
========================================
Thank you for using UniCash!
```

Logout / Exit System

To end the session:

1. Return to the Main Menu
2. Enter:

```text
0
```

The system displays:

```text
Logging out Romero...
```


Error Handling
Errors
* Invalid input
* Incorrect password
* Username not found
* Insufficient balance
* Wrong menu selection

Causes
* Non-numeric input
* Incorrect username/password
* Invalid menu number
* Balance lower than transaction amount


Solutions
* Enter valid menu options only
* Input correct username and password
* Ensure enough balance before transactions
* Restart the program if necessary


Features of the System
* Secure Login Authentication
* Money Conversion
* Cash In System
* Balance Checking
* Padala Pay Transfer
* Digital Receipt Generation
* PHP and USD Wallet Management
* Transaction Recording
* User-Friendly Console Interface


Developers
* Carla
* Raven
* Romero
* Jaren
* Chin


Conclusion

The Banking Card System improves the efficiency of digital money management by providing secure login authentication, fast money conversion, cash-in services, and money transfer features. The system helps users manage their finances conveniently while ensuring accurate balance computation and transaction recording through automated receipt generation.


