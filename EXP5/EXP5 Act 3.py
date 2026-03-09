# A shop inventory dictionary stores item name and quantity. Add new stock.
"""
Created on Mon Mar  9 15:37:01 2026

@author: Swapnil
"""

inventory = {"Apples": 50, "Bananas": 20}

item = "Apples"
added_quantity = 30

if item in inventory:
    inventory[item] += added_quantity  # Adds to existing 50
else:
    inventory[item] = added_quantity   # Creates new entry if not found
   
from collections import defaultdict

# Initialize with int (which defaults to 0)
inventory = defaultdict(int, {"Apples": 50, "Bananas": 20})

# No check needed!
inventory["Apples"] += 30
inventory["Oranges"] += 15

print(dict(inventory))
