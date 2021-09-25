def metade(num, c=True):
    """
    Estas funções visam calcular várias questões monetárias solicitadas.
    :param num: recebe o número digitado pelo usuário
    :param c: habilitará ou não a formatação para o texto monetário
    :return: retorna o valor encontrado. Nota-se que em caso do param c for True, esse retorno levará a função moeda()

    Importante dizer que a função dobro funciona de maneira similar a esta.
    """
    valor = num / 2
    if c == True:
        return moeda(valor)
    else:
        return valor


def dobro(num, c=True):
    valor = 2 * num
    if c == True:
        return moeda(valor)
    else:
        return valor


def porcentagem(num, p, c=True):
    valor = (p + 100) / 100 * num
    if c == True:
        return moeda(valor)
    else:
        return valor


def redução(num, p, c=True):
    valor = (100 - p) / 100 * num
    if c == True:
        return moeda(valor)
    else:
        return valor


def moeda(valor):
    return f'R${valor:>.2f}'.replace('.', ',')


def resumo(preço, a, b):
    print('=' * 44)
    print('RESUMO DOS PREÇOS'.center(44))
    print('=' * 44)
    print(f'Valor da metade: \t\t{metade(preço)}')
    print(f'Valor do dobro:  \t\t{dobro(preço)}')
    print(f'Aumenta em {a}%:  \t\t{porcentagem(preço, a)}')
    print(f'Reduz em {b}%:   \t\t{redução(preço, b)}')
    print('=' * 44)
    print()
