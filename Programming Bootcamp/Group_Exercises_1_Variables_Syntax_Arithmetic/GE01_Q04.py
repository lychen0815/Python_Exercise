"""
You are in charge of ordering pizza for your fortnightly Dungeons & Dragons night.
Write a program that takes the number of people attending your DnD night, as well as the number of pizza slices you are ordering.
Output how many slices everyone gets after dividing the slices evenly (so everyone gets the maximum number). You as the organiser will receive the “left over” number of slices after the division.
How many slices of pizza will you get?
"""

#Receive the number of players and pizza slices
player_number = int(input("please enter player number >>>"))

slice_number = int(input("please enter slice number >>>"))

#player_getslice = int(slice_number / player_number)

# Integer division (//) outputs an int answer (i.e. the whole number) rather than a float value
player_getslice = slice_number // player_number

player_getLeftSlice = slice_number % player_number
print("The players get " + str(player_getslice) + " lices each, while you get the " + str(player_getLeftSlice) + " left over slices.")

