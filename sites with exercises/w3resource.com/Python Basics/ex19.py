name = "Dawid"

def change_string(string):
    if (string[:2] == "ls"):
        return string
    else:
        return "ls" + string

print(change_string(name))
