l = [x for x in range(10)]

def square_numbers(num):
    for element in num:
        yield element**2


print(square_numbers(l))
generator = square_numbers(l)

try:
    for i in range(11):
        print(next(generator))
except StopIteration:
    print("No more elements")