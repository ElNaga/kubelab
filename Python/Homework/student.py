import re
import phonenumbers
from person import Person

class Student(Person):

    def __init__(self, name, lastname, email, num,a,b,c,d,e):
        # self.name = name
        # self.last_name = lastname
        # self.email = email
        # self.mobile_number = num
        super().__init__(name,lastname,email,num)
        self.Courses = {
            'GitFundamentals' : a,
            'Linux' : b,
            'Python' : c,
            'Docker' : d,
            'AWS' : e,
            }
        
    def printAll(self):
        print(self.first_name,self.last_name,self.email,self.mobile_number, self.Courses)

def checkEmail(string):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, string)):
        return string
    else:
        return False

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

def checkOneTen(number):
    if int(number) in range(1,10,1):
        return number
    else: return 'Not a valid number'

# ucenik1 = Student('Aleksandar','Ilijevski','asd','asd',6,6,6,6,6)

name = isString(input('Please enter a name:'))
last_name = input('Please enter a lastname:')
email = checkEmail(input('Please enter a email:')) # Има 2 функции за проверка на мејл, втората е специфична за kubelab
number = isPhoneNumber((input('Please enter your phone number: ')))
c1Grade = checkOneTen(isString(input('Please input grade for course 1: ')))
c2Grade = checkOneTen(isString(input('Please input grade for course 2: ')))
c3Grade = checkOneTen(isString(input('Please input grade for course 3: ')))
c4Grade = checkOneTen(isString(input('Please input grade for course 4: ')))
c5Grade = checkOneTen(isString(input('Please input grade for course 5: ')))
ucenik1 = Student(name,last_name,email,number,c1Grade,c2Grade,c3Grade,c4Grade,c5Grade)

ucenik1.printAll()


# Task 3:


# __init__

# The initialization constructor function is used to create the class/object and to pass the refference to the object
# that was created __init_(self, ... )

# super()

# We use "super()" if we want to access methods in parent classes. 
# For an example, that's how we access the vars from Person class in Student class, without redeclaring them.