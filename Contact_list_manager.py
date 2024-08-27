#Description: This program will ask the user for the name of a person they wish to add to their contacts, the associated number, if they want to delete a number,
#if they want to view someones number, and many other functions you encounter when making a new contact
#Author: Nicole Galvan 
#Date: 8/27/24

#Global Variable
contacts = {}
user_input = ""
def add_contact():
    contact_name = input("What is the name of your new contact?")
    contact_number = input("What is the number of your new contact?")

    contacts[f"{contact_name}"] = [contact_number]

def print_menu():
    print("       MENU       ")
    print('''  add) add new contact   
    delete) delete contact
    view) view someone's number
    number) check if number in your list
    address) add address to contact
    note) add notes to a person's contact
    quit)''')

def delete_contact():
    contact_name = input("Name of the contact")
    del contacts[f'{contact_name}']

while user_input != 'quit':
    print_menu()
    user_input = input("Choose Option: ").lower()
    if user_input == "add":
        add_contact()
    if user_input == "delete":
        delete_contact()
    
    print(contacts)

