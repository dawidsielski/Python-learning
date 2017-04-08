l = [5, 3, 4, 3, 5, 5, 3, 7]


for element in set(l):
    if l.count(element) == 1:
        print(element)