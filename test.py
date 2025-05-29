"""
Module for managing student grades and reporting.
"""

class Student:
    """
    Represents a student with grades and academic performance tracking.
    """

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, grade):
        """
            Add a grade to the student's record
        """
        self.grades.append(grade)

    def calculate_average(self):
        """
        Calculate the average of the student's grades.
        """
        total = 0
        for grade in self.grades:
            total += grade
        if len(self.grades) > 0:
            avg = total / len(self.grades)
            return avg
        return 0

    def check_honor(self):
        """
            Check if the student qualifies for honors based on average grade.
        """
        if self.calculate_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        """
        Delete a grade from the student's record by index.
        """
        del self.grades[index]

    def report(self):  # broken format
        """
        Print a report of the student's information and grades.
        """
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + str(self.calculate_average()))


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
