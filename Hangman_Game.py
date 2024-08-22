#Description: This program will be a hangman game where the user will have to guess a word in 12 turns
#Author: Nicole Galvan
#Date: 8/22/24
import random

word_list = ["cheese", "duck", "book", "telephone"]
word = random.choice(word_list)
guesses = "_"*len(word)
turns = 1
letters_guessed = []  

while turns <= 12:
    print(guesses)

    turns += 1



print(word)