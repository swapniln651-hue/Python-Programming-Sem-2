# Generate OTP using random module.
"""
Created on Mon Apr 20 15:00:32 2026

@author: swapnil
"""

import random
import string

def generate_otp(length=6):
    
    characters = string.digits 
    
    otp = ''.join(random.choice(characters) for _ in range(length))
    
    return otp

new_otp = generate_otp(6)

print("--- Secure Authentication ---")
print(f"Your mobile verification code is: {new_otp}")
print("This code expires in 3 minutes.")
