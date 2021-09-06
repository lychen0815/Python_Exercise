'''
2.使用super调用父类中的方法
多重继承应该用（父类.__init__(self,XXX)），而不是使用super方法，容易重复调用
如果非要使用super的话，要加不定长参数
'''

class Human:
    def __init__(self,sex,*args, **kwargs):# 为避免多继承报错，使用不定长参数，接受参数
        self.sex = sex
    def p(self):
        print("this is human of p method")

class Person:
    def __init__(self,name,*args,**kwargs):# 为避免多继承报错，使用不定长参数，接受参数
        self.name = name
    def p(self):
        print("this is person of p method")
    def person(self):
        print("this is a person of person method")

class Teacher(Person):
    def __init__(self,name,age,*args, **kwargs): # 为避免多继承报错，使用不定长参数，接受参数
        super().__init__(name, *args, **kwargs) # 为避免多继承报错，使用不定长参数，接受参数
        self.age = age


class Son(Human, Teacher):
    def __init__(self,name,age,sex,fan):
        super().__init__(name,age,sex)
        self.fan = fan

son1 = Son('jordan',18,"male",'skating')
print(son1.fan)