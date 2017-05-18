def greet(name):
    def inner_function():
        print("Hello," + name)
    return inner_function


greet_john = greet('John')
print(greet_john)
greet_john()