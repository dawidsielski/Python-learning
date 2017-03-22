from itertools import *

a = [0,1,2,3,4,5,6,7,8,9]
b = ["zero", "one", "two", "three", "four", "five", "six"]
c = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]


for element in chain(a, b, c):
    print(element)

print(list(chain(a, b, c)))


# print(count(1, 10, 1))

print(list(islice(a, 2, 5 , 2)))
print(list(islice(count(), 2, 5 , 1)))


binary_filter = [1,0,0,0,0,0,0,1,1,0]
print(list(compress(a, binary_filter)))


def square(n):
    """Returns square od a number"""
    return n**2

print(list(map(square, a)))

print("Only odd numbers from a {}".format(list(filter(lambda x: x % 2, a))))

print(list(islice(cycle("ABC"), 10)))

#groupby

persons = [ {"name": "Dawid", "surename": "Sielski"},
            {"name": "Anna", "surename": "Sielski"},
            {"name": "Martyna", "surename": "Arbuz"},
            {"name": "Daria", "surename": "Rower"} ]

surename = lambda x: x['surename']

group_by_surename = groupby(sorted(persons, key = surename), surename)

for key, group in group_by_surename:
    print(key)
    for value in group:
        print(value)
    print()


#product

print(list(product("AB", "d")))
print(list(product("AB", "d", "AB", "d")))
print(list(product("AB", "d", repeat = 2)))

#repeat

print(list(map(pow, range(10), repeat(2)))) #because it is needed to constantly supply power to pow function


#takewhile
print(list(takewhile(lambda x : x < 5, [1,3,5,7,9,2])))