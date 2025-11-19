# Author: Prisca Muleka
# File: gpa_checker.py
# This program asks for student names and GPAs and tells whether the
# student made the Dean's List or Honor Roll. The program ends when
# the last name entered is 'ZZZ'.

last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")

while last_name != "ZZZ":
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name, "made the Honor Roll.")
    else:
        print(first_name, last_name, "did not qualify for honors.")

    print()  # adds space
    last_name = input("Enter the student's last name (enter 'ZZZ' to quit): ")

print("Program ended.") 