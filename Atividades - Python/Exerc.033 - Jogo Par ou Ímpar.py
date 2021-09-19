from random import randint
import time
número = cpu = cont = pi = 0
print('\n=-=-=-=-=-=-=-=-=-= || Bem vindo ao jogo Par ou Ímpar || =-=-=-=-=-=-=-=-=-=\n')
while True:
    número = int(input('Escolha qual número você vai jogar: '))
    pi = str(input('Escolha PAR ou ÍMPAR (P/I): ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Escolha PAR ou ÍMPAR (P/I): ')).strip().upper()[0]
    print('O computador está escolhendo seu número....')
    time.sleep(2)
    cpu = randint(0, 11)
    print(f'O computador escolheu o número {cpu}.\n')
    time.sleep(1)
    resultado = (número + cpu) % 2
    if resultado == 0 and pi == 'P':
        print(f'PARABÉNS! Você venceu! A soma dos números escolhidos deu {número+cpu} e este número é PAR.\n')
        cont += 1
    if resultado == 0 and pi == 'I':
        print(f'Infelizmente você perdeu! A soma dos números escolhidos deu {número+cpu} e este número é PAR.\n')
        break
    if resultado != 0 and pi == 'I':
        print(f'PARABÉNS! Você venceu! A soma dos números escolhidos deu {número+cpu} e este número é ÍMPAR.\n')
        cont += 1
    if resultado != 0 and pi == 'P':
        print(f'Infelizmente você perdeu! A soma dos números escolhidos deu {número+cpu} e este número é ÍMPAR.\n')
        break
print(f'Jogo encerrado! Esse foi seu total de vitórias: {cont}.\n')

