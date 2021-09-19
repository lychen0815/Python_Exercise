'''
1. Try-Except
Below is a simplified implementation of Contact class from last week. Please identify all possible errors and use try-except blocks to raise and catch the errors.
'''


class Contact:
    def __init__(self, name, organisation, phones=[]):
        """
        Construct all attributes of the instance. (No need to modify this part)
        """
        try:
            if not isinstance(name, str):
                raise TypeError('name should be a string!')
            self.name = name
        except TypeError as e:
            print(e)
            self.name = ''

        try:
            if not isinstance(organisation, str):
                raise TypeError('organisation should be a string!')
            self.organisation = organisation
        except TypeError as e:
            print(e)
            self.organisation = ''

        try:
            if not isinstance(phones, list):
                raise TypeError('phones should be a list of string!')
            self.phones = [p for p in phones if self.validate_phone(p)]
        except TypeError as e:
            print(e)
            self.phones = []

    def validate_phone(self, num):
        """
        A method to validate phone number. (No need to modify this part)
        Args:
            1. num: the phone number needs to be validated
        Returns:
            bool: whether num is a valid phone number
        """
        return isinstance(num, str) and len(num) in range(10, 15) and num.isdigit()

    def match_name(self, substr):
        """
        See if the name starts with substr(case-insensitive)
        Args:
            1. substr(str): the string to test whether name is starting with
        Returns:
            bool: whether self.name is starting with substr
        """
        return self.name.lower().startswith(substr.lower())

    def update_phone(self, index, new_phone):
        """
        Update the phone number in at certain index.
        Args:
            1. index(int): the index of the phone list that needs update
            2. new_phone(str): the new phone number value
        """
        self.phones[index] = new_phone

    def __str__(self):
        """
        Usage:
            str(self)
        Returns:
            str: the string representation of the instance
        """
        formatted_str = """Name: {}
Organisation: {}
Phone Number(s):
{}"""
        return formatted_str.format(self.name, self.organisation, '\n'.join(self.phones))

    def __eq__(self, other):
        """
        Compares the name and organisation between two Contact instances and see if they are equal
        Usage:
            self == other
        Returns:
            bool: whether the name and organisation of two Contact instances are equal
        """
        return self.name.lower() + self.organisation.lower() == other.name.lower() + other.organisation.lower()

    def __lt__(self, other):
        """
        Compares the name and organisation between two Contact instances based on the lexicographic order and see if the name and organisation of self is ordered in front of other
        Usage:
            self < other
        Returns:
            bool: whether the name and organisation of self has a higher order than (in front of) other
        """
        return self.name.lower() + self.organisation.lower() < other.name.lower() + other.organisation.lower()

    def __gt__(self, other):
        """
        Compares the name and organisation between two Contact instances based on the lexicographic order and see if the name and organisation of self is ordered after other
        Usage:
            self < other
        Returns:
            bool: whether the name and organisation of self has a lower order than (after) other
        """
        return self.name.lower() + self.organisation.lower() > other.name.lower() + other.organisation.lower()