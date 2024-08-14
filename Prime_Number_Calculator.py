#Description: This program will determine if the input number is a prime number
#Author: Nicole Galvan 
#Date: 8/14/24

user_number = int(input("Lets check if this is a prime number!"))
factor_list = []
if user_number > 0:#first to check if the number is positive
    for x in range(2, user_number ):#iterates through every number to see if the number has factors
        if user_number % x == 0:
            factor_list.append(x)

if len(factor_list) == 0:#checks if number has any factors
    print(str(user_number) + " is a prime number")
else:
    print(factor_list)