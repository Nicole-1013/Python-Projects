#Description: This is a basic calculator program that will perform addition
#subtraction, division, and mulitplication with two user inputs
#Author: Nicole Galvan
#Date: 08/05/24

print("---------- BASIC CALCULATOR ----------")
print("-------Enter two number inputs-------")
print('''        ---------MENU----------
               add
               subtract
               divide
               multiply''')
print("--------------------------------------")

type_of_math = input("Math Type: ")
numberOne = int(input("Enter Number: "))
numberTwo = int(input("Enter Number: "))


addition_variable = numberOne + numberTwo
subtraction_variable = numberOne - numberTwo
multiplication_variable = numberOne * numberTwo
division_variable = numberOne / numberTwo

if type_of_math == 'add':
    print(addition_variable)
elif type_of_math == 'subtract':
    print(subtraction_variable)
elif type_of_math == 'divide':
    print(division_variable)
elif type_of_math == 'multiply':
    print(multiplication_variable)
else:
    print("INVALID MATH TYPE")

