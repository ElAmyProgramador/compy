from .complejos import Complejo

def es_real_pos(z : Complejo) -> bool:
    if z.real >= 0:
        return True
    else:
        return False

def es_imag_pos(z : Complejo) -> bool:
    if z.imag >= 0:
        return True
    else:
        return False

def es_real_neg(z : Complejo) -> bool:
    if z.real < 0:
        return True
    else:
        return False

def es_imag_neg(z : Complejo) -> bool:
    if z.imag < 0:
        return True
    else:
        return False

def complejo_random(a = 1, b = 1):
    import random as rd
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
