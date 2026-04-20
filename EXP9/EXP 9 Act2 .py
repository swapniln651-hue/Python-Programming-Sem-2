# Display today’s date in a hospital appointment system.
"""
Created on Mon Apr 20 14:51:59 2026

@author: swapnil
"""

from datetime import datetime

def display_hospital_header():
    
    now = datetime.now()
    
    formatted_date = now.strftime("%A, %B %d, %Y")
    formatted_time = now.strftime("%I:%M %p")
    
    print("="*40)
    print("      CITY GENERAL HOSPITAL      ")
    print("    APPOINTMENT MANAGEMENT SYSTEM   ")
    print("="*40)
    print(f"Date: {formatted_date}")
    print(f"Time: {formatted_time}")
    print("-"*40)

display_hospital_header()

patient_name = input("Enter Patient Name: ")
print(f"\nChecking available slots for {patient_name} on {datetime.now().strftime('%Y-%m-%d')}...")
