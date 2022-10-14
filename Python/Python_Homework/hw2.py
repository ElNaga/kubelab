from ast import If


print('Task 1')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4],'\n')

print("--------------------\n")

print('Task 2')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3],'\n')


print("--------------------\n")

print('Task 3')
def calcSquare(input):
    print('Area of the square with {} length of side, is: {}\n'.format(input,input*input))
calcSquare(7)


print("--------------------\n")

print('Task 4')
def isItHot(temp):
    if temp>25:
        print('Its hot at {} degrees.'.format(temp))
    elif temp>15:
        print("It's warm at {} degrees.".format(temp))
    elif temp<15:
        print("It's cold at {} degrees.".format(temp))

isItHot(13)
isItHot(19)
isItHot(33)


print("--------------------\n")

print('Task 5')

def greaterThenZero(list):
    list2 = [item for item in list if item > 0]
    print("Numbers greater than 0 are: ",list2)

greaterThenZero([-5,3,-1,101])

print("--------------------\n")

print('Task 6')

def alphaUpper(stringsArray):
    result = [x.upper() for x in stringsArray]
    result.sort()

    print(result)

alphaUpper(["snow", "glacier", "iceberg"])



