"""
Find and return largest element from a given list
Function takes list l as an argument and returns the biggest element.
"""

def find_largest(l):
    l.sort()
    return l[-1]


print(find_largest([1,5,3,5,78,8,3,6,4]) == 78)
print(find_largest([1,5,3,50,7,8,3,6,4]) == 50)
print(find_largest([1,5,3,5,78,8,300,6,4]) == 300)
print(find_largest([1,5,45644643,5,78,8,3,623424,4456]) == 45644643)
print(find_largest([0]) == 0)