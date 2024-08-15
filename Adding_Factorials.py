#Description: This program will find the sum of all the factorials of the inputted number
#Author: Nicole Galvan 
#Date: 8/14/24

factorial = int(input("Input the factorial"))
sum_of_all = 0
number_list = []
product = 1

for x in range(1, factorial + 1):
    number_list.append(x)

for x in number_list:
    product *= x
    sum_of_all += product

print(sum_of_all)



