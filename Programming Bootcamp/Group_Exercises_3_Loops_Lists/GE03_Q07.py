"""
Create a program that helps a user store their shopping list.
a.Prompt the user for items until the user enters “done”
b.Store the items and then display them to the user at the end
c.Extension: Display the items on separate lines with a numeric index. E.g.
1.Apples
2.Chocolate
3.Introduction to Algorithms 3rd Edition
"""
shopping_list = []

user_input = input('please enter item name >>>')

while user_input != "done":
    shopping_list.append(user_input)
    user_input = input("Enter item name >>>")
print("Shopping list:", shopping_list)

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(i+1,".", item)