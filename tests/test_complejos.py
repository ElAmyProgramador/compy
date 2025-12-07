from compy.complejos import Complejo

def test_creacion():
    z = Complejo(3, 4)
    assert z.real == 3
    assert z.imag == 4

def test_repr():
    z = Complejo(2, 1)
    w = Complejo(4, 3)
    u = Complejo(3, -5)
    assert str(z) == "2 + i"
    assert str(w) == "4 + 3i"
    assert str(u) == "3 -5i"
    assert str(z.conjugado()) == "2 - i"

def test_suma_escalar():
    z = Complejo(5, 2)
    res = z + 5
    assert res.real == 10
    assert res.imag == 2

def test_suma_complejos():
    z = Complejo(3, 1)
    w = Complejo(2, 3)
    res = z + w
    assert res.real == 5
    assert res.imag == 4

def test_resta_complejos():
    z = Complejo(1, 2)
    w = Complejo(3, 1)
    res = z - w
    assert res.real == -2
    assert res.imag == 1

def test_resta_escalar():
    z = Complejo(12, -2)
    res = z - 5
    assert res.real == 7
    assert res.imag == z.imag

def test_producto_complejos():
    z = Complejo(3, 1)
    w = Complejo(2, 3)
    res = z * w
    assert res.real == 3
    assert res.imag == 11

def test_producto_complejos_conjugado():
    z = Complejo(3, 2)
    res = z * z.conjugado()
    assert res == 13

def test_producto_complejos_escalar():
    z = Complejo(12, 14)
    res1 = z * 5
    res2 = 5 * z
    assert res1.real == 60
    assert res1.imag == 70
    assert res2.real == 60
    assert res2.imag == 70

def test_producto_complejos_conmutatividad():
    z = Complejo(8, 9)
    w = Complejo(3, -4)
    u = Complejo(2, 2)
    assert z * w == w * z
    assert z * u == u * z
    assert w * u == u * w

def test_producto_transitividad():
    z = Complejo(4, 5)
    w = Complejo(7, -1)
    u = w
    assert z * w == z * u
    assert w == u
