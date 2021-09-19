a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if a > b:
    print('O primeiro número digitado, {}, é MAIOR que o segundo, {}.'.format(a, b))
elif b > a:
    print('O segundo número digitado, {}, é MAIOR que o primeiro, {}.'.format(b, a))
else:
    print('Ambos os números digitados tem o mesmo valor, {}.'.format(a))
