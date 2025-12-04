from .complejos import Complejo
import random as rd

def complejo_random(a = 1, b = 1):
    return Complejo(rd.uniform(a, b), rd.uniform(a, b))
