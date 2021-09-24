def metade(num, c=True):
    valor = num/2
    if c == True:
        return moeda(valor)
    else:
        return valor

def dobro(num, c=True):
    valor = 2*num
    if c == True:
        return moeda(valor)
    else:
        return valor
    
def porcentagem(num, p, c=True):
    valor = (p+100)/100*num
    if c == True:
        return moeda(valor)
    else:
        return valor

def redução(num, p, c=True):
    valor = (100-p)/100*num
    if c == True:
        return moeda(valor)
    else:
        return valor

def moeda(valor):
    return f'R${valor:>.2f}'.replace('.',',')

def resumo(preço, a, b):
    print('='*44)
    print('RESUMO DOS PREÇOS'.center(44))
    print('='*44)
    print(f'Valor da metade: \t\t{metade(preço)}')
    print(f'Valor do dobro:  \t\t{dobro(preço)}')
    print(f'Aumenta em {a}%:  \t\t{porcentagem(preço, a)}')
    print(f'Reduz em {b}%:   \t\t{redução(preço, b)}')
    print('='*44)
    print()
