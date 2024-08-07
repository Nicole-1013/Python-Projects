#Description: This program uses a list of nouns that iterates through funny sentences
#Author: Nicole Galvan
#Date: 08/06/24
noun_list = []

for x in range(10):
    noun = input("Input a noun: ")
    noun_list.append(noun)

for x in noun_list:
    print(f'While I was watching my favorite TV show about the {x}, a {x} suddently appeared next to me! Almost as the {x} came to life from the TV!')