"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""

def move_zeros(array):
    without_zeros = [x for x in array if not x == 0]
    only_zeros = [x for x in array if x == 0]
    return without_zeros + only_zeros

print(move_zeros([1,0,1,2,0,1,3,"a"]))
print(move_zeros([9, 0.0, 9, 1, 2, 1, 1, 0.0, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0]))
print(move_zeros(['a', 'b', None, 'c', 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, False, 0, 0, 0, 0, 0, 0, 0]))