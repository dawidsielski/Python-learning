l1 = [{},{},{}]
l2 = [{1,2},{},{}]


def if_empty(it):
    for element in it:
        if element:
            return False
    return True

print(if_empty(l1))
print(if_empty(l2))