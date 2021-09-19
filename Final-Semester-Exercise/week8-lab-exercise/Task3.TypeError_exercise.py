# Approach II: TypeError

class ContactT:
    def __init__(self,name,organization,phones = []):
        self.name = name
        self.organization = organization
        if not isinstance(phones,list):
            raise TypeError('phones should be a list')
        self.phones = phones

c2 = ContactT('a','b','c')