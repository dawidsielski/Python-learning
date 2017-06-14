def decorator(f):
    def wrapper(numbers):
        print("Inside wrapper before call")
        print(f(numbers))
        print("Inside wrapper after call")
    return wrapper

@decorator
def return_list(l):
    return l

numbers = [1,2,3,4]
return_list(numbers)