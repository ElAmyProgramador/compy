# operaciones básicas de los complejos

from .complejos import Complejo
import math

'''
    Operaciones básicas
    Solo si los objetos son numeros complejos (de momento)
'''

# adición
def sumar(z : Complejo, w : Complejo) -> Complejo:
    return Complejo(z.real + w.real, z.imag + w.imag)

# sustraccion
def resta(z : Complejo, w : Complejo) -> Complejo:
    return Complejo(z.real - w.real, z.imag - w.imag)

# producto
def producto(z : Complejo, w : Complejo) -> Complejo:
    # de la forma (ac-bd, ad + cb)
    r = z.real * w.real - z.imag * w.imag
    i = z.real * w.imag - z.imag * w.real
    return Complejo(r, i)

# division
# sepa la bola xD

def exp(z : Complejo) -> Complejo:
    r = math.exp(z.real) * math.cos(z.imag)
    i = math.exp(z.real) * math.sin(z.imag)
    return Complejo(r, i)
