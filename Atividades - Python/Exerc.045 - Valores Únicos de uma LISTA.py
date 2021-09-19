lista = []
while True:
    número = (int(input('Digite um número: ')))
    lista.append(número)
    decisão = str(input('Deseja continuar? [S/N]')).strip().upper()[0]  
    if decisão in 'Nn':
        for pos, c in enumerate(lista):
            if lista.count(c) != 1:
                del lista[pos]
        break
lista.sort()
print(lista)
