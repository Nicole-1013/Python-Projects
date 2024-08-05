#Description: This program is meant to determine the amount
#of pages each student reads and how much it takes for a school
#to get to their goal
#Author: Nicole Galvan
#Date: 08/5/24

pages_each_student_reads = int(input("How many pages does one student read?"))
students_in_each_class = int(input("How many students are there in each classroom?"))
pages_each_class_reads = pages_each_student_reads * students_in_each_class
classrooms_in_the_school = int(input("How many classrooms are in the school?"))
pages_read_schoolwide = pages_each_class_reads * classrooms_in_the_school
students_in_school = students_in_each_class * classrooms_in_the_school

school_reading_goal = int(input("How many pages does the school aim to read?"))
pages_needed_from_each_student = round(school_reading_goal / students_in_school)

print(pages_each_class_reads)
print(pages_read_schoolwide)

print(pages_needed_from_each_student)
