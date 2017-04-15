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
        

class Developer(Employee):
    
    def __init__(self, name, surename, prog_language):
        super().__init__(name, surename)
        self.prog_language = prog_language
    
    def get_full_name(self):
        return self.name + " " + self.surename + " " + self.prog_language


class Manager(Employee):
    def __init__(self, name, surename, workers = None):
        super().__init__(name, surename)
        if workers is None:
            self.workers = []
        else:
            self.workers = workers
    
    def add_worker(self, worker):
        self.workers.append(worker)

e1 = Employee('Dawid', "Sielski")

print(e1)
print(e1.name)
print(e1.get_name())
print(e1.get_fullname())
print(Employee.number_of_employees)

e2 = Developer('Dawid', "Sielski", "Python")
print(e2.get_full_name())

m1 = Manager("Andrew", "ROmanowski")

worker = Employee("Marzanna", "Wiosenna")
worker1 = Employee("Peter", "Ball")
m1.add_worker(worker)
m1.add_worker(worker1)

for element in m1.workers:
    print(element.get_fullname())