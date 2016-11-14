'''
Created on Nov 14, 2016

@author: A Cell MUSCHITO
'''

from operator import itemgetter
'''
used in 'get_students_from_hometown'
'''

def create_student(code, name, hometown, grade):
    '''
    Create a new student dictionary with the given credentials
    
    Input:
    :param code:
    :param name:
    :param hometown:
    :param grade:
    Output:
    :return: stud
    '''
    stud = {"code": code, "name": name, "hometown": hometown, "grade": grade}
    return stud

def add_student(std_list, code, name, hometown, grade):
    '''
    Add a new student at the list  with the given credentials

    Input
    :param std_list:
    :param code:
    :param name:
    :param hometown:
    :param grade:
    Output:
    :return: std_list' = std_list+stud
    '''
    stud = create_student(code, name, hometown, grade)
    std_list.append(stud)
    
def update_student(std_list, code, grade):
    '''
    Update the grade of  a certain student having the given code

    Input
    :param std_list:
    :param code:
    :param grade:
    Output:
    :return: students list with student with code 'code' assigned grade 'grade' 
    '''
    for stud in std_list:
        if stud["code"] == code:
            stud["grade"] = grade
            
def penalize_group(std_list, group):
    '''
    Substract 10% from the grade of all students from a given group

    Input
    :param std_list:
    :param group[4:6]: The first 2 digits from the code of a student (group has 4 letters and 4 digits)
    Output:
    :return: students list with students in group 'group' penalized with 10%
    '''
    for stud in std_list:
        if stud["code"][4:6] == group:
            grade = float(stud["grade"]) - 10/100*float(stud["grade"])
            stud["grade"] = str(grade)
            
def get_students_from_hometown(std_list, hometown):
    '''
    Return a list of student dictionaries from a given hometown sorted descending after their grades

    Input
    :param std_list:
    :param hometown:
    Output:
    :return: ht_list = students from std_list who live in 'hometown' sorted by their grades descending
    '''
    ht_std = []
    for stud in std_list:
        if stud["hometown"] == hometown:
            ht_std.append(stud)
    return sorted(ht_std, key=itemgetter("grade"), reverse=True)