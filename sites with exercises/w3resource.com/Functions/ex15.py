def print_sorted(s):
    s = s.split("-")
    s.sort()
    return ("-".join(s))

print(print_sorted("green-yellow-orange-purple"))