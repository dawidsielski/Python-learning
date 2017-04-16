class Person:
    number_of_persons = 0

    def __init__(self, name = None, surename = None, age = None):
        self.name = name
        self.surename = surename
        self.age = age
        Person.number_of_persons += 1

    def printPerson(self):
        print("Name:", self.name, "Surename:", self.surename, "Age:" , self.age)

    def __str__(self):
        return "{} {} Age: {}".format(self.name, self.surename, self.age)

    @property
    def personName(self):
        return self.name + " " + self.surename

    @personName.setter
    def personName(self, name):
        self.name, self.surename = name.split()

    
person = Person("Dawid", "Sielski", 21)
person1 = Person("Dawid", "Sielski", 21)

person2 = Person()
person2.personName = "Maja Towar"
print(person2)
print(person2.personName)

person.printPerson()

print(Person.number_of_persons)
