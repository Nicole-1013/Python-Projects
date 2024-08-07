#Description: This program will determine the exact amount of pizzas needed for each order depending on how many people the food is for, and without any leftover slices
#Author: Nicole Galvan 
#Date: 08/07/24

party_size = int(input("🎉How many people are in your party?🎉"))

small_pizza_capacity = 1
medium_pizza_capacity = 3
large_pizza_capacity = 7
#This represents how many people can eat each pizza slice

number_of_large_pizzas = 0
number_of_medium_pizzas = 0
number_of_small_pizzas = 0

if party_size // large_pizza_capacity > 0:
    number_of_large_pizzas = party_size // large_pizza_capacity
    party_size = party_size % large_pizza_capacity


if party_size // medium_pizza_capacity > 0:
     number_of_medium_pizzas = party_size // medium_pizza_capacity
     party_size = party_size % medium_pizza_capacity


if party_size // small_pizza_capacity > 0:
     number_of_small_pizzas = party_size

final_statement = '''You will need:
~{} Large Pizzas 🍕~
~{} Medium Pizzas 🍕~
~{} Small Pizzas 🍕~'''

print(final_statement.format(number_of_large_pizzas, number_of_medium_pizzas, number_of_small_pizzas))

