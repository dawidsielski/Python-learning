import math
number = 999

def distance(number):
    if math.fabs(1000 - number) < 100 or math.fabs(2000 - number) < 100:
        return True
    return False

print(distance(999))
print(distance(1901))
