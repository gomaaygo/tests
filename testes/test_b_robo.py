from basquete_robo import calcula

def test_ponto1():
    assert calcula(250) == 1

def test_ponto2():
    assert calcula(1400) == 2

def test_ponto3():
    assert calcula(1720) == 3

def test_ponto0():
    assert calcula(-1) == 0

def test_ponto0():
    assert calcula(2001) == 0