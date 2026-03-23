# program for Store daily expenses in a file and calculate total monthly expense
"""
Created on Mon Mar 23 15:26:12 2026

@author: swapnil
"""

import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense(amount, description):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print(f"✅ Saved: {amount} for {description}")

def calculate_monthly_total(month_year):
    """month_year format should be 'YYYY-MM'"""
    total = 0.0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if the row date starts with the requested YYYY-MM
                if row[0].startswith(month_year):
                    total += float(row[2])
    except FileNotFoundError:
        return 0.0
    return total

# --- Simple Menu ---
print("--- Daily Expense Tracker ---")
action = input("Type 'add' to log an expense or 'total' to see monthly spend: ").lower()

if action == "add":
    amt = input("Amount: ")
    desc = input("Description: ")
    add_expense(amt, desc)
elif action == "total":
    target = input("Enter month (YYYY-MM): ")
    result = calculate_monthly_total(target)
    print(f"💰 Total for {target}: {result:.2f}")
