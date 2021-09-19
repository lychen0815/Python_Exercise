
# Approach I: AssertionError
class ContactA:
    def __init__(self,name,organization,phones = []):
        self.name = name
        self.organization = organization
        assert isinstance(phones,list), 'phones should be a list'
        self.phones = phones

c1 = ContactA('a','b','c')


