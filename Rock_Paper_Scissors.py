#Description: This game will prompt the user to either play with two players, or with the computer, the computer will choose at random rock, paper, or scissors
#Author: Nicole Galvan
#Date: 9/9/24

import random
choice = ["rock", "paper", "scissors"]
play_again = 'y'
player_1 = ""
player_2 = ""
player_1_points = 0
player_2_points = 0

def one_player_game():
    print()
def two_player_game():
    
    player_1 = input("Player 2: Choose Action (Rock: r, Paper: p, Scissors: s)").lower()
    player_2 = input("Player 2: Choose Action (Rock: r, Paper: p, Scissors: s)").lower()

    if player_1 == player_2:
        print("its a Tie!")

print("Welcome to Rock Paper Scissors!")

while play_again == 'y':
    user_input = input(int("Two player gamemode or One player gamemode? (2,1)"))
    if user_input == 2:
        two_player_game()
    elif user_input == 1:
        one_player_game()
    else:
        print("INVALID RESPONSE, TRY AGAIN")
        continue
    
    play_again = input("Play Again? (y: yes, n: no)").lower()

    

    