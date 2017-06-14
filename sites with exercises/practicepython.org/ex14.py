import random

list1 = random.sample(range(10),10)
list2 = random.sample(range(10),10)
sum_of_lists = list1 + list2

def delete_repeting_elements(listname):
    convertion = set(listname)
    convertion = list(convertion)
    return convertion

print(delete_repeting_elements(sum_of_lists))
