#Create an Employee class that calculates salary with bonus.
"""
Created on Mon Apr 13 15:24:38 2026

@author: swapnil
"""

class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_total_salary(self, bonus_percentage):
        bonus_amount = (bonus_percentage / 100) * self.base_salary
        total_salary = self.base_salary + bonus_amount
        return total_salary, bonus_amount

    def display_details(self, bonus_percentage):
        total, bonus = self.calculate_total_salary(bonus_percentage)
        print(f"\nEmployee: {self.name} (ID: {self.emp_id})")
        print(f"Base Salary: {self.base_salary:,.2f}")
        print(f"Bonus ({bonus_percentage}%):{bonus:,.2f}")
        print(f"Total Payable: {total:,.2f}")
        print("-" * 30)


name_input = input("Enter Employee Name: ")
id_input = input("Enter Employee ID: ")

try:
    salary_input = float(input("Enter Base Salary: "))
    bonus_pct_input = float(input("Enter Bonus Percentage: "))

   
    emp1 = Employee(name_input, id_input, salary_input)

    emp1.display_details(bonus_percentage=bonus_pct_input)

except ValueError:
    print("Error: Please enter a valid number for salary and bonus.")
