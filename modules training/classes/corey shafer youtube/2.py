class Employee:
    number_of_employees = 0

    def __init__(self, name, surename):
        self.name = name
        self.surename = surename
        Employee.number_of_employees += 1

    def get_name(self):
        return self.name

    def get_fullname(self):
        return self.name + " " + self.surename
        


e1 = Employee('Dawid', "Sielski")
e2 = Employee('Dawid', "Sielski")

print(e1)
print(e1.name)
print(e1.get_name())
print(e1.get_fullname())
print(Employee.number_of_employees)