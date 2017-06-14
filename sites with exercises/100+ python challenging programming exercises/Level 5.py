class Car(obiect):
    def __init__(self):
        self.name = ""

    def getString(self):
        self.name = str(input())

    def printName(self):
        print(self.name)



mercedes = Car()

mercedes.getString()
mercedes.printName()