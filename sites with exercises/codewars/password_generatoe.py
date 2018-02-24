import random
import string


def generate_password(length, password_type='strong'):
    if password_type == "strong":
        return "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length)])
    elif password_type == "medium":
        return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])
    elif password_type == "weak":
        return "".join([random.choice(string.ascii_letters) for _ in range(length)])
    else:
        return "Wrong type specified."


for i in range(100):
    print(generate_password(16))