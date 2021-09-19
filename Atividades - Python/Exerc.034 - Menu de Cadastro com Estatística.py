sexo = cont = cont2 = cont3 = cont4 = idade = 0
decisão = ' '
while True:
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        idade = int(input('Digite sua idade: '))
        if idade > 18:
            cont += 1
        if sexo == 'M':
            cont2 += 1
        if sexo == 'F' and idade < 20:
            cont3 += 1
        cont4 += 1
        while decisão not in 'SN':
            decisão = str(input('Deseja continuar cadastrando mais pessoas? [S/N] ')).strip().upper()[0]
        if decisão == 'N':
            break
print(f'\nForam cadastrados um total de {cont4} pessoas.\n\nA quantidade de pessoas com mais de 18 anos são {cont}.\nA quantidade de homens cadastrados são {cont2}.\nO total de mulheres com idade inferior a 20 anos são {cont3}.\n')
