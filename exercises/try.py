try:
    print(13/5)
except(ValueError):
    print("This is not valid expression.")


a = []
try:
    for i in range(1,10):
        a.append(i)

    for value in range(10):
        print(a[value])
except(IndexError):
    print("Test")
