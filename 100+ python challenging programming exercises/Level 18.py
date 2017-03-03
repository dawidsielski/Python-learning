def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    isupper, isdigit, islower, ischaracter = False, False, False, False
    for letter in password:
        if letter.isupper():
            isupper = True
        elif letter.islower():
            islower = True
        elif letter.isdigit():
            isdigit = True
        elif letter in "$#@":
            ischaracter = True
    return isupper and isdigit and islower and ischaracter

passwords = "ABd1234@1,a F1#,2w3E*,2We3345".split(",")
for element in passwords:
    if check_password(element):
        print(element, end = ", ")