#!/usr/bin/env python3

subjects = ["physics", "calculus", "poetry", "history"]
grades  = [98, 97, 85, 88]
gradebook = [subjects, grades]

def show_gradebook(gradebook):
    import subprocess
    subprocess.call('clear',shell=True)
    subject = 0
    grade = subject + 1
    row = 0

    tab = "\t"
    space = " "
    col1="Subject"
    space1=20-len(col1)
    col1+=space*space1
    col2="Grade"

    print(f"{col1+space+tab+col2}")
    print("\n")

    for row in range(len(gradebook[subject])):
        printRow = gradebook[subject][row]
        if len(gradebook[subject][row]) < 20:

            addchar=20-len(gradebook[subject][row])
            printRow+=' '*addchar
            print(printRow, gradebook[subject+1][row],sep=":\t",end="\n")
        else:
            print(gradebook[subject][row], gradebook[grade][row], sep=":\t",end="\n")

def prompt_message():
    print("\n")
    print('Type "Append",\n If you would like to make changes to an existing grade.')
    print('Type "Add",\n If you would like to add a new subject and grade.')
    print('Type "Last Semester",\n If you would like to view gradebook for last semester.')

def new_subject(gradebook):
    addSubject=input("Subject: ")
    subjects.append(addSubject.lower())
    return subjects

def new_grade(gradebook):
    addGrade=input("Grade: ")
    grades.append(addGrade)
    return grades



def prompt_continue():
    cont = input("Would you like to add another grade? ")
    return cont.lower()

def error_input():
    print("Error: Invalid Input!\n")

def which_subject():
    return input("For which subject would you like to modify the grade?")

def grade_type():
        return input('How would you like to modify this grade?\nType "Pass",\n To change grade schema to Pass/Fail.\nType "Numerical",\n To modify grade numerically.')

def prompt_PassorFail(gradebook, count):
    while True:
        modPass = str(input("Pass or Fail: "))
        if str(modPass.lower()) == str("pass") or str(modPass.lower()) == str("fail"):
            print(subjects[count], 'grade will be changed to', modPass)
            break
        else:
            print(modPass, 'is not a valid input.')
            continue
    return modPass

def pass_grade (gradebook, count):
    modPass = prompt_PassorFail(gradebook, count)
    if modPass.lower() == "pass" or modPass.lower() == "fail":
        grades[count] = modPass
        print(subjects[count], 'grade has been changed to ', grades[count])
    return grades[count]

def numerical_grade (gradebook, count):
    operator = input('Type "Add",\n To add a number to the currect grade.\nType "Subtract", to subtract a number from the currect grade.\n')
    number = input("Modify the grade by how much? :")
    if operator.lower() == "add":
        grades[count]=int(grades[count])+int(number)
    elif operator.lower() == "subtract":
        grades[count]=int(grades[count])-int(number)
    return grades[count]

def modify_subject(gradebook):
    while True:
        modSubject = which_subject()
        for count in range(len(subjects)):
            if subjects[count] == modSubject:
                modHow = grade_type()
                if modHow.lower() == "pass":
                    grades[count]=pass_grade(gradebook, count)
                elif modHow.lower() == "numerical":
                    grades[count]=numerical_grade(gradebook, count)
        cont = prompt_continue()
        if cont.lower() == "no":
            break
        elif cont.lower() == "yes":
            continue
        else:
            error_input()
            break
    return gradebook

def add_grade(gradebook):
    while True:
        subjects = new_subject(gradebook)
        grades = new_grade(gradebook)
        cont = prompt_continue()
        if cont.lower() == "no":
            break
        elif cont.lower() == "yes":
            continue
        else:
            error_input()
            cont = prompt_continue()
    return gradebook

def show_full_gradebook(gradebook):
    import subprocess
    subprocess.call('clear',shell=True)

    last_semester_subjects = ["chemistry", "statistics", "english", "economics"]
    last_semester_grades = [98, 95, 88, 96]
    last_semester_gradebook = [last_semester_subjects, last_semester_grades]

    subject = 0
    grade = subject + 1
    row = 0

    tab = "\t"
    space = " "
    col1="Subject"
    space1=20-len(col1)
    col1+=space*space1
    col2="Grade"

    print(f"{col1+space+tab+col2}")
    print("\n")

    for row in range(len(last_semester_gradebook[subject])):
        printRow = last_semester_gradebook[subject][row]
        if len(last_semester_gradebook[subject][row]) < 20:

            addchar=20-len(last_semester_gradebook[subject][row])
            printRow+=' '*addchar
            print(printRow, last_semester_gradebook[subject+1][row],sep=":\t",end="\n")
        else:
            print(last_semester_gradebook[subject][row], last_semester_gradebook[grade][row], sep=":\t",end="\n")
while True:
    show_gradebook(gradebook)
    prompt_message()
    prompt = input("Gradebook: ")
    if prompt.lower() == "exit":
        break
    elif prompt.lower() == "add":
        gradebook = add_grade(gradebook)
        continue
    elif prompt.lower() == "append":
        gradebook = modify_subject(gradebook)
        continue
    elif prompt.lower() == "last semester":
        while True:
            show_full_gradebook(gradebook)
            goback = input('Go back to current gradebook? (yes or no)')
            if goback.lower() == "yes":
                break
            elif goback.lower() == "no":
                continue
            else:
                error_input()
                continue
        continue
    else:
        error_input()
        continue
