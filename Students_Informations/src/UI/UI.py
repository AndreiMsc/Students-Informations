'''
Created on Nov 14, 2016

@author: A Cell MUSCHITO
'''

from domain.operations import add_student, update_student, penalize_group, get_students_from_hometown

def UI_print_the_commands(the_commands):
    for cmd in the_commands:
        print(cmd)
        
def UI_create_args_list(props, cmd):
    args = []
    for arg in props[cmd]:
        print(arg)
        arg = input("")
        args.append(arg)
    return args

def UI_get_codes(std_list):
    codes = []
    for stud in std_list:
        codes.append(stud["code"])
    return codes

def UI_add(std_list, args):
    if len(args) != 4:
        raise ValueError("Incorrect number of arguments!")
    code = args[0]
    name = args[1]
    hometown = args[2]
    grade = args[3]
    codes = UI_get_codes(std_list)
    if not name.isalpha() or len(name) < 3:
        raise ValueError("Invalid name!")
    if not hometown.isalpha() or len(hometown) < 3:
        raise ValueError("Invalid hometown!")
    try:
        float(grade)
    except ValueError:
        raise ValueError("Invalid grade!")
    if float(grade) < 0 or float(grade) > 10:
        raise ValueError("Invalid grade!")
    if len(code) != 8:
        raise ValueError("Invalid code!")
    elif not code[:4].isalpha():
        raise ValueError("Invalid code!")
    elif not code[4:].isdigit():
        raise ValueError("Invalid code!")
    elif code in codes:
        raise ValueError("Already a student with that code!")
    add_student(std_list, code, name, hometown, grade)
    
def UI_print_students(std_list, args):
    for stud in std_list:
        print("Code: " + stud["code"] + " Name: " + stud["name"] + " Hometown: " + stud["hometown"] + " Grade: " + stud["grade"] + "\n")
        
def UI_update(std_list, args):
    code = args[0]
    grade = args[1]
    codes = UI_get_codes(std_list)
    try:
        float(grade)
    except ValueError:
        raise ValueError("invalid grade")
    if float(grade) < 0 or float(grade) > 10:
        raise ValueError("invalid grade")
    if len(code) != 8:
        raise ValueError("invalid code")
    elif not code[:4].isalpha():
        raise ValueError("invalid code")
    elif not code[4:].isdigit():
        raise ValueError("invalid code")
    if not code in codes:
        raise ValueError("inexistent student")
    update_student(std_list, code, grade)
    
def UI_penalize(std_list, args):
    group = args[0]
    if len(group) != 2 or not group.isdigit():
        raise ValueError("invalid group")
    penalize_group(std_list, group)
    
def UI_print_from_hometown(std_list, args):
    hometown = args[0]
    if not hometown.isalpha() or len(hometown) < 3:
        raise ValueError("invalid hometown")
    studs = get_students_from_hometown(std_list, hometown)
    for stud in studs:
        print("Code: " + stud["code"] + "Name: " + stud["name"] + "Hometown: " + stud["hometown"] + "Grade: " + stud["grade"] + "\n")
