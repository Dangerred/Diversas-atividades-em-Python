count = 0
num = int(input('Digite um número: '))
print('Este número é divisível por:')
for c in range(1, num+1):
    if num % c == 0:
        count += 1
        print(c, end=' ')
print('\nA quantidade de divisores deste número são {}.'.format(count))
if count == 2:
    print('Este número é PRIMO.')   
else:
    print('Não é PRIMO.')      
               