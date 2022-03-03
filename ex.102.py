def fatorial(n, show=False):
    """
    -->Função para calcular o fatorial de um número.
    :param n: Valor que será calculado.
    :param show: Variável lógica para determinar se será mostrado a sequencia  de operação
    :return: Retorna o resultado da operação
    """
    fato = 1
    if show is True:
        for i in range(n, 0, -1):
            if i == 1:
                print(i, end=f" = {fato}")
                break
            print(i, end=" x ")
            fato *= i
    else:
        for i in range(n, 0, -1):
            fato *= i
        print(fato)


# Programa Principal
fatorial(9)
help(fatorial)
