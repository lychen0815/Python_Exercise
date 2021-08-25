#Lab Activity A
#2. Credit Card Validator

#let user input credit card number
credit_card = input("Please enter a credit card number:")

#Converts string inside the list to int
credit_card = list(map(int, credit_card))

#check the length of credit card
if 14 <= len(credit_card) <= 19:
    #Drop the last digit from the number
    last_digit = credit_card.pop(-1)
    #Reverse the numbers
    credit_card.reverse()

    #Multiply the digits in odd positions by 2
    for i in range(0,len(credit_card),2):
        credit_card[i] *= 2
    #subtract 9 to all any result higher than 9
    sub_list = []
    for item in credit_card:
        if item > 9:
            item = item - 9
        else:
            pass
        sub_list.append(item)
    #Add all the numbers together and Get the remainder of the sum divided by 10
    sum_num = sum(sub_list) % 10
    #Add remainder to last digit
    add_num = sum_num + last_digit
    #check the sum is divisible by 8
    if add_num % 8 == 0:
        print("The number is valid")
    else:
        print("The number is invalid.")


else:
    print("The number is invalid.")