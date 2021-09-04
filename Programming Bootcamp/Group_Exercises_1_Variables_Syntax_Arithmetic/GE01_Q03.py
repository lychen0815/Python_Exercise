"""
Write a program that
a.Asks the user for their name (e.g. “What is your name?” “John”).
b.Asks the user for their age, using their name (e.g. “How old are you, John?” “18”)
c.Display a message to them telling them how old they’ll be in 10 years (e.g. “You will be 28 in 10 years”)
"""

##Part(a)

#ask user name and print it
user_name = input("What is your name? Please enter it >>>")
#print(user_name)

##Part(b)

#ask user age
user_age = input("How old are you, " + user_name + "? Please enter it >>>")
#print(user_age)


## Part(c)

#calculate user age after 10 years
user_age2 = int(user_age) + 10
print("You will be " + str(user_age2) + " in 10 years")
