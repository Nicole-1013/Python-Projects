#Description: This program will ask the user for the name of a person they wish to add to their contacts, the associated number, if they want to delete a number,
#if they want to view someones number, and many other functions you encounter when using a contact list app
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
    contact_name = input("What is the name of your new contact? ")#acts as the key for the dictionary
    contact_number = input("What is the number of your new contact? ") #asks for first value for the key (phone number)
    address = input("Address (or leave blank): ") or "none" #if input is left blank, address will be none(second value of contact name key)
    contacts[contact_name] = [contact_number, address] #assigns list of values associated with contact name
    print(f"Added contact: {contact_name}") #lets the user know contact has been added (front end)


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
    contact_name = check_for_contact()#checks if contact is in contacts(done for almost all functinos)
    del contacts[contact_name]#deletes key and values of contact name
    print(f"Deleted contact: {contact_name}")#front end, lets user know


#Allows the user to view the information of specific contact
def view_contact():
    contact_name = check_for_contact()
    print(f"|Number: {contacts[contact_name][0]} | Address: {contacts[contact_name][1]}|")


#Shows all the contacts and all the values associated with the name (number, address) (address will be none until user adds it)
def show_contacts():
    for name, details in sorted(contacts.items()):#sorts printed values onto alphatbetical order
        print(f'Name: {name} | Number: {details[0]} | Address: {details[1]}')

#modifies the users choice of number, name, or address of a contact
def modify_contact():
    name = check_for_contact()
    clear_console()#clears text beforehand to ensure easily read code
    
    while True:#ends only when a valid option(choice) is chosen
        choice = input("What would you like to modify? (n: name, num: number, a: address) ").lower()
        if choice == "n":
            new_name = input("New name you wish to change this contact to: ")
            contacts[f"{new_name}"] = contacts.pop(name)#makes new key with the same values as the old key, deletes old key and values
            break
        elif choice == "num":
            contacts[f"{name}"][0] = input("New number you wish to change this contact to: ")#changes number value of key
            break
        elif choice == "a":
            contacts[f"{name}"][1] = input("New Address you wish to change this contact to: ")#changes address value of key
            break
        else:
            print("INVALID OPTION: Try again")#if no valid option chosen, while loop repeats
            clear_console()
            continue
    print("YOU HAVE MODIFIED THIS CONTACT")#front end, lets user know that the function was successful

def check_for_contact():
    while True:
        name = input("Contact name: ")#asks user for name
        if name in contacts:
            return name#breaks loop if name already un contacts
        clear_console()
        print("ERROR: Contact does not exist. Try again.")#loops until they find a name in contacts


#main loop working the menu
while user_input != 'quit':#ends run
    print_menu()#after each function, menu appears again
    user_input = input("Choose Option: ").lower()
    clear_console()#to not overload
    {'add': add_contact, 'delete': delete_contact, 'view': view_contact,
     'show': show_contacts, 'modify': modify_contact}.get(user_input, 
     lambda: print("INVALID OPTION, Try Again"))()#keys equal to user input will execute associated functions
clear_console()
print("Goodbye, Thank you!")#end of program :)
    
    

