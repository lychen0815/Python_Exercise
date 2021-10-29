"""
Q1: This question is about Classes and Objects.
Create a class named Bank, which has attributes Account Number, Account Name, Balance, Address. It will be performing transactions between 2 accounts, checking the balance, withdrawing, changing the account name, and passbook. Complete the following code template for the Bank class:

Transaction - removes funds from the bank account and sends it to another account. Check Balance - check the balance of the account holder. Withdraw - withdraws the amount from the account holder, and if withdrawal amount is higher than balance it should be rejected (return False). Change Name - should allow users to change the name. Passbook - should print all the current details of account holder into a file.
"""

class Bank:
    def __init__(self,acc_no,acc_name,balance,address):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.balance = balance
        self.address = address

    def check_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            return True

    def change_acc_name(self,new_name):
        self.acc_name = new_name
        return self.acc_name

    def transaction(self,other,amount):
        self.balance = self.balance - amount
        other.balance = other.balance + amount
        return other.balance

    def passBook(self, filename):
        account_info = "Account number: " + str(self.acc_no) + "\nAccount name: " + self.acc_name + "\nBalance: " + str(self.balance) + "\nAddress: " + self.address
        with open(filename,'w') as output_file:
            output_file.write(account_info)
        print(account_info)


bank1 = Bank(123,'Melbourne bank',100,"Australia Melbourne")
bank2 = Bank(133,'Monash Bank',200,'Clayton')

bank1.passBook("output.txt")