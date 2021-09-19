lista = []
cont = 0
while True:
    lista.append(int(input('Digite um número: ')))
    cont += 1       
    decisão = str(input('Deseja continuar digitando mais números? [S/N]')).strip().upper()[0]
    if decisão in 'Nn':
        break
lista.sort(reverse=True)
print(f'Os números da lista em ordem decrescente são {lista}.')
print(f'Foram digitados um total de {len(lista)} números.')
if 5 not in lista:
    print(f'Não foram digitados números 5 para essa lista.')
else:
    print(f'O total de vezes que o número 5 apareceu foram {lista.count(5)}.') 
