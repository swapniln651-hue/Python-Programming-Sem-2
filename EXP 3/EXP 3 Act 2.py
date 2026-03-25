# Code for seat booking
"""
Created on Mon Feb 16 15:44:09 2026

@author: swapnil
"""
# Input from user

rows=int(input("Enter number of rows:"))
seats_per_row=int(input("Enter number of seats in each row:"))

#outer loop for rows

for rows in range(1, rows+1):
    print("Row", rows, ":", end="  ")
   
    #Inner loop for seats in each row
    for seat in range(1, seats_per_rows +1):
        print(f"S{seat}", end=" ")
       
    print()   # Move to next line after each row
