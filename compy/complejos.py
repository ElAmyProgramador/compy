# aqui se definen los commplejos e intentar que sean tomados como un tipo de dto más como int, float, etc
# Es solo la estuctura / clase

class Complejo:
    # método constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # funcion para escribir un numero de la forma a + bi convencional
    def __repr__(self):
        return f"({self.real} + {self.imag}i)"

    # el conjugaod de un numero complejo
    def Conjugado(self):
        return Complejo(self.real, -self.imag)
    
    # estas funciones son para hacer z + w como is fueran de tipo int, float, etc
    # suma
    def __add__(self, otro):
        return Complejo(self.real + otro.real, self.imag + otro.imag)

    # resta
    def __sub__(self, otro):
        return Complejo(self.real - otro.real, self.imag - otro.imag)

    # Multiplicación
    def __mul__(self, otro):
        r = self.real * otro.real - self.imag * otro.imag
        i = self.real * otro.imag + self.imag * otro.real
        return Complejo(r, i)

    # Módulo
    def modulo(self):
        return (self.real**2 + self.imag**2) ** 0.5

    # Igualdad
    def __eq__(self, otro):
        return self.real == otro.real and self.imag == otro.imag
