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

    contacts[f"{contact_name}"] = [contact_number, "none"] #The "none" is the space indicated for the address which is optional to put in


#prints the menu
def print_menu():
    print(" ----------MENU----------")
    print('''     
    |add) add new contact   
    |delete) delete contact
    |view) view someone's contact info
    |show) show contact list
    |address) add/change address to contact
    |modify) modify contact
    |q) quit''')


#Deletes user indicated key and values from contacts dictionary
def delete_contact():
    contact_name = check_for_contact()
    del contacts[f'{contact_name}']
    print("YOU HAVE DELETED THIS CONTACT")


#Allows the user to view the information of one contact of their choosing
def view_contact():
    contact_name = check_for_contact()
    print("Number: " + contacts.get(f'{contact_name}')[0] + "| Address: " + contacts.get(f'{contact_name}')[1])


#Shows all the contacts and all the values associated with the name (number, address) (address will be none until user adds it)
def show_contacts():
    for x,y in contacts.items():
        print(f'Name: {x} | Number: {y[0]} | Address: {y[1]}')


#adds address to the value list of a certain key (user indicated)
def modify_address():
    contact_name = check_for_contact()
    address = input("Address: ")
    contacts[f"{contact_name}"][1] = address


def modify_contact():
    name = check_for_contact()
    choice = input("What would you like to modify? (n: name, num: number, a: address ")
    clear_console()
    while choice:
        if choice == "n":
            new_name = ("New name you wish to change this contact to: ")
            contacts[f"{new_name}"] = contacts[f"{name}"]
            del contacts[f"{name}"]
            break
        elif choice == "num":
            new_number = input("New number you wish to change this contact to: ")
            contacts[f"{name}"][0] = new_number
            break
        elif choice == "a":
            new_address = input("New Address you wish to change this contact to: ")
            contacts[f"{name}"][1] = new_address
            break
        else:
            print("INVALID OPTION: Try again")
            continue


def check_for_contact():
    contact_name = input("Name of contact: ")
    if contact_name in contacts:
        return contact_name
    while contact_name not in contacts:
        clear_console()
        print("ERROR: contact does not exist. Try Again.")
        contact_name = input("Name of Contact: ")
        continue
    return contact_name


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
    elif user_input == "address":  
        modify_address()
    elif user_input == "modify":
        modify_contact()
    else:
        print("INVALID OPTION: Try Again")
        continue
    
    
    

