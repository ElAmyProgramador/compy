# operaciones básicas de los complejos

from .complejos import Complejo

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
