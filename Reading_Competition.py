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
#this gathers all the information that we need to do the page count calculations
school_reading_goal = int(input("How many pages does the school aim to read?"))
pages_needed_from_each_student = round(school_reading_goal / students_in_school)
#This gathers the information to determine how many pages students need to read for
#the goal

final_answer = '''There are {} pages being read in every class, {} pages being read
schoolwide, and if the school wide reading goal is {} pages, then each
student needs to read {} pages'''

print(final_answer.format(pages_each_class_reads, pages_read_schoolwide, \
school_reading_goal, pages_needed_from_each_student))
