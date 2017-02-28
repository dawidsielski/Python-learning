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
print(names)


print([ (x,y) for x in range(5) for y in range(3) ])

words = ['anna', 'ala', 'ela', 'wiola', 'ola']
print([ [name, name[0]] for name in words if len(name) == 3 ])

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