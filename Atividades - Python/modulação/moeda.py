def metade(num, c=False):
    valor = num/2
    if c == True:
        return moeda(valor)
    else:
        return valor

def dobro(num, c=False):
    valor = 2*num
    if c == True:
        return moeda(valor)
    else:
        return valor
    
def porcentagem(num, p, c=False):
    valor = (p+100)/100*num
    if c == True:
        return moeda(valor)
    else:
        return valor

def redução(num, p, c=False):
    valor = (100-p)/100*num
    if c == True:
        return moeda(valor)
    else:
        return valor

def moeda(valor):
    return f'R${valor:>.2f}'.replace('.',',')
