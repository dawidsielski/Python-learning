def common_element(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

print(common_element([1,2,3], [3,4,5]))
print(common_element([1,2,3], [6,4,5]))