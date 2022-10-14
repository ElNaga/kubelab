import sys


# DICTIORARIES
# a = {'ime': 'Alek'};
# print(a)
# a['ime'] = 'aleksandar'
# print(a)
# b={'daniel':'test3'}
# a.update(b)
# print(a)

# touples are faster then lists

def test():
    ''' tekst koj sstho definirate help za zadadena funckija ''' #vaka se pishuva definicija za funckija

print("Zdravo, kako ste?\nOva e nova linija!") #nova linija vo string

# Bytes Squences
    # naucshi si sam...
# string = 'String1234'
# strByt = bytes(string,'utf-8')
# print(strByt)

# for byte in strByt:
#     print(byte)


#Range
    # nauci si sam isto taka...

# CONDITIONALS
    # if, elif, else
# hi = 'Hi'
# b = 'pozdrav'

# if hi == 'Hi':
#     print('Hello')

# age = 15
# print('kid' if age < 18 else 'adult')


#---------------------------------------------------
#FOR cycle

# for i in range(10):
#         print(i)
#         for j in 'a','b','c','d':
#             print(j)

# dictTest = {"Ivan": 'test1', "Antonio": 'test2'}
# lista = [1,2,3,4]
# for k,v in dictTest.items():
#     print(k,v)
# for li in lista:
#     print(li)
# for li in dictTest.values():
#     print(li)

#------------------------
#WHILE
i=1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# FUNCII ------------------

# def ime_funk(a,b):
#     return a+b

# print('Rezultatot e:' ,ime_funk(2,3))
# print(help(print))


# LAMBDA ARGUMENT : EXPRESSION

# x = lambda a : a + 2 
# print('\n')
# print(x(3))


# *args i **kwargs

def func1(*args):
    print(args)

func1(100,2,3) #prints touples because of the way we initialize the func

def func2 (**kwargs):
    print(kwargs) # prints dictionaries

func2(ime1='ivan')