# aqui se definen los commplejos e intentar que sean tomados como un tipo de dato más como int, float, etc
# Es solo la estuctura / clase

class Complejo:
    # método constructor
    def __init__(self, real, imag=None):
        if imag is None:
            self.real = real
            self.imag = 0
        else:
            self.real = real
            self.imag = imag

    # funcion para escribir un numero de la forma a + bi convencional
    def __repr__(self):
        return f"{self.real} + {self.imag}i"

    # el conjugado de un numero complejo
    def conjugado(self):
        return Complejo(self.real, -self.imag)
    
    # estas funciones son para hacer z x w como si fueran de tipo int, float, etc
    # suma
    def __add__(self, otro):
        # Como a + 0i es un complejo y un real, si a un numero a + bi le sumamos c + 0i tenemos a + c + bi 
        if isinstance(otro, Complejo):
            return Complejo(self.real + otro.real, self.imag + otro.imag)
        elif isinstance(otro, (int, float)):
            return Complejo(self.real + otro, self.imag)
        else:
            raise TypeError("No se puede sumar con este tipo de dato")

    # resta
    def __sub__(self, otro):
        if isinstance(otro, Complejo):
            return Complejo(self.real - otro.real, self.imag - otro.imag)
        elif isinstance(otro, (int, float)):
            return Complejo(self.real - otro, self.imag)
        else:
            raise TypeError("No se puede restar con este tipo de dato")
        
    # Multiplicación
    def __mul__(self, otro):
        if isinstance(otro, Complejo):
            # multiplicacion normal en los complejos
            r = self.real * otro.real - self.imag * otro.imag
            i = self.real * otro.imag + self.imag * otro.real
            return Complejo(r, i)
        elif isinstance(otro, (int, float)):
            # basicamente multipliacion por un escalar
            r = self.real * otro
            i = self.imag * otro
            return Complejo(r, i)
        else:
            raise TypeError("No se puede operar con este tipo de dato")

    def __rmul__(self, otro):
        return self.__mul__(otro)

    # Módulo o magnitud
    def modulo(self):
        return (self.real**2 + self.imag**2) ** 0.5

    # Igualdad
    def __eq__(self, otro):
        return self.real == otro.real and self.imag == otro.imag
