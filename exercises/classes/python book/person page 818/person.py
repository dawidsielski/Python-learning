class Person:
    def __init__(self, name , job = None, pay = 0):
        self.name = name
        self. job = job
        self.pay = pay

    
def main():
    dawid = Person("Dawid Sielski", "dev", 2000)
    print(dawid)
    print(dawid.name)

    john = Person("John Ball")
    print(john.name)

    victor = Person("Victor", "dean")
    print(victor.name)
    print(victor.job)
    print(victor.pay)

if __name__ == "__main__":
    main()