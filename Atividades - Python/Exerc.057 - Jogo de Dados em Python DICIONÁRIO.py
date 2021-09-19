from random import randint
from time import sleep
from operator import itemgetter
cont = 1
dados = {'Jogador 1': '', 'Jogador 2': '', 'Jogador 3': '', 'Jogador 4': ''}
ordem = dict()
print()
for d in range(0, 4):
    sorteio = randint(1, 6)
    sleep(1)
    dados[f'Jogador {d+1}'] = sorteio
    print(f'O jogador {d+1} tirou {sorteio}.') 
ordem = sorted(dados.items(), key=itemgetter(1), reverse=True)
print()
print(f'{"=-=-=-=-==-=-=-=-=-=":<0}{"  RANKING  ":<0}{"=-==-=-=-=-==-=-=-=-=":<0}')
print()
for k, v in ordem:
        print(f'{cont}º - O {k} tirou o valor no dado de número {v}.')
        cont += 1
        sleep(1)
print()
