from random import randint
from time import sleep
lista = []

print()
def sorteio():
    for sort in range(0, 5):
        núm = randint(0, 10)
        if sort == 0:
            lista.append(núm)
        else: 
            while lista.count(núm) != 0:
                núm = randint(0, 9)
            lista.append(núm)
    print('Sorteando 5 números da lista: ', end='')
    for i in lista:
        sleep(0.3)
        print(i, end=' ', flush=True)
    print('PRONTO!')

def somapar():
    par = 0
    print('Os números pares da lista são: ', end='')
    for p in lista:
        if p%2 == 0:
            print(p, end=' ')
            par += p
    print(f'\nA soma dos números pares totalizam {par}.')
    print()


sorteio()
somapar()
