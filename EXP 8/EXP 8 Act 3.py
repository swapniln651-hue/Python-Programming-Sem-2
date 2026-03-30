# Handle invalid product index in shopping cart.
"""
Created on Mon Mar 30 15:55:59 2026

@author: swapnil
"""

def display_cart(items):
    if not items:
        print("Your cart is empty.")
        return
    
    print("\nYour Current Cart:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

def manage_cart():
    shopping_cart = ["Apple", "Banana", "Cherry"]
    
    display_cart(shopping_cart)
    
    choice = input("\nEnter the number of the index to remove: ")
    
    try:
        idx = int(choice)
       
        if idx < 1:
            raise IndexError 
            
        removed = shopping_cart.pop(idx - 1)
        print(f"Successfully removed {removed}.")
        
    except (IndexError, ValueError):
        print("Invalid selection. No changes made to the cart.")

manage_cart()
