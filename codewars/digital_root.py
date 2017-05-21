
def digital_root(n):
    while len(str(n)) >= 2:
        n = sum(list([int(x) for x in str(n)]))
    return n

digital_root(999)