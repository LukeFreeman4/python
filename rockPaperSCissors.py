import random

wins = 0
ties = 0
loss = 0
number_games = 0

def start_game():
    player_name = input('What is your name? ')
    print('Hello, ' + player_name + '. Welcome to "Rock, Paper, Scissors game" \n' 
        'If you would like instructons please type the lettier "i"\n' 
        'to quit the game type "q"')

def instructions():
    print('HOW TO PLAY\n'
           'Type in your selection (Rock, Paper or Scissors)\n'
           'You choice will be played against the computer.'
           'Who ever wins the most matches will win the game')

def player_turn():
    return input("Please choose 'Rock', 'Paper', or 'Scissors ").lower()
    
def computer_turn():
    choice_list = ['rock', 'paper', 'scissors']
    return random.choice(choice_list)

def play_match():
    player_choice = player_turn()
    computer_choice = computer_turn()
    if  player_choice == 'i':
        instructions()    
    elif player_choice == computer_choice:
        print('Tie')
        ties +=1
        print(ties)
    elif player_choice == 'rock' and computer_choice != 'paper':
        print('Win')
        wins +=1
        print(wins)
    elif player_choice == 'paper' and computer_choice != 'scissors':
        print('Win')
        wins +=1
        print(wins)
    elif player_choice == 'scissors' and computer_choice != 'rock':
        print('Win')
        wins +=1
        print(wins)
    elif player_choice != 'rock' or player_choice != 'paper' or player_choice != 'scissors' or player_choice != 'i' or player_choice != 'q':
        print(f'Sorry, {player_choice} not a valid choice. Please choose Rock, Paper or Scissors')
        
    else: 
        print('lose')

def play_game():
    number_games = 0
    while number_games < 5:
        play_match()
        number_games +=1

play_game()