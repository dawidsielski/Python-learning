def gen_fib():
    fibonacci = [1,1]
    while True:
        fib_element =  fibonacci[-1] + fibonacci[-2]
        if fib_element > 10:
            raise StopIteration
        fibonacci.append(fib_element)
        yield fib_element


x = gen_fib()
print(x)

for fib_element in x:
    print(fib_element)

def gen_power():
    for _ in range(5):
        X = yield _ ** 2
        if X != None: print("From send: ", X)

y = gen_power()
print(y)
print(next(y))
print(next(y))
y.send(77)
print(next(y))
print(next(y))
print(next(y))
