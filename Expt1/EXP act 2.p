#code for seat booking
"""
Created on Mon Feb 16 15:43:30 2026

@author: swapnil
"""

row = int(input("Enter number of rows: "))
seats_per_rows = int(input("Enter number of seats in each row: "))

for rows in range(1 ,row + 1):
    print("Row", row,  ":", end=" ")
    
    for seat in range(1, seats_per_rows + 1):
    
        print("fS{seat}", end=" ")
    
    print()
        
