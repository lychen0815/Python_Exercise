"""
Task 1: The Contact Class
The first task is to create a Python class, called Contact, which contains:

instance variables required for this Contact class to represent each individual contact data. A contact should contain:

name, as a string
organisation as a string
phone numbers, can be implemented as a list
a collection of methods defined for manipulating a person's contact:

__init__ : Contructor method
update_name: method to update the name of the person
match_name: accepts a string as an argument, and return True if the string was a prefix of the name of the person, or False if it is not.
update_organisation: method to update the organisation of the person
add_phone: adding a phone number
remove_phone(self, index): remove the phone number on the position of index.
update_phone(self, index, new_phone): update the phone number on index to new_phone.
Overriding magic methods:
__str__: use to format the output of the contact represented in this Contact class.
__eq__: use to specific whether two contacts are equal. In this simple task, assume that two contacts are consider to be equal, if both contacts have the same name and organisation, CASE INSENSITIVE.
__lt__, __gt__: use to specify whether one conact is smaller than or larger than the other contact, based on the lexicographic order (CASE INSENSITIVE) based on the name, followed by the organisation. These would be useful when we sort a list of contacts.
"""


class Contact:
    def __init__(self,name,organization,phones = []):
        self.name = name
        self.organization = organization
        self.phones = phones

    def update_name(self,name):
        self.name = name

    def match_name(self,str):
        if self.name.lower().startswith(str.lower()):   #covert to lowercase
            return True
        else:
            return False

    def update_organization(self,organization):
        self.organization = organization

    def add_phone(self,new_phone):
        self.phones.append(new_phone)

    def remove_phone(self,index):
        if index in range(0,len(self.phones)):
            del self.phones[index]
            return True
        else:
            return False

    def update_phone(self,index,new_phone):
        if index in range(0,len(self.phones)):
            self.phones[index] = new_phone
            return True
        else:
            return False



    # __str__(self): This is  the overloaded method that is useful for formatting the output of the contact represented in this Contact class.
    def __str__(self):
        formatted_str = "Name: " + self.name + "\nOrganization: " + self.organization + "\nPhone Number: "
        for phone in self.phones:
            formatted_str += "\n" + phone
        return formatted_str

    def __eq__(self, other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organization.lower()
        org_other = other.organization.lower()
        if name_self == name_other and org_self == org_other:
            return True
        else:
            return False

    def __lt__(self, other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organization.lower()
        org_other = other.organization.lower()
        if name_self < name_other:
            return True
        elif name_self == name_other:
            if org_self < org_other:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        name_self = self.name.lower()
        name_other = other.name.lower()
        org_self = self.organization.lower()
        org_other = other.organization.lower()
        if name_self > name_other:
            return True
        elif name_self == name_other:
            if org_self > org_other:
                return True
            else:
                return False
        else:
            return False

c1 = Contact('zack','Monash',['0425685212','0464545464'])
c2 = Contact('Lily','Monash',['0425685212'])

contact_list = [c1,c2]
# we sort the list of contact, happened in place
contact_list.sort()
# now printing out the contacts one by one again, and see the difference!
for c in contact_list:
    print(c)

print('-------------------')
print(contact_list.index(Contact('zack','Monash')))




