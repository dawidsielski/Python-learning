user_input = input()

digits, letters = 0, 0
for element in user_input:
    if element.isdigit() == True:
        digits += 1
    elif (element.isalpha() == True and not element.isspace() == True):
        letters += 1

print("LETTERS ", letters, "\nDIGITS ", digits)