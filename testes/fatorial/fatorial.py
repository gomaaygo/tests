def fatorial(x):
    resultado = x

    if x < 0:
        return 0
    else:
        for y in range(1, x):
            resultado = resultado * y

    return resultado


def fatorial_recursivo(n):
    if n < 0:
        return 0;
    else:
        if n == 1:
            return 1
        else:
            return n * fatorial_recursivo(n-1)