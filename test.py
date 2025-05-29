"""
Module for managing student grades and reporting.
"""

class Student:
    """
    Represents a student with grades and academic performance tracking.
    """

    def __init__(self, student_id, name):
        # Validate name and ID are not empty
        if not student_id or not name:
            print("Error: Student ID and name cannot be empty")
            self.student_id = "INVALID"
            self.name = "INVALID"
        else:
            self.student_id = student_id
            self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "NO"

    def add_grades(self, grade):
        """
        Add a grade to the student's record with validation
        """
        try:
            grade_float = float(grade)
            if 0 <= grade_float <= 100:
                self.grades.append(grade_float)
                self._update_status()  # Update pass/fail and honor status
            else:
                print(f"Error: Grade {grade} must be between 0-100")
        except (ValueError, TypeError):
            print(f"Error: Grade {grade} must be a numeric value")

    def calculate_average(self):
        """
        Calculate the average of the student's grades.
        """
        if len(self.grades) > 0:
            total = sum(self.grades)
            avg = total / len(self.grades)
            return avg
        return 0

    def check_honor(self):
        """
        Check if the student qualifies for honors based on average grade.
        """
        if self.calculate_average() >= 90:
            self.honor = "YES"
        else:
            self.honor = "NO"
        return self.honor

    def delete_grade(self, index):
        """
        Delete a grade from the student's record by index with validation.
        """
        if 0 <= index < len(self.grades):
            removed_grade = self.grades.pop(index)
            self._update_status()
            print(f"Removed grade: {removed_grade}")
        else:
            print(f"Error: Index {index} out of range. Valid range: 0-{len(self.grades)-1}")

    def report(self):
        """
        Print a comprehensive report of the student's information and grades.
        """
        self._update_status()  # Ensure status is current
        avg = self.calculate_average()
        letter_grade = self._get_letter_grade()
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Grades: " + str(self.grades))
        print("Average Grade: " + str(round(avg, 2)))
        print("Letter Grade: " + letter_grade)
        print("Pass/Fail Status: " + self.is_passed)
        print("Honor Roll Status: " + self.honor)

    def _update_status(self):
        """
        Update pass/fail and honor status based on current average.
        """
        avg = self.calculate_average()
        self.is_passed = "PASSED" if avg >= 60 else "FAILED"
        self.honor = "YES" if avg >= 90 else "NO"

    def _get_letter_grade(self):
        """
        Convert average grade to letter grade.
        """
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def remove_grade_by_value(self, grade_value):
        """
        Remove first occurrence of a specific grade value.
        """
        try:
            grade_float = float(grade_value)
            if grade_float in self.grades:
                self.grades.remove(grade_float)
                self._update_status()
                print(f"Removed grade: {grade_value}")
            else:
                print(f"Error: Grade {grade_value} not found in student's grades")
        except (ValueError, TypeError):
            print(f"Error: {grade_value} is not a valid grade value")


def start_run():
    """
    Main function to run the student grade management system.
    """
    # Test with valid student
    student = Student("S001", "John Doe")
    # Add valid grades
    student.add_grades(100)
    student.add_grades(85)
    student.add_grades(95)
    # Test invalid inputs
    student.add_grades("Fifty")  # Will show error message
    student.add_grades(150)      # Will show error message
    student.add_grades(-5)       # Will show error message
    # Add more valid grades
    student.add_grades(92)
    student.calculate_average()
    student.check_honor()
    # Test safe grade deletion
    student.delete_grade(0)      # Valid deletion
    student.delete_grade(10)     # Will show error message
    # Test grade removal by value
    student.remove_grade_by_value(85)    # Valid removal
    student.remove_grade_by_value(999)   # Will show error message
    student.report()

start_run()
