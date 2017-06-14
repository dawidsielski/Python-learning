s = "sdSDdfisdjfh"

part = s[:4]
upper = 0
for element in part:
    if element.isupper():
        upper += 1

if upper >= 2:
    print(s.upper())