n = 123
m = -432

def reverse_num(num):
    if num > 0:
        num = list(reversed(str(num)))
        print(int("".join(num)))
    else:
        num *= -1
        num = list(reversed(str(num)))
        print(int("".join(num)) * -1)


reverse_num(n)
reverse_num(m)