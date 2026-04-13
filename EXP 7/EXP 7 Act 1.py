# Create a BankAccount class for deposit and withdrawal.
"""
Created on Mon Apr 13 15:14:01 2026

@author: swapnil
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"\nSuccessfully deposited ${amount:.2f}")
        else:
            print("\nError: Deposit amount must be positive.")
        self.display_balance()

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"\nSuccessfully withdrew ${amount:.2f}")
        elif amount > self._balance:
            print("\nError: Insufficient funds!")
        else:
            print("\nError: Withdrawal amount must be positive.")
        self.display_balance()

    def display_balance(self):
        print(f"Current Balance for {self.owner}: ${self._balance:.2f}")

# --- Setup ---
name = input("Enter account holder name: ")
initial_deposit = float(input("Enter initial deposit: "))
account = BankAccount(name, initial_deposit)


while True:
    print("\n" + "="*20)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)
    
    elif choice == '2':
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    
    elif choice == '3':
        account.display_balance()
    
    elif choice == '4':
        print(f"Goodbye, {account.owner}!")
        break
    
    else:
        print("Invalid choice. Please try again.")
