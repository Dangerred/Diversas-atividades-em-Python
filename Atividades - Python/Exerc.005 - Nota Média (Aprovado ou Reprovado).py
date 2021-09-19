n1 = float(input('Por favor, digite a nota da sua primeira prova: '))
n2 = float(input('Agora, a nota da sua segunda prova: '))
nt = (n1 + n2)/2
if nt > 6.9:
    print('Parabéns sua nota geral é {}, acima da média. Você está aprovado!'.format(nt))
elif nt > 5 and nt < 6.9:
    print('Caro aluno, sua nota geral é {} e portanto você está na recuperação!'.format(nt))
else:
    print('Sua nota é {} e portanto você foi reprovado!'.format(nt))
     