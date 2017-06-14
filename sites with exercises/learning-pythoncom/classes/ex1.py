class Adder:
    def add(self, x, y):
        print("Not implemented!")

    def __init__(self ,a = []):
        self.data = a

    def __add__(self, a):
        return self.add(self.data, a)

class ListAdder(Adder):
    def add(self, a, b):
        self.data = a + b
        return self.data


class DictAdder(Adder):
    def add(self, x, y):
        new = {}
        for k in x.keys(): new[k] = x[k]
        for k in y.keys(): new[k] = y[k]
        return new


def main():
    a = Adder()
    b = Adder()
    c = Adder.add(a, b, a)
    b.add(1,5)

    x = ListAdder()
    x.add([1], [1])
    print(x.data)

    d1 = DictAdder()
    print(d1.add({1:1}, {2:2}))


if __name__ == "__main__":
    main()