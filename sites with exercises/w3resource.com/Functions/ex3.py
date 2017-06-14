def multiply_all(l):
    """Return multiplication of all the elements in the given list."""
    result = 1
    for element in l:
        result *= element
    return result


print(multiply_all([1,6,3]))