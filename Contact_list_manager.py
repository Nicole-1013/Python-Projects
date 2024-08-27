#Description: This program will ask the user for the name of a person they wish to add to their contacts, the associated number, if they want to delete a number,
#if they want to view someones number, and many other functions you encounter when making a new contact
#Author: Nicole Galvan 
#Date: 8/27/24
import os


#Global Variable
contacts = {}
user_input = ""
def clear_console():
    if os.name == 'nt':
        os.system('cls')

def add_contact():
    contact_name = input("What is the name of your new contact?")
    contact_number = input("What is the number of your new contact?")

    contacts[f"{contact_name}"] = [contact_number]

def print_menu():
    print("-------MENU-------")
    print('''     
    add) add new contact   
    delete) delete contact
    view) view someone's contact info
    show) show contact list
    address) add address to contact
    note) add notes to a person's contact
    quit)''')

def delete_contact():
    contact_name = input("Name of the contact")
    del contacts[f'{contact_name}']

def view_contact():
    contact_name = input("Name of contact")
    print(contacts.get(f'{contact_name}'))

def show_contacts():
    for x,y in contacts.items():
        print(f'Name: {x} | Number: {y[0]}')
    
while user_input != 'quit':
    print_menu()
    user_input = input("Choose Option: ").lower()
    if user_input == "add":
        add_contact()
    elif user_input == "delete":
        delete_contact()
    elif user_input == "view":
        view_contact()
    elif user_input == "show":
        show_contacts()
    clear_console()
    
    

