from .complejos import Complejo
import random as rd

def complejo_random(a = 1, b = 1):
    return Complejo(rd.uniform(a, b), rd.uniform(a, b))

def i_elevado(n : int):
    if n >= 0:
        if n == 0:
            return 1
        elif n == 1:
            return Complejo.I
        elif n == 2:
            return -1
        elif n == 3:
            return i_elevado(2) * Complejo.I
        elif n == 4:
            return 1
        else:
            return Complejo.I * i_elevado(n - 1)
    else:
        return NotImplemented
