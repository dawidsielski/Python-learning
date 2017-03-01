even_numbers = [0, 100, 2]

for number in range(*even_numbers):
    print(number, end = " ")

print()

country = { "country":"Poland", "capital":"Warsaw"}
def print_countries(country, capital):
    """Prints countries in the following format: "[capital] is the capital of [country]." """
    print("{0} is the capital of {1}.".format(capital, country))

print_countries(**country)

countries = ["Poland", "Gernamy", "Netherlands"]
capitals = ["Warsaw", "Berlin", "Amsterdam"]

merged = zip(countries, capitals)
countries_dict = dict(merged)
print(countries_dict)

for key, value in countries_dict.items(): #to repeat
    print(key, ", ", value)

print()

words = ["David", "Ilona"]
names = (element.capitalize() for element in words)

for name in names:
    print(name)
#print(names) will not work


print([ (x,y) for x in range(5) for y in range(3) ])

words = ['anna', 'ala', 'ela', 'wiola', 'ola']
print([ [name, name[0]] for name in words if len(name) == 3 ])

def names_filter(word):
    if len(word) == 3:
        return True
    return False

print(list(filter(names_filter, words)), "Using dedicated function")
print(list(filter(lambda x: len(x) == 3, words)), "Using lambda function")

def increment(number):
    """Increments number by 1"""
    return number + 1

numbers = [1,3,5,7]
print("Incremented numbers before: ", numbers)
incremented_numbers = list(map(increment,numbers))
print("Incremented numbers: ", incremented_numbers)

a = 1
print([[a for y in range(3)] for x in range(2)])

print([ (x,y) for x in range(5) for y in range(3) ])


numbers_bigger_than_four = filter(lambda x: x > 4, incremented_numbers)
print("Numbers bigger than four ",list(numbers_bigger_than_four))

pupils = [
    ('jan','Nowak','1A',15),
    ('ola','Kujawiak','3B',17),
    ('andrzej','Bilski','2F',16),
    ('kamil','Czuja','1B',14)
]

sorted_by_surename = sorted(pupils, key = lambda pupils: pupils[1])
print("Pupils sorted by surename ", sorted_by_surename)

txt_file = open("text.txt", "w")
for i in range(10):
    txt_file.write("Dawid\n")
txt_file.close()

with open("text.txt", "r") as text_file:
    for line in text_file:
        print(line, end = "")

print()

for line in open('text.txt', 'r'):
    print(line, end = "")


def generate_even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

gen = generate_even(10)
print(next(gen))
print(next(gen))


print("Generate factorial.")
def generate_factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

gen = generate_factorial(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))