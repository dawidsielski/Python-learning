class Employee:
    def __init__(self, name, surename):
        self.name = name
        self.surename = surename
        self.email = self.name.lower() + "." + self.surename.lower() + "@company.com"

    def get_name(self):
        return self.name

    def get_fullname(self):
        return self.name + " " + self.surename
    
    def get_email(self):
        return self.email

    def __str__(self):
        return self.name + " " + self.surename + " Email: " + self.email

e1 = Employee('Dawid', "Sielski")

print(e1)
print(e1.name)
print(e1.get_name())
print(e1.get_fullname())

print(e1)
e1.name = "Dafciooo"
print(e1)
