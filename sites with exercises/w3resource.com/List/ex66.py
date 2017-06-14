list_of_list = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

max = 0
for element in list_of_list:
    sum_element = sum(element)
    if max < sum_element:
        max = sum_element
        current_max = element
print(current_max)