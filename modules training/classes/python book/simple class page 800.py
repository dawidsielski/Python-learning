class Anything:
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data

class Anything2(Anything):
    
    @property
    def display(self):
        print(self.data)



def main():
    x = Anything()
    x.set_data("Dawid")
    print(x.get_data())

    y = Anything2()
    y.set_data("Kazimierz")
    y.display


if __name__ == "__main__":
    main()