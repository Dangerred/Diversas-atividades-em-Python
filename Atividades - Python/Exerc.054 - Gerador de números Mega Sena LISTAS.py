from random import randint
from time import sleep
print('=-='*8, ' GERADOR DE JOGOS PARA A MEGA SENA ', '=-='*8, '\n')
sena = []
quantidade = int(input('Quantos jogos você deseja criar? '))
print()
for tot in range(0, quantidade):
    for s in range(0, 6):
        sena.append(randint(1, 60))
        s += 1
    for pos, g in enumerate(sena):
        if sena.count(g) != 1:
            sena[pos] = randint(1, 60)
            pos = -1
    sena.sort()      
    sleep(1)  
    print(f'Jogo {tot+1}: {sena}')
    sena.clear()
    tot += 1
print()
