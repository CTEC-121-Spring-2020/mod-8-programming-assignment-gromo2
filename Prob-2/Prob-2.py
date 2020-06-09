# Module 8
#   Programming Assignment 11
#     Prob-2.py

class Student:
    def __init__(self, name, ID, major, GPA):
        self._name = name
        self._ID = ID
        self._major = major
        self._GPA = GPA
        # I added them all here, since I felt it would be best. I'm unsure what I'm doing, to be honest.
    
    def set_name(self, name):
        self._name = name 

    def get_name(self):
        return self._name
    
    def set_ID(self, ID):
        self._ID = ID

    def get_ID(self):
        return self._ID   

    def set_major(self, major):
        self._major = major

    def get_major(self):
        return self._major

    def set_GPA(self, GPA):
        self._GPA = GPA

    def get_GPA(self):
        return self._GPA 

def studentTest():
    JB = Student("Joe Bella", "9933", "Web Development", "3.8")
    TB = Student("Tucker Blank", "3399", "Nursing", "3.0")
    GU = Student("Gayle Ujifusa", "1011", "Baking", "2.8")
    EA = Student("Edna Anker", "9875", "Medical Office", "3.0")
    students = [JB, TB, GU, EA]

    print("Name            ID Number       Major           GPA")
    for student in students:
        print('{:<15}'.format(student._name), '{:<15}'.format(student._ID), '{:<15}'.format(student._major), student._GPA)
studentTest()
