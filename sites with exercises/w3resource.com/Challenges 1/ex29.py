l = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]

def print_majority(lis):
    s = list(set(lis))
    for element in s:
        if lis.count(element) >= len(lis) / 2:
            print(element) 


print_majority(l)