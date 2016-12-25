import random

list = random.sample(range(100), random.randint(2,15))
print(list)

new_list = []
new_list.append(list[0])

last_element = len(list) - 1
new_list.append(list[last_element])

print(new_list)
