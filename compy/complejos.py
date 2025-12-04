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
