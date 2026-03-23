# Create a student attendance file and append new records
"""
Created on Mon Mar 23 15:30:34 2026

@author: swapnil
"""

import csv
import os
from datetime import datetime

FILE_NAME = "attendance.csv"

def initialize_file():
    """Creates the file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Student Name", "Status"])
        print(f"📁 Created new file: {FILE_NAME}")

def mark_attendance(name, status):
    date_today = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_today, name, status])
    print(f"✔️ Recorded: {name} is {status}")

# --- Execution ---
initialize_file()

print("\n--- Student Attendance Logger ---")
student_name = input("Enter Student Name: ")
# Basic validation for status
attendance_status = input("Enter Status (Present/Absent/Late): ").capitalize()

mark_attendance(student_name, attendance_status)
