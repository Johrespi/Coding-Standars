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
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, grade):
        """
            Add a grade to the student's record
        """
        self.gradez.append(grade)

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
