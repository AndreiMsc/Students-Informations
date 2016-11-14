'''
Created on Nov 14, 2016

@author: A Cell MUSCHITO
'''

from domain.operations import create_student, add_student, update_student, \
    penalize_group, get_students_from_hometown


def test_create():
    stud = create_student("abcd1234", "test", "home", "5")
    assert (stud["code"] == "abcd1234")
    assert (stud["name"] == "test")
    assert (stud["hometown"] == "home")
    assert (stud["grade"] == "5")
    
def test_add():
    std_list = []
    add_student(std_list, "abcd1234", "test", "home", "5")
    assert (std_list == [{"code": "abcd1234", "name": "test", "hometown": "home", "grade": "5"}])
    
def test_update():
    std_list = []
    add_student(std_list, "abcd1234", "test", "home", "5")
    update_student(std_list, "abcd1234", "9")
    assert (std_list == [{"code": "abcd1234", "name": "test", "hometown": "home", "grade": "9"}])
    
def test_penalize():
    std_list = []
    add_student(std_list, "abca1234", "test", "home", "10")
    add_student(std_list, "abcb2134", "test", "home", "10")
    add_student(std_list, "abcd1234", "test", "home", "9")
    penalize_group(std_list, "12")
    assert (std_list == [{"code": "abca1234", "name": "test", "hometown": "home", "grade": "9.0"},
                         {"code": "abcb2134", "name": "test", "hometown": "home", "grade": "10"},
                         {"code": "abcd1234", "name": "test", "hometown": "home", "grade": "8.1"}])
    
def test_get_from_hometown():
    std_list = []
    add_student(std_list, "abcd1231", "test", "home", "6")
    add_student(std_list, "abcd1232", "test", "house", "9")
    add_student(std_list, "abcd1233", "test", "home", "5")
    ht_std = get_students_from_hometown(std_list, "home")
    assert (ht_std == [{"code": "abcd1231", "name": "test", "hometown": "home", "grade": "9"},
                       {"code": "abcd1233", "name": "test", "hometown": "home", "grade": "5"}])

def test_all():
    test_create()
    test_add()
    test_update()
    test_penalize()
    test_get_from_hometown()
