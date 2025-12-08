from compy.complejos import Complejo
import compy.utils as cu

def test_parte_real():
    z = Complejo(2, 3)
    w = Complejo(-4, -3)
    assert cu.es_real_pos(z) == True
    assert cu.es_real_pos(w) == False
    assert cu.es_real_neg(z) == False
    assert cu.es_real_neg(w) == True

def test_parte_imag():
    z = Complejo(3, 1)
    w = Complejo(5, -8)
    assert cu.es_imag_pos(z) == True
    assert cu.es_imag_pos(w) == False
    assert cu.es_imag_neg(z) == False
    assert cu.es_imag_neg(w) == True
