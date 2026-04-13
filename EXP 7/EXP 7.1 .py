# To implement Python programs using Object-Oriented Programming (OOP), specifically:
"""
Created on Mon Apr 13 15:00:36 2026

@author: swapnil
"""

class Employee:
     def __init__(self, name, emp_id, basic_salary):
         self.name = name
         self.emp_id = emp_id
         self.basic_salary = basic_salary 
         
     def calculate_gross_salary(self):
         hra = 0.2 * self.basic_salary
         da = 0.1 * self.basic_salary
         gross_salary = self.basic_salary + hra + da
         return gross_salary
     
     def display_details(self):
         print(f"Employee Name: {self.name}")
         print(f"Employee ID: {self.emp_id}")
         print(f"Basic Salary: {self.basic_salary}")
         print(f"Gross Salary: {self.calculate_gross_salary()}")


name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))

emp = Employee(name, emp_id, basic_salary)
print("\nEmployee Details:")
emp.display_details()
