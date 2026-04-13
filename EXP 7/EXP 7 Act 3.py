# Create a Student class that calculates grade
"""
Created on Mon Apr 13 15:33:28 2026

@author: swapnil
"""

class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
        else:
            print("Invalid score! Please enter a value between 0 and 100.")

    def calculate_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_letter_grade(self):
        avg = self.calculate_average()
        
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_report(self):
        avg = self.calculate_average()
        grade = self.get_letter_grade()
        print(f"\n--- Progress Report: {self.name} ---")
        print(f"Scores: {self.scores}")
        print(f"Average: {avg:.2f}")
        print(f"Final Grade: {grade}")

# --- Interactive Section ---

student_name = input("Enter student name: ")
student = Student(student_name)

while True:
    print("\n1. Add Score")
    print("2. Show Report")
    print("3. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        try:
            val = float(input("Enter score (0-100): "))
            student.add_score(val)
        except ValueError:
            print("Please enter a valid number.")
            
    elif choice == '2':
        student.display_report()
        
    elif choice == '3':
        print("Closing Gradebook.")
        break
    else:
        print("Invalid choice.")
