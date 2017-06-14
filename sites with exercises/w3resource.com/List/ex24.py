import random
items = [1,2,3,4]

def print_random_element(iterable):
    print(iterable[random.randint(0, len(iterable) - 1)])

print_random_element(items)

print(random.choice(items))