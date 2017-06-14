list = [1,7,3,9,4,2,76,35,321,-34]
extracted_list = []

user_number = int(input("Enter your number: "))

for i in list:
    if i < user_number:
        print(i, end = " ")
        extracted_list.append(i)

print() # for extra enter
print(extracted_list)
