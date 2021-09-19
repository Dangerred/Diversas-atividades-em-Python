soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        print('Resultado parcial da soma apenas dos números pares: {}.'.format(soma))
print('O resultado final da soma é {}.'.format(soma))
