"""
5. Coffee Shop (4 Marks)
#Class #VariableScope

You are creating a new class StarucksBranch in python representing a coffee shop branch of an international coffee brand.

We have already known that every object of StarucksBranch shares the same company_name class variable value as 'Starucks'.

However, different StarucksBranch objects have unique branch_id variable values, which will be initialised using the argument of the constructor method and stored as an instance variable.

a) Please implement the class StarucksBranch with the following variables:

company_name as class variable
branch_id as instance variable
And the following class methods:

__init__: constructor of the class
"""
class StarucksBranch:
    company_name = 'Starucks'
    def __init__(self,branch_id):
        self.branch_id = branch_id




sb = StarucksBranch('001')

StarucksBranch.company_name
























