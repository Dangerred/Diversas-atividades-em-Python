num = count = 0
while not num < 0:
    num = int(input('\nDigite um número para saber sua tabuada. Caso queira encerrar, digite um número negativo. '))
    if num < 0:
        break
    for count in range(1,11):
        print(f'{num} x {count} = {num*count}')
print('=-=-=-='*15)
print('Programa tabuada ENCERRADO!')
