class Student:
    def msg(self):
        print("this is class program")
    def __init__(self):
        print("I will run without object")


s=Student() # creating object of student class
Student.msg(s)
s.msg()
s2=Student()
