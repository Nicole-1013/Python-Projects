#Description: This program will be a hangman game where the user will have to guess a word in 12 turns
#Author: Nicole Galvan
#Date: 8/22/24
import random

word_list = ["cheese"]
word = [x for x in random.choice(word_list)]
guesses = ["_" for x in word]
turns = 1
letters_guessed = []  
print(word)
while turns <= 12:
    print(" ".join(letters_guessed))
    print(" ".join(guesses))
    char = input("What guess would you like to make for turn " + str(turns))
    for x in word:
        if x == char:
            index = word.index(x)
            guesses[index] = char
            word[index] = "_"
    if char not in word and char not in guesses:
        letters_guessed.append(char)
    turns += 1



