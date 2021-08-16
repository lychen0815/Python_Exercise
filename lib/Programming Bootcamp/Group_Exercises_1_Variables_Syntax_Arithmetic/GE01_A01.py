"""
Advanced Exercises

Write a program that takes (as input) a four letter word and prints to console the reverse of that word.
You may find helpful the documentation on string indexing - particularly the section on “Strings are Arrays”.
eg. for input “code”, the output should be “edoc”.

"""

letter_word = input("Please enter a four letter >>>")

#reverse this word

#method one
#reverse_word = letter_word[::-1]


#method two

reverse_word = ''.join(reversed(letter_word))
print("You enter a letter is " + letter_word + " , and reverse this word is " + reverse_word)

#method three
#reverse_word = letter_word[3] + letter_word[2] + letter_word[1] + letter_word[0]