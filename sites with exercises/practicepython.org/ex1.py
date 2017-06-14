import datetime

name = input("Enter your name:")
print("Your name is \'" + name + "\'")

age = int(input("Enter your age:"))
now = datetime.datetime.now()
print("Your age is: " + str(age) + ". In the year of: " + str(now.year + (100 - age)) + "." )
