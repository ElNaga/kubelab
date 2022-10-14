# vezhba 4

# r = float(input('Radius na krug: \n'))
# print("Area of circle is: " + str(r*r*3.14))

# name = input('First name:\n')
# last_name = input('Last name:\n')
# print(last_name + ' ' + name)

# numbers = input('Please input numbers in order: x,y,z...\n')
# number_list = numbers.rsplit(',')
# tuple_nums = tuple(number_list)
# print(number_list)
# print(tuple_nums)

# filename_input = input('Filename:\t')
# print(filename_input.rsplit('.')[-1])

# color_list = ["Red","Green","White" ,"Black"]
# print("First color: %s"%(color_list[0]) +  '\tSecond color: %s'%(color_list[-1]))

a = int(input("Input an integer: \t"))
n1 = int("%s" %a)
n2 = int( "%s%s" %(a,a))
n3 = int( "%s%s%s" %(a,a,a))
print(n1+n2+n3)