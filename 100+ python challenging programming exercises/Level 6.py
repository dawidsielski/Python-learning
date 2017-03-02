import math

c, h = 50, 30

def values(l):
    value = []
    for d in l:
        value.append(math.sqrt((2 * c * float(d))/h))
    return value


data = "100, 150, 180".split(",")
data = [int(x) for x in data]
data = values(data)
str1 = ","
str1 = str1.join(str(x) for x in data)
print(str1)