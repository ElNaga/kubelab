#     Create a directory HomeWork03. In that directory create all the files from the tasks.

# Task 1: 
# Make a class Person in person.py with some parameters to accept/variables to be used. To have:
# First Name -> String
# Last Name -> String
# E-mail Address -> e-mail
# Mobile Number -> integer

# Task 2:
# Make a class Student in student.py where he will inherited the Person class and in the Student class you will have courses from DevOps.
# For example
# List of available courses:
# Git -> String
# Linux -> String
# Python -> String
# Docker -> String
# AWS -> String

# So, each of these people will contain grade for each of the courses he has. 
# For example 

# Person:
# First Name: Ivan
# Last Name: Adji - Krstev
# E-mail: iadjikrstev@gmail.com
# Mobile: +389 77 72 92 92 
	
# Is a Student of the following and has grades from (0-10) - this could be a dictionary. 
# Git - 7
# Python - 8
# AWS - 10
# Linux - 4


# Task 3:
# Investigate about "super()" method and "__init__" and how they are working, why and some example usage to be shown. 
# Use your own words 


import re
import phonenumbers

class Courses:
    def __init__(self,a,b,c,d):
        self.GitFundamentals = a
        self.AmazonWS = b
        self.Azure = c
        self.Kubernetes = d


class Person:
    def __init__(self, name, lastname, email, num,a,b,c,d):
        self.first_name = name
        self.last_name = lastname
        self.email = email
        self.mobile_number = num
        self.courses = Courses (a,b,c,d)

    def printObject(self):
        print("Name is: ",   self.first_name)
        print("Lastname is: ",   self.last_name)
        print("Email is: ",   self.email)
        print("Name is: ",   self.mobile_number)
        print("Courses grades are: ",   self.courses.GitFundamentals, ' ', self.courses.AmazonWS, ' ', self.courses.Azure, ' ',self.courses.Kubernetes)



# def checkEmail(string):
#     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#     if(re.fullmatch(regex, string)):
#         return string
#     else:
#         return False

def checkIfEmailIsKubelab(string):
    regex = r'\b[A-Za-z0-9._%+-]+@kubelab+\.cloud\b'
    if(re.fullmatch(regex, string)):
        return string
    else:
        return False

# def checkPhoneNumber(number):
    # if (len(number) == 9):

def isString(string):
    if (isinstance(string,str)):
        return string
    else:
        return 'Not valid info'

def isPhoneNumber(number):
    if (phonenumbers.is_valid_number(phonenumbers.parse(isString(number)))):
        return number
    else:
        return 'not a valid number!'

name = isString(input('Please enter a name:'))
last_name = input('Please enter a lastname:')
email = checkIfEmailIsKubelab(input('Please enter a email:')) # Има 2 функции за проверка на мејл, втората е специфична за kubelab
number = isPhoneNumber((input('Please enter your phone number: ')))
c1Grade = isString(input('Please input grade for course 1: '))
c2Grade = isString(input('Please input grade for course 2: '))
c3Grade = isString(input('Please input grade for course 3: '))
c4Grade = isString(input('Please input grade for course 4: '))
ucenik1 = Person(name,last_name,email,number,c1Grade,c2Grade,c3Grade,c4Grade)

ucenik1.printObject()

# Коментар: Подобрување може да се направи со тоа што секој инпут ќе биде во една while функција и доколку 
# не се задоволи условот за внесот, повторно да се внесува за истата променлива


# __init__

# The initialization constructor function is used to create the class/object and to pass the refference to the object
# that was created __init_(self, ... )

# super()

# We use "super()" if we want to access methods in parent classes. 
# For an example, I could've made a method isString in the Person class, and than from Courses 