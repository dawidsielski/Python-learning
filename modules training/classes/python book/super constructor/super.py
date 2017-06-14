class Super:
    def __init__(self, x):
        self.x = x

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        self.y = y

class Sub2(Super):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y



def main():
    x = Super(1)
    y = Sub(2,3)
    z = Sub2(4,5)

    print(z.x) #to check super().__init__ calling


if __name__ == "__main__":
    main()

    page 868