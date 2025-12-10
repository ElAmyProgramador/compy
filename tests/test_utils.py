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

def test_cap():
    z = Complejo(3, 2)
    w = Complejo(-4, -5)
    u = Complejo(2)
    assert cu.cap(z) == (3, 2)
    assert cu.cap(w) == (-4, -5)
    assert cu.cap(u) == (2)

def test_tac():
    a = (4, 3)
    b = (-3)
    assert cu.tac(a) == Complejo(4, 3)
    assert cu.tac(b) == Complejo(-3)

def test_i_elevado():
    for i in range(20):
        assert cu.i_elevado(i + 1) == 1 or -1 or Complejo.I or -Complejo.I

def test_es_complejo():
    a = 54
    b = Complejo(3, -2)
    assert cu.es_complejo(a) == False
    assert cu.es_complejo(b) == True

# hacer tests de conversión de ángulos
