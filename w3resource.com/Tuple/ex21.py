l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for element in l:
    element = element[:len(element) - 1] + (100,)
    print(element)