from collections import Counter
l = [1,2,3,4,4,3,2,3,6,4,7,4,99,99,99]
c = Counter(l)
print(c)

user_number = int(input("Enter number: "))
print("Your number appears " + str(c[user_number]) + " times in " + str(l))