#code  for receipt
"""
Created on Mon Feb 16 15:33:43 2026

@author: swapnil
"""

copies = int(input("Enter number of receipt copies: "))
items = int(input("Enter number of items in each receipt: "))

for copy in range(1, copies + 1):
    print("\nReceipt copies:",copy)
    print("------------------------")
    
    for items in range(1 , items + 1):
        print("Items Number:",items)
        
    print("-------------------------")
    
    
print("\nAll receipt printed successfully!")
