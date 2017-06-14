import random
characters = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNORSTUWXYZ1234567890!@#$%^&*()_+=,./;'[]<>?:\{\}|"

def set_type(password_type):
    if password_type == 1:
        return random.randrange(16,24)
    elif password_type == 2:
        return random.randrange(12,15)
    else:
        return random.randrange(6,11)

def generate_password(pass_type):
    password = []
    for i in range(set_type(pass_type)):
        password.append(characters[random.randrange(len(characters))])
    password = "".join(password)
    return password

for i in range(100):
    password_type = random.randint(1,3)
    print(generate_password(password_type))
