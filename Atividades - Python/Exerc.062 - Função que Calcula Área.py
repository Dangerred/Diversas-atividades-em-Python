def area(mensagem):
    print()
    print(mensagem)
    print('---'*15)
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    a = c * l
    print(f'A área do terreno de {l} x {c} em metros fica {a}m².')

def espaço():
    print()


area('            Controle de Terrenos')
espaço()