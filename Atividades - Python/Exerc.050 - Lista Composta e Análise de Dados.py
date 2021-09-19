nomep = list()
dado = list()
maior = menor = 0
while True:
    nomep.append(str(input('Nome:')))
    nomep.append(float(input('Peso: ')))
    if len(dado) == 0:
        maior = menor = nomep[1]
    elif nomep[1] > maior:
        maior = nomep[1]
    elif nomep[1] < menor:
        menor = nomep[1]
    dado.append(nomep[:])
    nomep.clear()
    dec = str(input('Deseja continuar? [S/N] ')).strip()
    if dec in 'Nn':
        break
print(f'O número total de pessoas cadastradas foram {len(dado)}.')
print(f'O maior peso é {maior}KG e pertence a ', end='')
for d in dado:
    if d[1] == maior:
        print(f'[{d[0]}]', end=' ')
print(f'\nO menor peso é {menor}KG e pertece a', end=' ')        
for d in dado:
    if d[1] == menor:
        print(f'[{d[0]}]', end=' ')
