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

    @classmethod
    def set_full_name(cls, emp_str):
        name, surename = emp_str.split()
        return cls(name, surename)
    
    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

e1 = Employee('Dawid', "Sielski")
e2 = Employee('Dawid', "Sielski")

print(e1)
print(e1.name)
print(e1.get_name())
print(e1.get_fullname())
print(Employee.number_of_employees)

e2 = Employee.set_full_name("Magdalena Ulica")
print(e2.get_fullname())

import datetime
print(datetime.date.today())
print(Employee.is_working_day(datetime.date.today()))