prime_numbers = open("primenumbers.txt", "r")
happy_numbers = open("happynumbers.txt", "r")

primenumbers = prime_numbers.readlines()
happynumbers = happy_numbers.readlines()

primenumbers = list(primenumbers)
happynumbers = list(happynumbers)

prime_list = []
happy_list = []
for line in primenumbers:
    prime_list.append(int(line))

for line in happynumbers:
    happy_list.append(int(line))


print(prime_list)
print(happy_list)

overlaping = []
for i in prime_list:
    if i in happy_list:
        overlaping.append(i)

print(overlaping)
