# operaciones básicas de los complejos

from .complejos import Complejos

# adición
def sumar(Complejo z, Complejo w):
    return Complejo(z.real + w.real, z.imag + w.imag)

# sustraccion
def resta(Complejo z, Complejo w):
    return Complejo(z.real - w.real, z.imag - w.imag)

# producto
def producto(Complejo z, Complejo w):
    # de la forma (ac-bd, ad + cb)
    r = z.real * w.real - z.imag * w.imag
    i = z.real * w.imag - z.imag * w.real
    return Complejo(r, i)

# division
# sepa la bola xD
