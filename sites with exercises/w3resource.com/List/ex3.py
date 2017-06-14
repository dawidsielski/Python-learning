def largest(items):
    items = sorted(items, reverse=True)
    return items[0]

print(largest([2,3,5,1,23,5,2,34]))