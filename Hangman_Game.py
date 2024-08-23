#Description: This program will be a hangman game where the user will have to guess a word in 12 turns
#Author: Nicole Galvan
#Date: 8/22/24
import random

def game():
    
    word_list = ["cheese"]
    word = [x for x in random.choice(word_list)]
    guesses = ["_" for x in word]
    letters_guessed = [] 
    turns = 1
 
    while turns <= 12:
        print(" ".join(letters_guessed))
        print(" ".join(guesses))

        char = input("What guess would you like to make?").lower()

        if char in letters_guessed:
            print(f"You've already guessed '{char}'. Try a different letter.")
            continue
    
        for x in word:
            if x == char:
                index = word.index(x)
                guesses[index] = char
                word[index] = "_"
    
        if char not in word and char not in guesses:
            letters_guessed.append(char)
    
        if "_" not in guesses:
            break
    
        turns += 1
    print("Hooray! You discovered the word " + "".join(guesses) + "!")

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
