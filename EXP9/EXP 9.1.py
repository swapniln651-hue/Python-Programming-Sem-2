# using the math module to calculate square root,power, and trigonometric functions.
"""
Created on Mon Apr 20 14:33:24 2026

@author: swapnil
"""
import math

num = float(input("Enter a number for square root and power calculation: "))
power = float(input("Enter the exponent value: "))
angle_deg = float(input("Enter an angle in degrees for trigonometric functions: "))

sqrt_value = math.sqrt(num)
print(f"Square root of {num} is {sqrt_value}")

power_value = math.pow(num, power)

77

print(f"{num} raised to the power {power} is {power_value}")

angle_rad = math.radians(angle_deg)

sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)
print(f"Sin({angle_deg}°) = {sin_value}")
print(f"Cos({angle_deg}°) = {cos_value}")
print(f"Tan({angle_deg}°) = {tan_value}")
