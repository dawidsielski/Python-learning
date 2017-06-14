import time

def time_decorate(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution of " + func.__name__ + " took " + str((end - start) * 1000) + " in miliseconds.")
        return result
    return wrapper

@time_decorate
def square_list(l):
    result = []
    for element in l:
        result.append(element ** 2)
    return result

@time_decorate
def cube_list(l):
    result = []
    for element in l:
        result.append(element ** 3)
    return result


square_list(range(1000000))
cube_list(range(1000000))