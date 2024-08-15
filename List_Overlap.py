#Description: This program will find which numbers both lists have in common without duplicates, then print those numbers
#Author: Nicole Galvan 
#Date: 8/15/24

list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [x for x in list_one if x in list_two]
newer_list = []
for x in new_list:
    if x not in newer_list:
        newer_list.append(x)



#for x in list_one: #iterates through first list
    #if x in list_two: #checks if it is in the second list also
        #if x not in new_list: #checks if there is already a duplicate of the shared number
            #new_list.append(x)# if not, the shared number is added to a new list



print(newer_list)