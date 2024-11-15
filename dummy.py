users = {}  
admin_pin = "123"  

def create_customer():
    user_id = len(users) + 1
    name = input("Please enter customer Name: ")
    pin = input("Please enter a 4-digit PIN: ")
    initial_deposit = float(input("Enter initial deposit amount: "))

    users[user_id] = {
        "name": name,
        "pin": pin,
        "balance": initial_deposit
    }

    print(f"Customer created successfully!\nUser ID: {user_id}\nName: {name}")
    return user_id

def deposit_money(user_id):
    
    amount = float(input("Enter amount to deposit: "))
    users[user_id]["balance"] += amount
    print(f"Deposit successful! New balance: {users[user_id]['balance']}")

def withdraw_money(user_id):
    
    amount = float(input("Enter amount to withdraw: "))
    if users[user_id]["balance"] >= amount:
        users[user_id]["balance"] -= amount
        print(f"Withdrawal successful! Remaining balance: {users[user_id]['balance']}")
    else:
        print("Insufficient balance!")

def balance_check(user_id):
    
    print(f"Your current balance is: {users[user_id]['balance']}")

def admin_menu():
    
    print("\n--- Admin Menu ---")
    create_customer()

def customer_menu(user_id):
    
    while True:
        print("\n--- Customer Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Logout")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            users[user_id]["balance"] += amount
            print(f"Deposit successful! New balance: {users[user_id]['balance']}")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if users[user_id]["balance"] >= amount:
                users[user_id]["balance"] -= amount
                print(f"Withdrawal successful! Remaining balance: {users[user_id]['balance']}")
            else:
                print("Insufficient balance!")
        elif choice == "3":
            print(f"Your current balance is: {users[user_id]['balance']}")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    
    while True:
        print("\nWelcome to the Bank!")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            entered_pin = input("Enter Admin PIN: ")
            if entered_pin == admin_pin:
                create_customer()
            else:
                print("Incorrect PIN!")
        elif choice == "2":
            try:
                user_id = int(input("Enter your User ID: "))
                pin = input("Enter your PIN: ")
                if user_id in users and users[user_id]["pin"] == pin:
                    print(f"Welcome, {users[user_id]['name']}!")
                    customer_menu(user_id)
                else:
                    print("Invalid User ID or PIN!")
            except ValueError:
                print("Invalid input! Please enter a valid User ID.")
        elif choice == "3":
            print("Exiting the application. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


main()