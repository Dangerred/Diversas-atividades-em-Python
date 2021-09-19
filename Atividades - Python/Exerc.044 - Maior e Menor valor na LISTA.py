lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um número para a posição {c+1}: ')))
print(f'O maior número da lista foi o {max(lista)} e apareceu nas posições ', end='')
for pos, valores in enumerate(lista):
    if valores == max(lista):
        print(f'{pos+1}...', end=' ')
print(f'\nO menor número da lista foi o {min(lista)} e apareceu nas posições ', end='')
for pos, valores in enumerate(lista):
    if valores == min(lista):
        print(f'{pos+1}...', end=' ')
