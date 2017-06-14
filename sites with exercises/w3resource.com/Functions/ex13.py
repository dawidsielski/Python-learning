def pascal(n):
    result = [1,1,1]

    row = [1]
    for i in range(3, (n + 1)):
        row.