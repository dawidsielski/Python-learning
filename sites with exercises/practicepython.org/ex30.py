import random
file_name = open("sowpods.txt", "r")
content = file_name.readlines()
# print(content)

random_word = content[random.randrange(len(content))]

print(random_word, end="")
