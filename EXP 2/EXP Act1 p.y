# Traffic police speed checking program
"""
Created on Mon Mar 16 14:47:07 2026

@author: swapnil
"""



speed = float(input("Enter vehicle speed (km/h): "))

if speed > 60:
    print("Overspeeding! You have to pay a fine.")
else:
    print("Speed is within the limit. Drive safely.")
