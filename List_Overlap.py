#Description: This program will find which numbers both lists have in common without duplicates, then print those numbers
#Author: Nicole Galvan 
#Date: 8/15/24

list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []

for x in list_one:
    if x in list_two:
        if x not in new_list:
            new_list.append(x)
print(new_list)