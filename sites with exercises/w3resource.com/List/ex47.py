def insert_before_each_element(l, element):
    result = []
    for i in range(len(l) * 2):
        if i % 2 == 0:
            result.append(element)
        else:
            result.append(l[int(i/2)])
    return result

print(insert_before_each_element([1,2,3,4], 90))