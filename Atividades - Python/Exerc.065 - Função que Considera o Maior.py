from time import sleep

print()
def maior(*núm):
    maximo = 0
    print('Analisando os valores informados', end=' ')
    sleep(0.6)
    print('.', end = '', flush=True)
    sleep(0.6)
    print('.', end = '', flush=True)
    sleep(0.6)
    print('.', end = '', flush=True)
    print()
    print(f'Foram informados ao todo {len(núm)} números.')
    for m in núm:
        sleep(0.2)
        print(f'{m}', end=' ', flush = True)
        if m > maximo:
            maximo = m
    print(f'o maior valor entre os informados foi o {maximo}.')
    print('---'*20)
    print()

#Programa Principal#
maior(0, 4, 5, 2, 6, 8, 1)
maior(2, 3, 9, 0)
maior(8, 7, 1, 0, 4, 5)
maior()
