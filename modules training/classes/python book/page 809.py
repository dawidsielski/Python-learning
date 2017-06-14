class Rec:
    pass

Rec.name = "John"

x = Rec()

print(x.name)

x.name = "David"

print(x.name)

print(x.__dict__)
print(Rec.__dict__)
print(Rec.__dict__.keys())

