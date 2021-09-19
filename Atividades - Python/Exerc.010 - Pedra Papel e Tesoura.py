from random import choice
print('Vamos jogar Pedra, Papel ou Tesoura?')
jg = str(input('Escolha sua mão: ')).strip()
jg = jg.lower()
lista = ['pedra', 'papel', 'tesoura']
cpu = choice(lista)
print('O computador escolheu {}.'.format(cpu))
if cpu == jg:
    print('Empate')
elif cpu == 'pedra' and jg == 'tesoura':
    print('Vitória cpu.')
elif cpu == 'pedra' and jg == 'papel':
    print('Vitória jogador.')
elif cpu == 'papel' and jg == 'tesoura':
    print('Vitória jogador.')
elif cpu == 'papel' and jg == 'pedra':
    print('Vitória cpu.')
elif cpu == 'tesoura' and jg == 'papel':
    print('Vitória cpu.')
elif cpu == 'tesoura' and jg == 'pedra':
    print('Vitória jogador.')
