#Description: This program will be a hangman game where the user will have to guess a word in 12 turns
#Author: Nicole Galvan
#Date: 8/22/24
import random

def game():
    
    word_list = ["Cheese"]
    word = [x.lower() for x in random.choice(word_list)]
    guesses = ["_" for x in word]
    letters_guessed = [] 
    turns = 0
    max_turns = 12

    while turns <= max_turns:
        
        turns_left = max_turns - turns
        print(f"You have '{turns_left}' turns left ")
        print(f"Guessed letters: {' '.join(letters_guessed)}")
        print("Word: " + " ".join(guesses))

        char = input("What guess would you like to make?").lower()

        if char in letters_guessed or char in guesses:
            print(f"You've already guessed '{char}'. Try a different letter.")
            continue
        
        if char in word:    
            for index, letter in enumerate(word):
                if letter == char:
                    guesses[index] = char
                    word[index] = "_"
    
        else:
            letters_guessed.append(char)
    
        if "_" not in guesses:
            print("Hooray! You discovered the word " + "".join(guesses) + "!")
            break
    
        turns += 1
    if "_" in guesses:
        print(f"Out of turns! The word was {''.join([x if x != '_' else word_list[0][i] for i, x in enumerate(guesses)])}. Better luck next time!")
    

game()
game_on = True
while game_on:
    user_input = input("Play Again? (y: yes, q: quit) ").lower()  # Convert input to lowercase for consistency
    
    if user_input == "y":
        game()
    elif user_input == "q":
        game_on = False
    else:
        print("Invalid input, please enter 'y' to play again or 'q' to quit.")
