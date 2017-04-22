class Person:
    def __init__(self, name , job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRise(self, percentage):
        self.pay = int(self.pay * (1 + percentage / 100))
    
    def __repr__(self):
        return "{} - {} - {}".format(self.name, self.job, self.pay)

class Manager(Person):
    def __init__(self, name, pay = 0):
        Person.__init__(self, name, "Manager", pay)
    def giveRise(self, percentage, bonus = 10):
        Person.giveRise(self, (percentage + (bonus / 100)))

class Department:
    def __init__(self, *args):
        if len(args) == 0:
            self.workers = []
        else:
            self.workers = list(args)

    def addPerson(self, person):
        self.workers.append(person)

    def showAll(self):
        for element in self.workers:
            print(element)


def main():
    dawid = Person("Dawid Sielski", "dev", 2000)
    print(dawid)
    print(dawid.name)
    print(dawid.lastName())
    dawid.giveRise(10)
    print(dawid.pay)

    john = Person("John Ball")
    print(john.name)

    victor = Person("Victor", "dean")
    print(victor.name)
    print(victor.job)
    print(victor.pay)

    tom = Manager("Tom Markowicz", 15000)
    tom.giveRise(11, 5)
    print(tom)

    print()
    programmers = Department(dawid, john)
    programmers.showAll()
    programmers.addPerson(tom)
    print("\nAfter Tom addition")
    programmers.showAll()

if __name__ == "__main__":
    main()