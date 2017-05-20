class Person:
    def __init__(self):
        self.name = ""
        self.surename = ""

    def print_name(self):
        pass


def print_obj(obj):
    print(obj.getattr)


# print_obj(Person)
print(dir(Person))
print(Person.__dict__)