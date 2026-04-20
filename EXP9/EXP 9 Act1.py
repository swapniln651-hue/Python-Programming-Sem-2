#Use math module to calculate EMI interest.
"""
Created on Mon Apr 20 14:48:52 2026

@author: swapnil
"""

import math

def calculate_emi(p, annual_rate, years):
   
    r = annual_rate / (12 * 100)
   
   
    n = years * 12
   
   
    numerator = p * r * math.pow(1 + r, n)
    denominator = math.pow(1 + r, n) - 1
   
    emi = numerator / denominator
    return emi


principal = 100000      
rate = 12.5            
tenure = 2            

emi_result = calculate_emi(principal, rate, tenure)

print(f"Loan Amount: {principal}")
print(f"Annual Interest Rate: {rate}%")
print(f"Tenure: {tenure} years")
print(f"Monthly EMI: {round(emi_result, 2)}")
