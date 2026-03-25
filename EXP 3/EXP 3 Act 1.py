Code for receipt
"""
Created on Mon Feb 16 15:04:29 2026

@author:swapnil
"""
# Input from user

copies=int(input("Enter number of receipt copies:"))
items=int(input("Enter number of items in each receipt:"))

#outer loop for receipt copies

for copy in range(1, copies+1):
    print("\nReceipt copy:", copy)
    print("----------------------")
   
    #Inner loop for items in each receipt
    for item in range(1, items+1):
        print("Item Number:",item)
       
    print("----------------------")
   
print("\nALL receipts printed successfully!")    
