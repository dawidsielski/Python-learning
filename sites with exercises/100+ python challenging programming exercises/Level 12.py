for i in range(2000, 3001):
    string_number = str(i)
    if int(string_number[0]) % 2 == 0 and int(string_number[1]) % 2 == 0 and int(string_number[2]) % 2 == 0 and int(string_number[3]) % 2 == 0:
        print(i, end = ", ")