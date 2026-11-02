# 2.10 ATM PIN Simulator (With Balance Management)

CORRECT_PIN = "1234"
attempts = 3
balance = 5000.0  # Setting a starting balance for the user
authenticated = False

# Part 1: PIN Verification Loop
while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    
    if entered_pin == CORRECT_PIN:
        print("Access Granted!\n")
        authenticated = True
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Attempts remaining: {attempts}")

if attempts == 0:
    print("Card Blocked! Too many incorrect attempts.")

# Part 2: ATM Transaction Menu (Runs only if PIN is correct)
while authenticated:
    print("----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit (Save) Money")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")
    
    if choice == "1":
        print(f"Your current balance is: Rs. {balance}\n")
        
    elif choice == "2":
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Transaction Failed: Insufficient funds!\n")
        elif withdraw_amount <= 0:
            print("Transaction Failed: Invalid amount!\n")
        else:
            balance -= withdraw_amount
            print(f"Rs. {withdraw_amount} withdrawn successfully.")
            print(f"Remaining Balance: Rs. {balance}\n")
            
    elif choice == "3":
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount <= 0:
            print("Transaction Failed: Invalid amount!\n")
        else:
            balance += deposit_amount
            print(f"Rs. {deposit_amount} deposited successfully.")
            print(f"New Balance: Rs. {balance}\n")
            
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break  # Exits the ATM menu loop
        
    else:
        print("Invalid choice! Please select a valid option.\n")
