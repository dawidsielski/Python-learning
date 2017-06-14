class Person:
    name = "Person"

    def __init__(self, name = ""):
        self.name = name


dawid = Person("Dawid")
adrianna = Person("Adrianna")

print(dawid.name)
print(adrianna.name)
print(Person.name)