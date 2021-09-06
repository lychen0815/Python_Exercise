class Student:
    def __init__(self,name,id,marks):
        self.name = name
        self.id = id
        self.marks = marks

    def update_mark(self,unit,mark):
        self.marks[unit] = mark

    def avg_mark(self):
        total_mark = 0
        unit_count = len(self.marks)
        for k,v in self.marks.items():
            total_mark += v
        avg_mark = total_mark / unit_count
        return avg_mark

    def __str__(self):
        stu_info = "This student name is: " + str(self.name)
        stu_info += "\nID: " + str(self.id)
        stu_info += "\nMarks: " + str(self.marks)
        return stu_info

    def __eq__(self,other):
        if isinstance(other,Student):
            if self.name == other.name and self.id == other.id:
                return True
            else:
                return False
        else:
            return False

student1 = Student("jordan","1234785",{'python':100,'java':101})
#student3 = Student("jordan1","1234785",{'python':100,'java':101})
#student1.update_mark("Language",100)
print(student1)