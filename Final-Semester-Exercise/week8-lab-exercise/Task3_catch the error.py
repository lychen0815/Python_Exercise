#Catch the Error

'''
class ContactA:
    def __init__(self,name,organization,phones=[]):
        self.name = name
        self.organization = organization
        try:
            assert isinstance(phones,list),'phones should be a list'
            self.phones = phones
        except AssertionError as e:
            print(e)
            self.phones = []
c1 = ContactA('a','b','x')
'''
class ContactT:
    def __init__(self,name,organization,phones = []):
        self.name = name
        self.organization = organization
        try:
            if not isinstance(phones,list):
                raise TypeError('phones should be a list')
        except TypeError:
            self.phones = []
c2 = ContactT('a','b','c')
