import os
import calendar
import shelve
import sys

script_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_path)
# print(script_path)

year = int(input("Enter year: "))

if os.path.isdir(str(year)):
    os.chdir(str(year))
else:
    sys.exit("Invalid year.")

month = int(input("Enter month (1 to 12 inclusive): "))
month_name = str(calendar.month_name[month])

if not os.path.isfile(month_name + ".dat"):
    sys.exit("There is no such file in this directory.")

# day = int(input("Enter day: "))

database = shelve.open(month_name)

print("\nDatabase contents:")
for element in database:
    print(element)
    print(database[element])

database.close()
os.chdir(script_path)