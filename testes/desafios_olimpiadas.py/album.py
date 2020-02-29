"""Função recebe 5 parametros:
 1) representa o numero de espaço de figurinhas no album
 2) quantidade de figurinhas carimbadas que o album possui
 3) quantidade de figurinhas q o usuario comprou
 4) vetor que representa as figurinhas carimbadas
 5) vetor que representa as figurinhas carimbadas
"""
def fig_rest(numero_figs, n_figs_carimbadas, numero_figs_compradas, figs_carimbadas, figs_compradas):
    quant = 0
    for x in figs_compradas:
        if x in figs_carimbadas: # verifica se a figurinha comprada está contida no vetor de figurinhas carimbadas
            quant += 1

    return n_figs_carimbadas - quant
        
