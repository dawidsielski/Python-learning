text = input()

if (len(text) >= 2):
    print(text[:2] + text[len(text) - 2:])
else:
    print("")