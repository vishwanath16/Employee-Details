import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create a table for storing user information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance REAL NOT NULL
)
''')

conn.commit()

def create_customer():
    """Function to create a new customer."""
    name = input("Enter customer name: ")
    pin = input("Enter a 4-digit PIN: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    
    cursor.execute("INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)", (name, pin, initial_deposit))
    conn.commit()
    
    print(f"Customer {name} created successfully!")

def customer_menu(user_id):
    """Customer menu for account operations."""
    while True:
        print("\n--- Customer Menu ---")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Logout")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
            conn.commit()
            print("Deposit successful!")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
            current_balance = cursor.fetchone()[0]
            if current_balance >= amount:
                cursor.execute("UPDATE users SET balance = balance - ? WHERE user_id = ?", (amount, user_id))
                conn.commit()
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")
        elif choice == "3":
            cursor.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,))
            balance = cursor.fetchone()[0]
            print(f"Your current balance is: {balance}")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    """Main function to handle bank operations."""
    while True:
        print("\nWelcome to the Bank!")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            entered_pin = input("Enter Admin PIN: ")
            if entered_pin == "123":  # Admin PIN hardcoded for simplicity
                create_customer()
            else:
                print("Incorrect PIN!")
        elif choice == "2":
            try:
                user_id = int(input("Enter your User ID: "))
                pin = input("Enter your PIN: ")
                cursor.execute("SELECT * FROM users WHERE user_id = ? AND pin = ?", (user_id, pin))
                user = cursor.fetchone()
                if user:
                    print(f"Welcome, {user[1]}!")
                    customer_menu(user_id)
                else:
                    print("Invalid User ID or PIN!")
            except ValueError:
                print("Invalid input! Please enter a valid User ID.")
        elif choice == "3":
            print("Exiting the application. Thank you!")
            conn.close()  # Close the database connection
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
main()
