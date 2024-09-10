#Description: This game will prompt the user to either play with two players, or with the computer, the computer will choose at random rock, paper, or scissors
#Author: Nicole Galvan
#Date: 9/9/24

import random
import os
move = ["r", "p", "s"]
play_again = 'y'
rounds = 1

def clear_console():
    if os.name == 'nt':
        os.system('cls')

def one_player_game():
    global rounds 
    player_points = 0
    computer_points = 0
    while rounds <= 3:
        player = input("Choose Action (Rock: r, Paper: p, Scissors: s)").lower()
        computer = random.choice(move)




def two_player_game():
    global rounds
    global move
    player_1_points = 0
    player_2_points = 0
    while  rounds <=3:
        print(f"POINTS :  Player 1: {player_1_points}  |  Player 2: {player_2_points}")
        player_1 = input("Player 1: Choose Action (Rock: r, Paper: p, Scissors: s)").lower()
        player_2 = input("Player 2: Choose Action (Rock: r, Paper: p, Scissors: s)").lower()
        
        if player_1 not in move or player_2 not in move:
            clear_console()
            print("INVALID RESPONSE, TRY AGAIN")
            
            continue

        if player_1 == player_2:
            print("its a Tie!")
            continue
        elif (player_1 == "r" and player_2 == "p") or \
            (player_1 == "p" and player_2 == "s") or \
            (player_1 == "s" and player_2 == "r"):
            player_2_points += 1
            print(f"Player 2 won round {rounds}!")
        else:
            player_1_points += 1
            print(f"Player 1 won round {rounds}!")
        
        if player_1_points == 2 or player_2_points == 2:
            clear_console()
            if player_1_points > player_2_points:
                print("Player 1 is the Winner!")
            else:
                print('Player 2 is the Winner!')
            break
        
        rounds += 1

            
        
                

print("Welcome to Rock Paper Scissors!")

while play_again == 'y':
    user_input = input("Two player gamemode or One player gamemode? (2,1)")
    if user_input == '2':
        two_player_game()
    elif user_input == '1':
        one_player_game()
    else:
        print("INVALID RESPONSE, TRY AGAIN")
        continue
    
    play_again = input("Play Again? (y: yes, n: no)").lower()

    

    