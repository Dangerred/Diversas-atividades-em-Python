lista = []
listap = []
listai = []
while True:
    número = int(input('Digite um número: '))
    lista.append(número)
    if número % 2 == 0 or número == 0:
        listap.append(número)
    else:
        listai.append(número)
    decisão = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if decisão in 'N':
        break
print(f'A lista é composta pelos seguintes números: {lista}.')
print(f'A lista dos números pares é: {listap}.')
print(f'A lista dos números ímpares é: {listai}.')
