import json

f = open("birthdays.json", "r")
birthdays = json.load(f)
f.close()

user_input = input("Enter name and surename: ")

if user_input in birthdays.keys():
    print(user_input + " was born on " + birthdays[user_input])
else:
    print("There is no " + user_input + " in database.")