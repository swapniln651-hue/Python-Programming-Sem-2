# code for EMI calculation-
"""
Created on Mon Feb 16 15:58:29 2026

@author: swapnil
"""
principal=float(input("Enter principal amount:"))
monthlyintrest=float(input("Enter monthly intrest:"))
year=float(input("Enter loan tenure (in years):"))
months = year * 12
monthlyintrest = monthlyintrest /100
emi= (principal * monthlyintrest * (1 + monthlyintrest)** months) / ((1 + monthlyintrest))
print("your emi is:", round(emi, 2))

