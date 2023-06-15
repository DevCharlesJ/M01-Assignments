""" GPA AWARD

    Author: Charles Jones
    Description: Given a student's name and gpa, this program will output wether
                 the student is to be awarded Dean's List or Honor Roll

                 Multiple students can be iteratedly processed
"""

while (lname := input("Enter student's last name, or 'ZZZ' to quit: ")) != 'ZZZ':

    fname = input("Enter student's first name: ")
    gpa = float(input("Enter student's gpa (Ex: 3.5): "))
    award = ""

    if gpa >= 3.5:
        award = "Dean's List"
    elif gpa >= 3.25:
        award = "Honor Roll"

    if award:
        print(f"{fname} {lname} has made the {award}")