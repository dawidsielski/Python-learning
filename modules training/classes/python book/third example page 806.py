class ThirdClass:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return "Data inside is: " + str(self.data)


def main():
    x = ThirdClass(2)
    y = ThirdClass(3)
    print(x)
    print(y)
    print(x + 3)


if __name__ == "__main__":
    main()