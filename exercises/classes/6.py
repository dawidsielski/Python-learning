class Employee:
    """Employee class"""
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename 

    def get_name(self):
        return self.name
    
    @property
    def get_fullname(self):
        return self.name + " " + self.surename
    
    @property
    def email(self):
        return self.name.lower() + "." + self.surename.lower() + "@company.com"

    def __str__(self):
        return self.name + " " + self.surename + " Email: " + self.email

    @get_fullname.setter
    def get_fullname(self, fullname):
        self.name, self.surename = fullname.split()

e1 = Employee('Dawid', "Sielski")

print(e1)
print(e1.name)
print(e1.get_name())
print(e1.get_fullname)

print(e1)
e1.name = "Dafciooo"
print(e1)
print(e1.email)

e2 = Employee.get_fullname = "Janusz Korkotrampki" #is this possible to do this that way
print(e2)