"""
Consider a very primitive login system.
Create a program that
a.Asks the user for a username and password
Only allows access if the username is “admin” and the password is “hunter2” (e.g. prints “Access Granted” or “Access Denied”)
"""

##part(a)

#put username and password
log_username = input("please enter a username >>>")
log_password = input("please enter a password >>>")

##part(b)
if(log_username == "admin" and log_password == "hunter2"):
    print("Access Granted!")
else:
    print("Error username or password ! Please try again")

