# ATM withdrawal system handles insufficient balance.
"""
Created on Mon Mar 30 15:35:24 2026

@author: swapnil
"""

class InsufficientFundsError(Exception):   
    pass

class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw(self, amount):
        print(f"\n--- Transaction Started ---")
        print(f"Current Balance: {self.balance}")
        print(f"Attempting to withdraw: {amount}")

        try:
            if amount > self.balance:
                raise InsufficientFundsError(f"Transaction Denied: You are {amount - self.balance} short.")
            
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
          
            self.balance -= amount
            print(f"Success! Please take your cash.")
            print(f"New Balance: {self.balance}")

        except InsufficientFundsError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid Input: {e}")
        finally:
            print("--- Transaction Finished ---")

my_account = ATM(500)

my_account.withdraw(200)

my_account.withdraw(400)
