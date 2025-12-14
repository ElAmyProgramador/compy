# aqui se definen los commplejos e intentar que sean tomados como un tipo de dato más como int, float, etc
# Es solo la estuctura / clase

from __future__ import annotations # para usar la clase dentro de la definición de la clase

class Complejo:
    # método constructor
    def __init__(self, real, imag=None) -> None:
        if imag is None:
            self.real = real
            self.imag = 0
        else:
            self.real = real
            self.imag = imag

    # funcion para escribir un numero de la forma a + bi convencional
    def __repr__(self) -> str:
        if self.imag == 0:
            return f"{self.real}"
        elif self.imag == 1:
            return f"{self.real} + i"
        elif self.imag < 0:
            # abusando de los ifs
            if self.imag == -1:
                return f"{self.real} - i"
            else:
                return f"{self.real} {self.imag}i"
        else:
            return f"{self.real} + {self.imag}i"

    # estas funciones son para hacer z x w como si fueran de tipo int, float, etc
    # suma
    def __add__(self, otro : Complejo | float | int) -> Complejo:
        # Como a + 0i es un complejo y un real, si a un numero a + bi le sumamos c + 0i tenemos a + c + bi 
        if isinstance(otro, Complejo):
            return Complejo(self.real + otro.real, self.imag + otro.imag)
        elif isinstance(otro, (int, float)):
            return Complejo(self.real + otro, self.imag)
        else:
            raise TypeError("No se puede sumar con este tipo de dato")

    # resta
    def __sub__(self, otro : Complejo | float | int) -> Complejo:
        if isinstance(otro, Complejo):
            return Complejo(self.real - otro.real, self.imag - otro.imag)
        elif isinstance(otro, (int, float)):
            return Complejo(self.real - otro, self.imag)
        else:
            raise TypeError("No se puede restar con este tipo de dato")
        
    # Multiplicación
    def __mul__(self, otro : Complejo | float | int) -> Complejo:
        if isinstance(otro, Complejo):
            # multiplicacion normal en los complejos
            # caso especial en el que se mútiplica un complejo por su conjugado
            if otro == self.conjugado():
                return self.real ** 2 + self.imag ** 2
            else:
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

    def __rmul__(self, otro : Complejo | float | int) -> Complejo:
        return self.__mul__(otro)

    # división
    def __truediv__(self, otro) -> Complejo:
        if isinstance(otro, (float, int)):
            if otro == Complejo.CERO:
                raise ZeroDivisionError("División sobre 0")
            else:
                return Complejo(self.real / otro, self.imag / otro)
        elif isinstance(otro, Complejo):
            if otro == 0:
                raise ZeroDivisionError("División sobre 0")
            else:
                d = otro.real ** 2 + otro.imag ** 2
                r = (self.real * otro.real + self.imag * otro.imag) / d
                i = (self.imag * otro.real - self.real * otro.imag) / d
                return Complejo(r, i)
        else:
            raise TypeError("No se puede operar con este tipo de dato")

    def __rtruediv__(self, otro) -> Complejo:
        if isinstance(otro, (int, float)):
            if otro == 0:
                raise ZeroDivisionError("División por 0")
            else:
                d = self.real**2 + self.imag**2
                return Complejo(otro * self.real / d, -otro * self.imag / d)

    # Igualdad
    def __eq__(self, otro : Complejo | float | int) -> bool:
        return self.real == otro.real and self.imag == otro.imag

    # Negativo
    def __neg__(self) -> Complejo:
        return Complejo(-self.real, -self.imag)

    # pos
    def __pos__(self) -> Complejo:
        return self

    # potencia
    def __pow__(self, n : int) -> Complejo:
        if not isinstance(n, int):
            raise TypeError("El exponente debe ser un número entero")

        if n == 0:
            return Complejo.UNO
        elif n < 0:
            return Complejo.UNO / (self ** (-n))
        else:
            res = Complejo.UNO
            for _ in range(n):
                res *= self
            return res

    # el conjugado de un numero complejo
    def conjugado(self) -> Complejo:
        #return Complejo(self.real, -self.imag)
        if self.imag == 0:
            return self.real
        else:
            return Complejo(self.real, -self.imag)


    # Módulo, magnitud
    def modulo(self) -> float:
        return (self.real**2 + self.imag**2) ** 0.5

    # un vector complejo con la misma dirección que su vector padre
    def normalizar(self) -> Complejo:
        mod = self.modulo()
        if mod != 0:
            re = self.real / mod
            im = self.imag / mod
            return Complejo(re, im)
        else:
            Complejo.Cero

    # obtiene el argumento/angulo de un numero complejo
    def arg(self) -> float:
        from math import atan2
        return atan2(self.imag, self.real)

    # obtiene la forma polar de un complejo
    def polar(self) -> (float, float):
        r = self.modulo()
        theta = self.argumento()
        return (r, theta)

    # un método para graficar un solo objeto
    def graficar(self) -> None:
        import matplotlib.pyplot as plt
        plt.axhline(0, color = "black", lw = 0.5)
        plt.axvline(0, color = "black", lw = 0.5)
        plt.xlabel("Re")
        plt.ylabel("Im")
        plt.axis("equal")
        plt.grid(True)
        plt.scatter(self.real, self.imag, s = 120)
        plt.text(self.real, self.imag, f"{self}")
        plt.show()

    def graficar_vector(self) -> None:
        import matplotlib.pyplot as plt
        plt.axhline(0, color = "black", lw = 0.5)
        plt.axvline(0, color = "black", lw = 0.5)
        plt.quiver(0, 0, self.real, self.imag, angles = "xy", scale_units = "xy", scale = 1, color = "blue")
        plt.xlim(min(0, self.real) - 1, max(0, self.real) + 1)
        plt.ylim(min(0, self.imag) - 1, max(0, self.imag) + 1)
        plt.gca().set_aspect("equal", adjustable = "box")
        plt.grid(True)
        plt.show()

# constantes del campo
Complejo.CERO = Complejo(0)
Complejo.UNO = Complejo(1)
Complejo.I = Complejo(0, 1)
Complejo.I2 = Complejo(-1)
