# Name: David Theimer
# M02 Lab Case Study: if...else and while
# File Name: m02lab.py
# Program will accept student names and GPAs and test if the student \
# qualifies for either the Dean's List or the Honor Roll


while True:
    # Enter student last name
    last_name = input("Enter student's last name or (ZZZ to quit): ")

    # Check 'ZZZ has been entered for last name to quit
    if last_name == 'ZZZ':
        break
    
    # User enters student first name and GPA
    first_name = input("Enter student's first name: ")
    student_gpa = float(input("Enter student's GPA: "))

    if student_gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List")
    elif student_gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll")
    elif student_gpa < 3.5:
        print(first_name, last_name, "has not made the Honor Roll or Dean's List")    
