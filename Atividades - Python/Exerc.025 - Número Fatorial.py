n = 0
f = 1
s = 0
fatorial = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}!'.format(fatorial), end= ' = ')
while n != fatorial:
    n += 1
    f = n*f 
    if n < fatorial:
        s = fatorial/fatorial+s
        print(s, end=' x ')
    else:
        s = fatorial/fatorial+s
        print(s)
print('O resultado é igual a {}.'.format(f))
