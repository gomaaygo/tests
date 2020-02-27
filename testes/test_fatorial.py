from fatorial import fatorial

def test_fatorial2():
    assert fatorial(2) == 2

def test_fatorial3():
    assert fatorial(3) == 6 

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120

def test_fatorial_negativo():
    assert fatorial(-1) == 0      