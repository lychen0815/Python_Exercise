'''
Modify the program from advanced exercises 2 to allow for an input word of any length.

a.Now allow the user to input several separate words, and check if each of them is a palindrome. It should repeatedly prompt the user to enter a word until the user enters “done”. It should then print out the total number of palindromes the user entered, as well the list of palindromes (with each word on a separate line)
'''

words = []
user_input = input("please enter a word: ")

while user_input != "done":
    words.append(user_input)
    user_input = input("please enter a word: ")

palindromes = []

for word in words:
    reversed_word = ""
    for i in range(len(word)-1,-1,-1):
        reversed_word = reversed_word + word[i]
    if reversed_word == word:
        palindromes.append(word)
num_palindromes = str(len(palindromes))
print("Number of palindromes entered: " + num_palindromes)

for palindrome in palindromes:
    print(palindrome)