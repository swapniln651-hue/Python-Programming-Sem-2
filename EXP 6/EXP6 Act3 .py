#Copy backup data from one file to another.
"""
Created on Mon Mar 23 15:59:24 2026

@author: swapnil
"""

# Source file (original data)
source_file = "source.txt"

# Destination file (backup file)
backup_file = "backup.txt"

try:
    # Open source file in read mode
    with open(source_file, "r") as src:
        data = src.read()

    # Open destination file in write mode
    with open(backup_file, "w") as dest:
        dest.write(data)

    print("Backup completed successfully!")

except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("An error occurred:", e)
