def remove_nth(string, n):
    return string[:n] + string[n + 1:]


print(remove_nth("Dawid", 3))