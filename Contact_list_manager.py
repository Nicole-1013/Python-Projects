#Description: This program will ask the user for the name of a person they wish to add to their contacts, and the associated phone number
#Author: Nicole Galvan 
#Date: 8/27/24

contacts = {}
contact_name = ""
contact_number = 0

contact_name = input("What is the name of your new contact?")
contact_number = input("What is the number of your new contact?")

contacts[f"{contact_name}"] = contact_number

print(contacts)