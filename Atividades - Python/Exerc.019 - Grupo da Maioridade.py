from datetime import datetime
counts = 0
countn = 0
for ano in range(0, 7):
    print('Em que ano a {}ª pessoa nasceu? '.format(ano+1), end=' ')
    a = int(input(''))
    if a > 9999 or a < 1900:
        a = int(input('Ano inválido. Por favor digite novamente o ano de nascimento: '))
        if int(datetime.today().strftime('%Y'))-a < 18:
            countn += 1
        else:
            counts += 1
    elif int(datetime.today().strftime('%Y'))-a < 18:
        countn += 1
    else:
        counts += 1
if counts == 0:
    print('\nNão existem pessoas com a idade superior a 18 anos.')
else:
    print('\nA quantidade de pessoas que são maiores de idade são {}.'.format(counts))
if countn == 0:
    print('\nNão existem pessoas com a idade inferior a 18 anos.')
else:
    print('\nA quantidade de pessoas que não são maiores de idade são {}.'.format(countn))
