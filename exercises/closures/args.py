def args_closure():
    def closure(*args, **kwargs):
        for element in args:
            print(element)
        for key, value in kwargs.items():
            print("{}: {}".format(key, value))
    return closure

f = args_closure()
f(1,2,3,4, k = "key", v = "values")