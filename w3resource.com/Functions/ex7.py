def string_letters(s):
    small = 0
    big = 0
    for letter in s:
        if letter.isupper():
            big += 1
        elif letter.islower():
            small += 1
    return (small, big)


print(string_letters("DawiD"))
    