def print_binary(n):
    n = bin(n)
    n = str(n)[2:]
    n = list(reversed(n))
    for i in range(len(n)):
        if n[i] == '1': 
            n = n[i:]
            break
    ending_zeros = 32 - len(n)
    for i in range(ending_zeros - 1):
        n.append("0")
    print(int("".join(n), 2))


print_binary(1234)