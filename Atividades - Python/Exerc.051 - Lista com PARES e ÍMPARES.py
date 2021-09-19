listat = [[],[]]
for c in range(1, 8):
    núm = int(input(f'Digite o {c}º número: '))
    if núm % 2 == 0:
        listat[0].append(núm)
    else:
        listat[1].append(núm)
listat[0].sort()
listat[1].sort()
print(f'\nOs números pares dessa lista são {listat[0]}.')
print(f'Os números ímpares dessa lista são {listat[1]}.')
