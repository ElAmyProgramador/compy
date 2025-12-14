from .complejos import Complejo

# una especie de get, pero que pregunta por el simbolo
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

# crear complejos pseudoaleatorios
def complejo_random(a = 1, b = 1) -> Complejo:
    import random as rd
    return Complejo(rd.uniform(a, b), rd.uniform(a, b))

# este ejercicio viene deu n examen, la pregunta:
# Demuestra que para todo n en los naturales i elevado a la n solo puede tener como valor a i, -i, 1, -1
def i_elevado(n : int) -> Complejo | int:
    n %= 4
    match n:
        case 0:
            return 1
        case 1:
            return Complejo.I
        case 2:
            return -1
        case 3:
            return -Complejo.I

# utilidades de complejos y tuplas (debido a esto, es probable que esta alibreria solo trabaje en python <= 3.9)
# cap : Complejo a tupla
def cap(z : Complejo) -> tuple[float | int, float | int]:
    return (z.real, z.imag)

# tac : tupla a complejo
def tac(p : tuple[int | float, int | float] | float | int) -> Complejo:
    if isinstance(p, tuple):
        return Complejo(p[0], p[1])
    else:
        return Complejo(p)

# normalizar
def normalizar(z : Complejo) -> float | int:
    modu = z.modulo()
    if modu != 0:
        re = z.real / modu
        im = z.imag / modu
        return Complejo(re, im)
    else:
        return Complejo.Cero

# conversiones de radianes a grados y viceversa
def rad_a_grad(rad : float) -> float:
    from math import pi
    return rad * 180 / pi

def grad_a_rad(grad : float) -> float:
    from math import pi
    return grad * pi / 180

# validacion de tipo
def es_complejo(x) -> bool:
    return isinstance(x, Complejo)
