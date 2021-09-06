#单继承使用super调用父类方法


class Parent:
    def __init__(self,name):
        self.name = name


class Son1(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age


class Grandson(Son1):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender = gender


grandSon = Grandson('jordan',18,'male')
print(grandSon.age,grandSon.gender)