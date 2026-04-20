# program using the date time module to print the currentdate, time, and weekday.
"""
Created on Mon Apr 20 14:38:04 2026

@author: swapnil
"""

import datetime
now = datetime.datetime.now()

print("Current Date:", now.strftime("%Y-%m-%d"))

print("Current Time:", now.strftime("%H:%M:%S"))


print("Weekday:", now.strftime("%A"))
