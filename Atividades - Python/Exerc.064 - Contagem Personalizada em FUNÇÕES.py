from time import sleep

def contador(i, f, p):
    if p == 0:
        print(f'Não há como realizar a progressão para uma passagem com valor {p}.')
    else:   
        print(f'Contagem de {i} até {f} de {p} em {p}:')
        if i < f:
            if p < 0:
                p = -p
            print('==='*10)
            for c in range(i, f, p):
                sleep(0.5)
                print(c, end=' ', flush=True)
            print(f'{f} FIM!')
        else:
            if p > 0:
                p = -p
            for c in range(i, f, p):
                sleep(0.5)
                print(c, end=' ', flush=True)
            print(f'{f} FIM!')
        print('==='*10)    
    

#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passagem: '))
print('==='*10)
contador(i, f, p)
