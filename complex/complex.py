class ComplexNum:
    def __init__(self, real = 0, imag = 0):
        self.imag = imag
        self.real = real

    def real(self):
        return self.real

    def imag(self):
        return self.imag

    def __str__(self):
        if self.imag < 0:
            return (str(self.real) + " - " + str(abs(self.imag)) + "i")
        return (str(self.real) + " + " + str(self.imag) + "i")

    def __add__(self, other):
         imag = self.imag + other.imag
         real = self.real + other.real
         return ComplexNum(real,imag)

    def __sub__(self, other):
         imag = self.imag - other.imag
         real = self.real - other.real
         return ComplexNum(real,imag)

    def __mul__(self,other):
        imag = self.imag * other.real + self.real * other.imag
        real = (self.real * other.real) - (self.imag * other.imag)
        return ComplexNum(real,imag)

    def conjugate(self):
        if self.imag <= 0:
            imag = abs(self.imag)
        else:
            imag = -1*(self.imag)
        return ComplexNum(self.real,imag)

    def __truediv__(self,other):
        real = (self.real * other.real + self.imag * other.imag) / (other.real**2 + other.imag**2)
        imag = (self.imag * other.real - self.real * other.imag) / (other.real**2 + other.imag**2)
        return ComplexNum(real,imag)
