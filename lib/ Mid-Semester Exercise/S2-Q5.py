'''
Write a python program to create a class “Student”, which would allow user to enter and store student's information including Name, ID, and list of marks achieved by the student in the specific unit.

This Student class contains:

instance variables required to represent each individual student data. A student should contain:

name, as a string
id as a integer
marks, can be implemented as a dictionary
a collection of methods defined for manipulating a student's contact:

__init__ : Contructor method.
update_mark: method to update the mark of the specif unit.
avg_mark: method to return the average mark of the student.
__str__: use to print all the details of the student in a proper format.
__eq__: use to check if the two objects of student class are same or not.
IMPORTANT After completing the class, you have to test the functionality of each method.
'''
class Student():
    def __init__(self,name,ID,marks):
        self.stud_name = name
        self.stud_ID = ID
        self.stud_marks = marks

    def update(self,unit,mark):
        self.stud_marks[unit] = mark

    def avg_mark(self):
        total_mark = 0
        unitCount = len(self.stud.marks)

        for key,value in self.stu_marks.items():
            total_mark += value
        avg = total_mark / unitCount
        return avg

    def __str__(self):
        std_info = "ID: " + str(self.stud_ID)
        std_info += "\nName: " + self.stud_name
        std_info += "\nMarks: " + str(self.stud_marks)
        return std_info

    def __eq__(self,other):
        if isinstance(other,Student):
            if self.stu_ID == other.study_ID and self.stud.name == other.stud.name:
                return True
            else:
                return False




student3 = Student("shirin", 11111, {"Python": 50, "Java": 60, "C+": 80})
student3.update("Python",100)
print(student3)












