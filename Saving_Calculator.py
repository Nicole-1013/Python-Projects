#Description: This program will calculate how much money the user needs to
#save monthly, weekly, and daily
#Author: Nicole Galvan
#Date: 08/05/24

print("💰 ~SAVINGS CALCULATOR~ 💰")
print("💵 How much money do you want to save this year? 💵")
amountYearly = int(input("Enter amount: "))

saveMonthly = round(amountYearly / 12 , 2)
saveWeekly = round(amountYearly / 52, 2)
saveDaily = round(amountYearly / 365, 2)

goal = '''For you to meet your goal of saving ${} this year, you need to
save ${} each month, ${} each week, and ${} daily'''

print(goal.format(amountYearly, saveMonthly, saveWeekly, saveDaily))
