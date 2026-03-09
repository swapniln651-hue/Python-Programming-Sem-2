# Dictionary operation: add ,delete and updated key value pair
"""
Created on Mon Mar  9 14:56:52 2026

@author: swapnil
"""

# Creating an empty dictionary
student = {}
# Adding key-value pairs
student["name"] = "Rahul"
student["age"] = 20
student["course"] = "Python"
print("Dictionary after adding elements:")
print(student)
# Updating a value
student["age"] = 21
print("\nDictionary after updating a value:")
print(student)
# Deleting a key-value pair
del student["course"]
print("\nDictionary after deleting a key-value pair:")
print(student)


