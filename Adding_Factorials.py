#Description: This program will find the sum of all the factorials of the inputted number
#Author: Nicole Galvan 
#Date: 8/14/24

factorial = int(input("Input the factorial"))
#starting inputs of the sum, product, and number list
sum_of_all = 0
number_list = []
product = 1

#This for loop will make a list of all the numbers from 1 to the input number
for x in range(1, factorial + 1):
    number_list.append(x)

#This for loop mulitiplies every number (factorials) and adds the product to the sum at every iteration
for x in number_list:
    product *= x
    sum_of_all += product

print(sum_of_all)



