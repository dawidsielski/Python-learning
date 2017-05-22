"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""
def maxSequence(arr):
    max = 0
    for number_list in range(1, len(arr)):
        for starting_point in range(len(arr) - number_list):
            x = sum(arr[starting_point:starting_point + number_list])
            if max < x:
                max = x
            x = sum(arr[len(arr) - (starting_point + number_list) - 1:len(arr) - starting_point])
            if max < x:
                max = x
    return max

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))