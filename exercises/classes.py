class Person:
    number_of_persons = 0

    def __init__(self, name, surename, age):
        self.name = name
        self.surename = surename
        self.age = age
        Person.number_of_persons += 1

    def printPerson(self):
        print("Name:", self.name, "Surename:", self.surename, "Age:" , self.age)


person = Person("Dawid", "Sielski", 21)
person1 = Person("Dawid", "Sielski", 21)

person.printPerson()

print(Person.number_of_persons)
