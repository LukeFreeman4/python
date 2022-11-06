import random


def start_game():
    player_name = input('What is your name? ')
    print('Hello, ' + player_name + '. Welcome to "Rock, Paper, Scissors game" \n' 
        'If you would like instructons please type the lettier "i"\n' 
        'to quit the game type "q"')


#Get player input
#computer choice
#compare computer choice with player choice
#choose winner
#keep track of score

def player_choice():
    return input("Please choose 'Rock', 'Paper', or 'Scissors ").lower()


def computer_choice():
    choice_list = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice_list)
    return computer_choice

wins = 0
ties = 0
loss = 0

if player_choice() == "i":
    print("Instructions to be typed here")
elif player_choice() == "q":
    pass
    
