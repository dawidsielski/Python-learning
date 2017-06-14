user_string = "a3"

def operation(string , n):
    if len(string) >= 2:
        return string[:2] * n
    else:
        return string * n

print(operation(user_string,10))
