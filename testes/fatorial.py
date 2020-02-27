def fatorial(x):
    resultado = x

    if x < 0:
        return 0
    else:
        for y in range(1, x):
            resultado = resultado * y

    return resultado