import random
#Description: This program will find which numbers both lists have in common without duplicates, then print those numbers
#Author: Nicole Galvan 
#Date: 8/15/24

#Asks for the length of each list so the user can create custom lists
user_input_one = int(input("Enter the length of the first list!(Less than 100)"))
user_input_two = int(input("Enter the length of the second list!(Less than 100)"))

#These make the initial sample list
sample_list_one = [x for x in range(100)]
sample_list_two= [x for x in range(100)]

#takes sample lists and creates a list based on the user input
list_one = random.sample(sample_list_one, user_input_one)
list_two = random.sample(sample_list_two, user_input_two)

#filtered common numbers into list
new_list = [x for x in list_one if x in list_two] 
newer_list = []

#second filter getting rid of any duplicates in new_list
for x in new_list:
    if x not in newer_list:
        newer_list.append(x)

print(newer_list)
print(list_one)
print(list_two)
