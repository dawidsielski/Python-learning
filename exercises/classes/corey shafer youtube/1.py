class Employee:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename

    def get_name(self):
        return self.name

    def get_fullname(self):
        return self.name + " " + self.surename
    
    def __str__(self):
        return self.name + " " + self.surename
        


e1 = Employee('Dawid', "Sielski")
e2 = Employee('John', "Brown")

print(e1)
print(e1.name)
print(e1.get_name())
print(e1.get_fullname())