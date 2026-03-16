# Find the factorial of a number using loops.
"""
Created on Mon Mar 16 14:42:41 2026

@author: swapnil
"""
n = int(input("Enter number:"))
fact = 1
for i in range(1, n + 1):
   fact = fact * i
print("Factorial:", fact)
