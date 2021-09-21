def fatorial(a, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou nao a conta.
    :return: O valor do fatorial de um número N.
    """
    c = 1
    for i in range(a, 0, -1):
        if show:
            if i != 1:
                print(i, end=' * ')
            else:
                print(i, end=' = ')
        c *= i
    return f'{c}'

    
print(fatorial(6, False))
