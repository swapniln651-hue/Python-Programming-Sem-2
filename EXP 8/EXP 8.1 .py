# Exception handling by handling ZeroDivisionError and IndexError exceptions
"""
Created on Mon Mar 30 15:30:45 2026

@author:swapnil
"""

# Example list
numbers = [10, 20, 30]
try:
# Division operation
  a = int(input("Enter a numerator: "))
  b = int(input("Enter a denominator: "))
  result = a / b
  print("Division result:", result)
# Accessing a list element
  print(numbers)
  index = int(input("Enter index to access in the list [0,1,2]: "))
  print("Element at index", index, "is", numbers[index])
except ZeroDivisionError:
  print("Error: Division by zero is not allowed.")
except IndexError:
  print("Error: Index out of range for the list.")
except ValueError:
  print("Error: Invalid input. Please enter an integer.")
finally:
  print("Program execution completed.")
