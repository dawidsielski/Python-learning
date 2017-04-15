class Employee:
    number_of_employees = 0

    def __init__(self, name, surename, salary = None):
        self.name = name
        self.surename = surename
        self.salary = salary
        Employee.number_of_employees += 1

    def get_name(self):
        return self.name
        
    # def __add__(self, e1, e1)

    def __str__(self):
        return self.name + " " + self.surename + " Salary: " + str(self.salary)

e1 = Employee('Dawid', "Sielski", 3000)
e2 = Employee('Dawid', "Sielski")

print(e1)
print(e1.name)
print(e1.get_name())
print(Employee.number_of_employees)
print(e2)