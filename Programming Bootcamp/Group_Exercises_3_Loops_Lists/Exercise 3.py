#Lab Activity A
#3.Sentiment Analyser

#import re and this module provides regular expression matching operations
import re
#let user input a sentence and convert String to List

user_input = input("Input:")

#initialize small letter
small_letter = 0
#initialize whole string
whole_string = 0

#Loop through each item
for item in user_input:
    #check the quantity in small letter
    if item.islower():
        small_letter += 1
    # check the quantity in whole thing
    if item.isalpha():
        whole_string += 1
# count calmness score
calmness_score = small_letter / whole_string
print("calmness score:",calmness_score)

#count excitement score
#re.IGNORECASE means case insensitive
excitement_score = len(re.findall('(?=wow)', user_input,re.IGNORECASE))

#check excitement score and print it
if excitement_score >= 0 and excitement_score < 3:
    print("excitement score: 0")
elif excitement_score >= 3 and excitement_score < 5 :
    print("excitement score: 3")
elif excitement_score >= 5:
    print("excitement score: 5")
