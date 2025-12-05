from compy.complejos import Complejo

def test_creacion():
    z = Complejo(3, 4)
    assert z.real == 3
    assert z.imag == 4

def test_repr():
    z = Complejo(2, 1)
    assert str(z) == "2 + i"

def test_suma_escalar():
    z = Complejo(5, 2)
    res = z + 5
    assert res.real == 10
    assert res.imag == 2
