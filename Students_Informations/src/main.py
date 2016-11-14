'''
Created on Nov 14, 2016

@author: A Cell MUSCHITO
'''

from tests.tests import test_all
from UI.UI import UI_print_the_commands, UI_create_args_list, UI_add, UI_print_students, UI_update, UI_penalize, UI_print_from_hometown

def initialize(std_list):
    UI_add(std_list, ["test1234", "namea", "hta", "2"])
    UI_add(std_list, ["test1264", "nameb", "htb", "3"])
    UI_add(std_list, ["test1634", "namec", "htc", "4"])
    UI_add(std_list, ["tegt1234", "named", "htd", "6"])
    UI_add(std_list, ["tsst1234", "namee", "hte", "2"])
    UI_add(std_list, ["tett1234", "namef", "htf", "9"])
    UI_add(std_list, ["test1236", "nameg", "htg", "3"])
    UI_add(std_list, ["teat1214", "nameh", "hth", "7"])
    UI_add(std_list, ["tqst1314", "namei", "hth", "6"])
    UI_add(std_list, ["trst1314", "namej", "hth", "1.2"])
    
if __name__ == '__main__':
    std_list = []
    initialize(std_list)
    test_all
    cmd_list= {"1": UI_add, "2": UI_print_students, "3": UI_update, "4": UI_penalize, "5": UI_print_from_hometown}
    the_commands = ["Please type the number corresponding to the command you want to use:","1 to add a new student,","2 to print all students,", "3 to update a student,","4 to penalize a student,","5 to print all students from a certain hometown:"]
    props = {"1": ["Code = ", "Name = ", "Hometown = ", "Grade = "],
             "2": [],
             "3": ["Code = ", "Grade = "],
             "4": ["Group = "],
             "5": ["Hometown = "]}
    while True:
        try:
            UI_print_the_commands(the_commands)
            cmd = input("")
            args = []
            if cmd not in cmd_list:
                raise ValueError("Incorrect command!")
            args = UI_create_args_list(props, cmd)
            cmd_list[cmd](std_list, args)
        except ValueError as e:
            print (e)