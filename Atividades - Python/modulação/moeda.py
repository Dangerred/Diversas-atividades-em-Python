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
    print(f'A metade do valor colocado é {metade(preço)}.')
    print(f'O dobro do valor colocado é {dobro(preço)}.')
    print(f'Esse valor aumentado em {a}% resulta em {porcentagem(preço, a)}.')
    print(f'Esse valor reduzido em {b}% resulta em {redução(preço, b)}.')
