def insert_element_at_the_beginning(_list, _element):
    result = []
    for i in _list:
        result.append(_element + str(i))
    return result

print(insert_element_at_the_beginning(range(10), 'emp'))