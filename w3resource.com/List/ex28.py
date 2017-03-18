items = [1,2,3,4,5,6]

def second_smallest(l):
    items = sorted(l, reverse=True)
    return(items[1])

print(second_smallest(items))
