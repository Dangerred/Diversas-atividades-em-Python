jogador = dict()
gols = []
print()
jogador['Nome'] = str(input('Qual é o jogador? ')).strip().title()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} fez? '))
for v in range(0, jogador['Partidas']):
    gols.append(int(input(f'Quantos gols foram feitos no jogo {v+1}? ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('=-='*20)
del jogador['Partidas']
print(jogador)
print('=-='*20)
for k, v in jogador.items():
    print(f'O item {k} tem valor {v}.')
print('=-='*20)
print(f'O jogador {jogador["Nome"]} realizou {len(gols)} partidas.')
for k, v in enumerate(gols):
    print(' '*5, end='')
    print(f'=> Na partida {k+1} fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')
print()
    