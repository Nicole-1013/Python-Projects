#Description: This program will ask the user for the name of a person they wish to add to their contacts, the associated number, if they want to delete a number,
#if they want to view someones number, and many other functions you encounter when making a new contact
#Author: Nicole Galvan 
#Date: 8/27/24
import os

#Global Variables
contacts = {}
user_input = ""

def clear_console():
    if os.name == 'nt':
        os.system('cls')


#function that adds key and value to contacts dictionary (only adds number value first)
def add_contact():
    contact_name = input("What is the name of your new contact? ")
    contact_number = input("What is the number of your new contact? ")
    address = input("Address (or leave blank): ") or "none"
    contacts[contact_name] = [contact_number, address]
    print(f"Added contact: {contact_name}")


#prints the menu
def print_menu():
    print(''' 
    ----------MENU----------
    | add) Add new contact
    | delete) Delete contact
    | view) View contact info
    | show) Show contact list
    | modify) Modify contact
    | quit) Exit''')


#Deletes user indicated key and values from contacts dictionary
def delete_contact():
    contact_name = check_for_contact()
    del contacts[contact_name]
    print(f"Deleted contact: {contact_name}")


#Allows the user to view the information of specific contact
def view_contact():
    contact_name = check_for_contact()
    print(f"Number: {contacts[contact_name][0]} | Address: {contacts[contact_name][1]}")


#Shows all the contacts and all the values associated with the name (number, address) (address will be none until user adds it)
def show_contacts():
    for name,details in contacts.items():
        print(f'Name: {name} | Number: {details[0]} | Address: {details[1]}')

#modifys the users choice of number, name, or address of a contact
def modify_contact():
    name = check_for_contact()
    clear_console()
    
    while True:
        choice = input("What would you like to modify? (n: name, num: number, a: address) ").lower()
        if choice == "n":
            new_name = input("New name you wish to change this contact to: ")
            contacts[f"{new_name}"] = contacts[f"{name}"]
            del contacts[f"{name}"]
            break
        elif choice == "num":
            new_number = input("New number you wish to change this contact to: ")
            contacts[f"{name}"][0] = new_number
            break
        elif choice == "a":
            address = input("New Address you wish to change this contact to: ")
            contacts[f"{name}"][1] = address
            break
        else:
            print("INVALID OPTION: Try again")
            continue
    print("YOU HAVE MODIFIED THIS CONTACT")

def check_for_contact():
    while True:
        name = input("Contact name: ")
        if name in contacts:
            return name
        clear_console()
        print("ERROR: Contact does not exist. Try again.")


#main code working the menu and which functions to use
while user_input != 'quit':
    print_menu()
    user_input = input("Choose Option: ").lower()
    clear_console()
    if user_input == "add":
        add_contact()
    elif user_input == "delete":
        delete_contact()
    elif user_input == "view":
        view_contact()
    elif user_input == "show":
        show_contacts()
    elif user_input == "modify":
        modify_contact()
    elif user_input == "q":
        print("EXITED")
    else:
        print("INVALID OPTION: Try Again")
        continue
    
    
    

