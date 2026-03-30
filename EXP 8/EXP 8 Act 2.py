# Handle invalid age input in registration form.
"""
Created on Mon Mar 30 15:43:12 2026

@author: swapnil
"""

def get_valid_age():
    while True:
        user_input = input("Please enter your age: ")
        
        try:         
            age = int(user_input)
            if age < 0:
                print("Age cannot be negative.")
            elif age > 50:
                print("That age seems unlikely. Please enter a real age.")
            else:
                return age
                
        except ValueError:
            
            print(f"Invalid input '{user_input}'. Please enter a whole number.")

registration_age = get_valid_age()
print(f"Registration successful! Age set to: {registration_age}")
