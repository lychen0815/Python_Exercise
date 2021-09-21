"""
In this task, you will be implementing a more specific passcode-protected phone book class PasscodePhoneBook that inherits from PhoneBook class implemented above.

This class inherits all properties from PhoneBook class.

However, it has introduced:

passcode: instance variable, which is initialised in the constructor. You have to decide the datatype of it
validate_passcode(self): a method that asks the user to enter the passcode and compares it to the value stored in the passcode instance variable. This method will return True when the user input matches the passcode. It will return False otherwise.
Also, for all the methods under this class except __len__() and add_entry(), it has to validate the passcode from user input before performing the original operations. If the passcode entered is not correct, an error message will be printed out and the method will return False.
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

class PasscodePhoneBook(PhoneBook):
    def __init__(self,passcode):
        self.passcode = passcode
        super().__init__()

    def validate_passcode(self):
        user_input = input("Please enter passcode: ")
        return user_input == self.passcode

    def remove_entry(self,name,organization):
        if not self.validate_passcode():
            print("Invalid passcode.")
            return False
        return super().remove_entry(name,organization)

    def search_byname(self,name):
        if not self.validate_passcode():
            print("Invalid passcode.")
            return False
        super().search_byname(name)

    def __str__(self):
        if not self.validate_passcode():
            print('Invalid passcode.')
            return False
        return super().__str__()


c1 = Contact('Tom','Melbourne',['0425685212','0464545464'])
c2 = Contact('Jerry','Monash',['042568524'])
pass_phone_book = PasscodePhoneBook('1234567')
pass_phone_book.add_entry(c1)
pass_phone_book.add_entry(c2)
print(pass_phone_book)




















