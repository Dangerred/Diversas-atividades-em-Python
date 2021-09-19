lista = []
cont = 0
for c in range(0, 5):
    núm = int(input('Digite um número: '))
    if cont == 0:
        lista.append(núm)
        print('Adicionado ao final da lista.')
        cont += 1
    elif cont == 1:
        if núm > max(lista):
            lista.append(núm)
            print('Adicionado ao final da lista.')
        elif núm < min(lista):
            lista.insert(0, núm)
            print('Adicionao na posição 0 da lista.')
        elif min(lista) < núm < max(lista):
            for pos, c in enumerate(lista):
                if min(lista) < núm < c:
                    lista.insert(pos, núm)
                    print(f'Adicionado na posição {pos} da lista.')
                    break
                elif max(lista) < núm < c:
                    lista.insert(pos, núm)
                    print(f'Adicionado na posição {pos} da lista.')
                    break
print(lista)
