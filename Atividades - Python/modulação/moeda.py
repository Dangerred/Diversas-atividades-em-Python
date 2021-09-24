def metade(num):
    valor = num/2
    return valor

def dobro(num):
    valor = 2*num
    return valor

def porcentagem(num, p):
    valor = (p+100)/100*num
    return valor

def redução(num, p):
    valor = (100-p)/100*num
    return valor

def moeda(valor):
    return f'R${valor:.2f}'.replace('.',',')
