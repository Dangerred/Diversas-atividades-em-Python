an = 1
count = 1
qntd = 1
b = 0
decisao = 'S'
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite qual a razão da PA: '))
print('Os 10 primeiro termos dessa PA com o primeiro termo {} e a razão {} são: '.format(a1, r))
a10 = a1 + (an - 1)*r
print(a10, end=', ')
an += 1
while an != 0 and qntd != 0:
    a10 = a1 + (an - 1)*r
    print(a10, end='')
    print(', ' if an != 0 else '', end='')   
    an += 1
    count += 1
    if an == 11 and an != qntd+b:
        decisao = str(input('Deseja que sejam mostrados mais alguns termos da PA? (S/N)')).strip().upper()[0]
        if decisao == 'S':
            qntd = int(input('Quantos termos deseja que sejam mostrados? '))
            b = an
        elif decisao == 'N':
            an = 0
            qntd = 0
    if an == qntd+b:
        decisao = str(input('Deseja que sejam mostrados mais alguns termos da PA? (S/N)')).strip().upper()[0]
        if decisao == 'S':
            qntd = int(input('Quantos termos deseja que sejam mostrados a mais? '))
            b = an
        elif decisao == 'N':
            an = 0
            qntd = 0
print('\nA quantidade total de termos mostradas para esta PA foi de {}.'.format(count))

