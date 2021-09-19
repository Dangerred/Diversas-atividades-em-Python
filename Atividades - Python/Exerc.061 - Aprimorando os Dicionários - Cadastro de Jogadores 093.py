jogadores = {}
gols = []
relatorio = []
total = 0
while True:
    jogadores['Nome'] = str(input('\nNome do jogador: ')).strip().title()
    jogadores['Partidas'] = int(input('Total de Partidas: '))
    for v in range(0, jogadores['Partidas']):
        gols.append(int(input(f'Gols na {v+1}ª partida: ')))
        jogadores['Gols'] = gols
        total = sum(gols)
    jogadores['Total'] = total
    gols = relatorio[:]
    relatorio.append(jogadores.copy())
    gols.clear()
    jogadores.clear()
    decisão = str(input('Deseja continuar cadastrando [S/N]? ')).upper()[0]
    while decisão != 'S' and decisão != 'N':
        decisão = str(input('Inválido! Deseja continuar cadastrando [S/N]? ')).upper()[0]
    if decisão in 'N':
        break
print()
print(f'{" Cod":<}{"   Nome":<24}{"Partidas":<12}{"      Gols":<24}{"Total":<12}')
print('----'*18)
for k, v in enumerate(relatorio):
    print(f'{k+1:^7}{v["Nome"]:<24}{v["Partidas"]:<10}{str(v["Gols"]):<25}{v["Total"]:<12}')
decisão = str(input('Deseja detalhar algum jogador? [S/N]')).upper()[0]
while decisão != 'S' and decisão != 'N':
    decisão = str(input('Inválido! Deseja detalhar algum jogador? [S/N] ')).upper()[0]
if decisão in 'S':
    while True:
        núm = int(input('Qual o código do jogador? (Digite 999 para encerrar) '))
        if núm == 999:
            break
        if núm > len(relatorio):
            print('Não existe jogador com esse código!')
        else:
            núm = núm-1
            print(f'\nLevantamento do jogador {relatorio[núm]["Nome"]}:')
            print('---'*20)
            for k, e in enumerate(relatorio[núm]['Gols']):
                print(f'    Na partida {k+1} fez {e} gols.')
            print('---'*20)
print()
print('RELATÓRIO  ENCERRADO')
print()
