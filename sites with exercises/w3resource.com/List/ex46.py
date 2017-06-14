def return_odd(l):
    return [x for x in l if x % 2 == 1]

numbers = [x for x in range(30)]
print(return_odd(numbers))