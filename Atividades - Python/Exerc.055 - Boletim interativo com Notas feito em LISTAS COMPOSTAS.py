boletim = []
alunos = []
média = escolha = 0
print()
print('=-='*8, ' BOLETIM INTERATIVO ', '=-='*8)
while True:
    alunos.append(str(input('\nDigite o nome do aluno: ')))
    for n in range(0, 2):
        alunos.append(float(input(f'Digite a nota {n+1} do aluno: ')))
        if n == 1:
            média = (alunos[1]+alunos[2])/2
            alunos.append(média)
    boletim.append(alunos[:])
    alunos.clear()
    decisão = str(input('Deseja continuar digitando? [S/N] ')).strip()[0]
    if decisão in 'Nn':
        break
print('\n Número          Nome            Média\n','=-='*13)
for pos, l in enumerate(boletim):
    print(f'{pos+1:^7}      {l[0]:<20}   ', end =' ')
    print(f'{l[3]:^8}')
print()
escolha = str(input('Deseja ver as notas de algum aluno? [S/N]'))
if escolha in 'Ss':
    while True:
        escolha = 0
        escolha = int(input('Digite o número do aluno o qual deseja ver: (Digite 999 para cancelar) '))
        if escolha == 999:
            break
        print(f'O nome do aluno é {boletim[escolha-1][0]} e suas notas são {boletim[escolha-1][1]} e {boletim[escolha-1][2]}.\n')
print()
print('=-='*6, ' BOLETIM INTERATIVO FECHADO ', '=-='*6, '\n')        