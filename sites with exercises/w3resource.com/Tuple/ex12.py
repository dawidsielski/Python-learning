def remove_nth_element(tup, n):
    return (tup[:n] + tup[n+1:])

print(remove_nth_element((1,2,3,4), 3))