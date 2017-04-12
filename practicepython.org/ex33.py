birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        'Donald Trump': '06/14/1946',
        'Rowan Atkinson': '01/6/1955'}

user_input = input("Enter name and surename: ")
print(user_input)

if user_input in birthdays.keys():
    print(user_input + " was born on " + birthdays[user_input])
else:
    print("There is no " + user_input + " in database.")