"""Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order.
Each student object has the followig attributes: name (string), roll_number (string), and cgpa (float).
Test the functionwith different input lists of students."""

class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  # Syntax - lambda arg:exp
  return sorted_students
  

# Example usage:
students = [
    Student("Divya", "A126", 6.1),
    Student("jee", "A125", 7.1),
    Student("selvam","A124", 8.1),
    Student("kavi", "A123", 9.1),
    Student("Muthu", "A127", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))