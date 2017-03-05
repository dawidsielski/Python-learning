n = int(input())

even = [x for x in range(0,n + 1, 2)]
print(",".join([str(x) for x in even]))