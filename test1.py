#def hej(imie):
#    print('Hej ' + imie + '!')

#dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
#for imie in dziewczyny:
#    hej(imie)
#    print('Kolejna dziewczyna')


#number = 0
#for i in range(0,5):
#	print("%.2f"%i)
#	number = number +0.2


#number = 0
#for i in range(0,2):
#	print("%.1f" % number)
#	number = number +0.2


##print numbers from 0 to 9 included
#for i in range(0,10):
#	print(i)
##end


##line should continue with "\"
#a = 1
#b = 2
#c = 3
#
#sum = 	a + \
#		b + \
#		c
#print(sum)
##end

#a = int("22", 8) #converts 22 from decimal to octal numbering system
#print(a)

# x = 10
# while x != 0:
# 	print("The value of x is",x,"dafcioo")
# 	x-=1

# #iterate through list
# list = [1,2,3,4,5,6,7,8,9,10,11]
# iterate_list = iter(list)
# for i in iterate_list:
# 	print(i)
#end

# import random
# for i in range(10):
# 	print(random.random() * 10**10	)

# import math
# print(math.cos(math.pi))
# print(math.degrees(3)) #converts radians to degrees



# tuple1, tuple2 = (1253,125) , (123,123)
# print(tuple1)
# print(tuple2)
# print (min(tuple1))

# dict = {"name" : 'Dawid', "surename" : "Sie", "age" : 21}
# print(dict.keys())

# import time
# ticks = time.time()
# print(ticks)
# print(time.localtime())
# print(time.asctime(time.localtime()))
# clock = time.clock()
# print(clock)


# import calendar
# cal = calendar.month(2016,12)
# print(cal)

# def pokaz(a,b = ''):
#     print(len(a), end=" ")
#     print(b)
#
# pokaz('amarantowy')

# #Lambda
# sum = lambda a,b: a+b
#
# print('Sum of two integers:', sum(2,2))

# def fact(number):
#     result = 1
#     while number > 1:
#         result *= number
#         number -= 1
#     return result
#
# print(len(str(fact(52))))


#Namespaces and scoping
# age = 21
#
# def increase_age():
#     global age
#     age += 1
#     print(age)
#
# print(age)
# increase_age()
# print(age)


# import math
# content = dir(math)
# print (content)
#
# import time
# content = dir(time)
# print(content)

# #input
# keyboard_input = input("type your input: ")
# print(len(keyboard_input))

# #data input
# doc = open("doc.txt", "r")
# data = doc.readline()
# print(data, end="")
# data = doc.read(5)
# print(data)
#
# for line in doc:
#     print(line)
# doc.close()

# write_file = open("write.txt", "w")
# s = "Writing to the file"
# for i in range(100):
#     write_file.write("%d, %s \n" %(i, s))
# write_file.close()
#
# print (write_file.mode)

# import os
# print(dir(os))


import re

text = "Dawid Tomek Wacław Kolega"
text_split = re.split(r'\s*', "text here are some")

for word in text_split:
    print(word)
