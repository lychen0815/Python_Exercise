"""
Rock, Paper, Scissors is a very simple 2-player game. In each round, every player needs to throw either rock, paper or scissors. The rules of the game are as follows:

rock wins scissors
paper wins rock
scissors wins paper
draw if both players throw the same thing
The players will need to play 3 rounds and whoever wins at least 2 rounds is considered as the winner. As a result, there might be no winner at all after 3 rounds.

You will receive a list of 3 game round results in the form of list of 3 tuples. Each tuple represents a game round. The first item of the tuple is what the player 1 throws, while the second item of the tuple is what the player 2 throws.

In the list, '0' represents rock, '5' represents paper, '2' represents scissors.

Below is an example of the list:

games = [('2','5'),('5','5'),('0','2')]
Now, please write a function def rps_analyse(games): that:

analyses the game list(games)
prints out "Player 1 wins" if player 1 wins.
prints out "Player 2 wins" if player 2 wins.
prints out "Draw" if no one wins.
From the example list above, the function will print out "Player 1 wins", because player 1 won the first and the last rounds(2 rounds).
"""
def rps_analyse(games):
    player1 = 0
    player2 = 0
    for each_game in games:
        if each_game[0] == '0':
            if each_game[1] == "2":
                player1 += 1
            if each_game[1] == "5":
                player2 += 1
        elif each_game[0] == '2':
            if each_game[1] == "5":
                player1 += 1
            if each_game[1] == "0":
                player2 += 1
        elif each_game[0] == '5':
            if each_game[1] == "0":
                player1 += 1
            if each_game[1] == "2":
                player2 += 1
    if player1 >= 2:
        print("Player 1 wins")
    elif player2 >= 2:
        print("Player 2 wins")
    else:
        print("Draw")

rps_analyse(games = [('2','5'),('5','5'),('0','2')])





















