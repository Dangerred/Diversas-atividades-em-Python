n = decisao = 0
count = 1
num = int(input('Digite um número: '))
a = b = c = num
n += num
while decisao != 'N':
    decisao = str(input('Deseja continuar digitando mais números? (S/N)')).strip().upper()[0]
    if decisao == 'S' != int:
        num = int(input('Digite um número: '))
        n += num
        count += 1
    if count == 1:
        num = num
    else:
        if num > a:
            a = num
        if num < a:
            b = num
print('A média dos números digitados é {} e'.format(n/count))
print('o maior número é o {} e o menor é o {}.'.format(a, b))
