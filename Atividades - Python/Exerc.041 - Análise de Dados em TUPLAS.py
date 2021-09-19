tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), 
        int(input('Digite outro número para finalizar: ')))
nove = tupla.count(9)
print(f'\nO número 9 apareceu um total de {nove} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3)+1}ª posição.')
else:
    print(f'Não foi escrito nenhum número 3.')
print('Os números pares são: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end='  ')
