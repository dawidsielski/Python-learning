l = [1,5,3,6,8,87,33,44,55,66,77,22,34,56,43,26,85,235,79,4,2,5,8,343,5674,2278,54]

treshold = int(input("Enter treshold: "))
for element in l:
    if element > treshold:
        print(element)