# 1 Task:

print('Twinkle , twinkle little star')
print('\tHow I wonder what you are!')
print('\t\tUp above the world so high,')
print('\t\tLika a diamond in the sky.')
print('Twinkle, twinkle, little star,')
print('\tHow I wonder what you are!')
print('\n')
print('--------------------------')
print('\n')

# 2 Task:

import datetime
from ntpath import join

print('Current date and time: ' + str(datetime.datetime.now()))

print('\n')
print('--------------------------')
print('\n')

# 3 task

st = 'Print only the words that start with s in this sentence'
words_st = st.split(' ')
for word in words_st:
    if word[0]=='s':
        print(word)

print('\n')
print('--------------------------')
print('\n')

# task 4

for num in range(0,100):
    if num%2 == 0:
        print(num)

print('\n')
print('--------------------------')
print('\n')

# Task 5

def lesserEven_bigOdd(x,y):
    if x%2 == 0 and y%2 == 0:
        if x < y:
            print('Smaller number is '+ str(x))
        else:
            print('Smaller number is '+ str(y))
    else:
        if x < y:
            print('Larger number is '+ str(y))
        else:
            print('Larger number is '+ str(x))

lesserEven_bigOdd(6,4)
lesserEven_bigOdd(6,9)
lesserEven_bigOdd(7,9)


print('\n')
print('--------------------------')
print('\n')

#task 6


def checkWords(aString):
    x = aString.split(' ')
    if x[0][0] == x[1][0]:
        print('True')
        return True
    else:
        print('False')
        return False

checkWords('Crazy Kangaroo')
checkWords('Levelheaded Llama')

print('\n')
print('--------------------------')
print('\n')

# Task 7

def makes_twneenty(a,b):
    if (a+b) == 20 or a == 20 or b == 20:
        print('True')
        return True
    else:
        print('False')
        return False

makes_twneenty(12,8)
makes_twneenty(2,3)
makes_twneenty(20,10)

print('\n')        
print('--------------------------')
print('\n')

# Task 8

def mcd(someStr):
    print(someStr[:3].capitalize() + someStr[3:].capitalize())

mcd('macdonald')

# Task 9

print('\n')
print('--------------------------')
print('\n')


def Yoda(a):
    a_list = a.rsplit()
    aRev = list(reversed(a_list))
    aRev = ' '.join(aRev)
    print (aRev)

toYoda = 'Are you ready'
Yoda(toYoda)       