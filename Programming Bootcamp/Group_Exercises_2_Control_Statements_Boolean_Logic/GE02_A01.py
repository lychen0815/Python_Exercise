'''
Create a program which tells a user whether a four letter input word is a palindrome. A palindrome is a string which is the same backwards as forwards.
eg. for input “list” output should be “The word is not a palindrome.”
      for input “deed” output should be “The word is a palindrome!”
Hint: see advanced exercise 1 from above.
a.Change your program so that the code handles invalid inputs – so that if a word is not four letters, an appropriate error message is printed rather than the code crashing.
eg. for input “racecar” the output should be “Invalid word length.”
'''

user_input = input("please a four letter >>>")
input_reverse = user_input[3] + user_input[2] + user_input[1] + user_input[0]

#check the input length
if(len(user_input) != 4):
    print("Input error!")
else:
    if (input_reverse == user_input):
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome")



