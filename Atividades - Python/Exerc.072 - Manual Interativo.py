from time import sleep

c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - Vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'   , # 6 - branco
)

def fim(ate, cor=0):
    print(c[1])
    print(ate)
    print(c[1])
    
def var(msg):
    a = f'Acessando o manual referente a função: {ajuda}'
    tam = len(a) + 4
    print(c[5], '~'*tam)
    print(c[5], f'  {a}')
    print(c[5], '~'*tam)
    sleep(2)
    help(msg)
    print(c[0], end='')


def título(tit, cor=0):
    print(c[cor], '~~~~'*15)
    print(c[4], tit)
    print(c[cor], '~~~~'*15)
    sleep(2)
    print(c[0], end='')


#Programa Principal
while True:
    título('             Acessando o manual de comando', 4)
    ajuda = str(input('Qual função ou biblioteca você deseja ajuda? ')).strip()
    if ajuda.upper() == 'FIM':
        break
    else:
        var(ajuda)
fim('VOLTE SEMPRE QUE PRECISAR!')
