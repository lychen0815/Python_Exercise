
#两个类之间的引用

"""
1. The PhoneBook class
In this task, you are required to implement another class that is responsible for handling a collection of contacts. Please note: in order to complete this task you required to use Task 1.

The following is a list of methods we have to implement:

__init__ : Constructor method
__len__: This is overloaded method that is commonly implement to return the number of items in the collection.
add_entry : This method will add a new item which is a Contact class object to the collection represented in this PhoneBook class
remove_entry(self, name, organisation): This method will remove the occurrences of the specific item (as indicated by name and organisation) from the contact collection represented in this PhoneBook class.
search_byname(self, name): The method is to search and print out contacts that are at least partically match the given name (CASE INSENTITIVE).
__str__(self): This is the overloaded method that is useful for formatting the output of the contact collection represented in this PhoneBook class. Construct a Python string which organises each item (according to ascending order) from the contact collection as a separate line in the output.
Consider time limitation, pesudocode is acceptable!
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


class PhoneBook():
    def __init__(self):
        self.contact_list = []

    def __len__(self):
        return len(self.contact_list)

    def add_entry(self,contact):
        if contact in self.contact_list:
            print("Duplicate entry")
            return False
        else:
            self.contact_list.append(contact)
            return True

    def remove_entry(self,name,organization):
        for i in range(0,len(self.contact_list)):
            if self.contact_list[i].name == name and self.contact_list[i].organization == organization:
                del self.contact_list[i]
                return True
        print('No such contact exit')
        return False

    def search_byname(self,name):
        match_contacts = [contact for contact in self.contact_list if contact.match_name(name)]
        for contact in match_contacts:
            print(contact)
        if match_contacts == []:
            print("No matching contact found")

    def __str__(self):
        formatted_str = ""
        for contact in sorted(self.contact_list):
            formatted_str = formatted_str + str(contact) + '\n'
        return formatted_str

c1 = Contact('Tom','Melbourne',['0425685212','0464545464'])
c2 = Contact('Jerry','Monash',['042568524'])

phone_book = PhoneBook()
#phone_book.add_entry(c1)
phone_book.add_entry(c2)
phone_book.search_byname('Jerry')



















