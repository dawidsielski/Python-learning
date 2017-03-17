def multiply_list_elements(elements):
    result = 1
    for element in elements:
        result *= element
    return result

print(multiply_list_elements([1,2,3,4]))