def find_items(items, n):
    for element in items:
        if len(element) >= n:
            print(element)


words = "aslk dlkjs ajsdkl dufu su a yusdoiu doiufy".split()

find_items(words, 5)