#Description: This program is a little funny mad libs story meant to
#ask the user for different words to complete the story
#Author: Nicole Galvan
#Date: 08/05/24


print('This is the start of your Mad Libs, enjoy!')

noun_1 = input("noun: ")
adjective_1 = input("adjective: ")
verb_1 = input("verb: ")
adverb_1 = input("adverb: ")
number_1 = input("number: ")
place_1 = input("place: ")
noun_2 = input("plural noun: ")
adjective_2 = input("adjective: ")
verb_2 = input("past tense verb: ")
silly_word = input("silly word: ")

#This completes the user input for the Mad Lib

nounToPlural = noun_1 + "s"
print("Here you go!")

MadLib = '''Once upon a time, in the {} land of {}, there was
a {}. This {} wasn't like any other {}; it had {} {} across
the sky. One day, it decided to visit a place where there were
exactly {} {} {}. The {} {} {} at the sight of them and
decided to stay for a while. In this place, everyone
loved to {}. The end!'''

print(MadLib.format(adjective_1, place_1, noun_1, noun_1, nounToPlural, verb_1, \
adverb_1, number_1, adjective_2, noun_2, noun_1, adverb_1, verb_2, silly_word ))





