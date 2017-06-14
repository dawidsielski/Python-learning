import random

random_list = random.sample(range(100), random.randint(10,40))
random_list.sort()
print(random_list)

i, j = 0 , len(random_list) - 1
middle = int((i + j) / 2)
user_input =  90 #int(input("Enter Your number:"))
while i <= j:
    middle = int((i + j) / 2)
    if random_list[middle] == user_input:
        print(random_list[middle])
        break
    else:
        if random_list[middle] > user_input:
            i = middle - 1
        else:
            j = middle + 1


print(i)
