"""
5. Class and object
Write a python program to create a class “Student”, which would allow user to enter and store student's information including Name, ID, and list of marks achieved by the student in the specific unit.
"""

class Student:
    def __init__(self,name,id,marks = {}):
        self.name = name
        self.id = id
        self.marks = marks

    def update_mark(self,unit,mark):
        self.marks[unit] = mark

    def avg_mark(self):
        total_marks = 0
        for key,value in self.marks.items():
            total_marks += value
        unit_count = len(self.marks)
        average_mark = total_marks // unit_count
        return average_mark

    def __str__(self):
        str_info = "This student name is: " + str(self.name) + ", id: " + str(self.id) + ", Marks: " + str(self.marks)
        return str_info

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.id == other.id and self.name == other.name:
                return True
            else:
                return False
        else:
            return False

student1 = Student("shirin", 11111, {"Python":50, "Java":60, "C+":80})
student3 = Student("shirin", 11111, {"Python":50, "Java":60, "C+":80})
student2 = Student("lily", 11111, {"Python":10, "Java":10, "C+":10})

student1.update_mark("Python",100)
print(student1.avg_mark())
print(student1==student3)
print(student1)