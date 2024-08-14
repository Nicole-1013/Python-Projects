#Description:This program will evaluate if a year was a leap year
#Author: Nicole Galvan
#Date: 8/14/24

input_year = int(input("What year would you like to input?"))
leap_year = False

if input_year % 4 == 0: #checks if the year is perfectly divisible by 4
    if input_year % 100 == 0: #checks if there are two zeros at the end of the year
        if input_year % 400 == 0:#checks if it is the exception to the two zero rule
            leap_year = True
        elif input_year % 400 > 0:#checks if it is not divisible byb 4
            leap_year = False
    elif input_year % 100 != 0:#checks if it is divisible by 4 but not by 100
        leap_year = True
else:
    leap_year = False #this shows that the year is not divisible by 4

if leap_year == True:
    print("This is a leap year")
else:
    print("This is not a leap year")    
    
