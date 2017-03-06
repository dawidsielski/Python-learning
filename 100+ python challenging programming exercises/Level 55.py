"""line 1907"""
import random
for i in range(100):
    random_even = random.choice([2*x for x in range(6)]) 
    print(random_even, end = " ")