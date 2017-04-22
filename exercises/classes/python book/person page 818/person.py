class Person:
    def __init__(self, name , job = None, pay = 0):
        self.name = name
        self. job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRise(self, percentage):
        self.pay = int(self.pay * (1 + percentage / 100))
    
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

if __name__ == "__main__":
    main()