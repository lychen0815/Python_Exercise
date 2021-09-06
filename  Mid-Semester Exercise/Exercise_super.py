#1.多继承的使用   (使用父类.__init__(self,XXX)）

class Human:
    def __init__(self,sex):
        self.sex = sex

    def p(self):
        print("this is human of p method")

class Person:
    def __init__(self,name):
        self.name = name
    def p(self):
        print("this is person of p method")
    def person(self):
        print("this is a person of person method")

class Teacher(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

class Student(Person,Human):
    def __init__(self,name,sex,grade):
        Person.__init__(self,name)
        Human.__init__(self,sex)
        self.grade = grade

class Son(Human, Teacher):
    def __init__(self,name,age,sex,fan):
        Human.__init__(self,sex)
        Teacher.__init__(self,name,age)
        self.fan = fan


son1 = Son('jordan',18,"male",'skating')
print(son1.name)