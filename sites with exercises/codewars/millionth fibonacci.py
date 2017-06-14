def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    i = 0
    a, b = 0, 1
    while i < n - 2:
        a, b = b, a + b
        # print(a, b)
        i += 1
    return b


for _ in range(10):
    print(_, fib(_))


print(fib(100000 * 3))