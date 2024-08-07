#Description: This is a basic calculator program that will perform addition
#subtraction, division, and mulitplication with two user inputs
#Author: Nicole Galvan
#Date: 08/05/24

print("---------- BASIC CALCULATOR ----------")
print("-------Enter two number inputs-------")
print('''        ------OPERATIONS-------
               +)add
               -)subtract
               /)divide
               *)multiply
               **)exponent
               //)floor division''')
print("--------------------------------------")

numberOne = int(input("Enter First Number: "))
type_of_math = input("Math Operation: ")
numberTwo = int(input("Enter Second Number: "))


addition_variable = numberOne + numberTwo
subtraction_variable = numberOne - numberTwo
multiplication_variable = numberOne * numberTwo
division_variable = numberOne / numberTwo
exponent_variable = numberOne ** numberTwo
floor_division_variable = numberOne // numberTwo


if type_of_math == '+':
    print(addition_variable)
elif type_of_math == '-':
    print(subtraction_variable)
elif type_of_math == '/':
    print(division_variable)
elif type_of_math == '*':
    print(multiplication_variable)
elif type_of_math == '**':
    print(exponent_variable)
elif type_of_math == '//':
    print(floor_division_variable)
else:
    print("INVALID MATH TYPE")

