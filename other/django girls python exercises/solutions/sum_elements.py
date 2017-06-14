"""
Your task is to sum all the elements that are divisible by 7 from the specific range
Function takes starting point argument and ending point argument.
Function returns sum satisfying
"""

def sum_elements(starting_point, ending_point):
    # Put your code here
    sum = 0
    for number in range(starting_point, ending_point):
        if number % 7 == 0:
            sum += number
    return sum


print(sum_elements(7,20) == 21)
print(sum_elements(5,190) == 2646)
print(sum_elements(65,130) == 882)
print(sum_elements(-5,2) == 0)
print(sum_elements(0,80) == 462)

# You can also do it quicker using list comprehentions
def sum_elements_quick(starting_point, ending_point):
    # Put your code here
    return sum([x for x in range(starting_point, ending_point) if x % 7 == 0])

print(sum_elements_quick(7,20) == 21)
print(sum_elements_quick(5,190) == 2646)
print(sum_elements_quick(65,130) == 882)
print(sum_elements_quick(-5,2) == 0)
print(sum_elements_quick(0,80) == 462)