from datetime import date
print()
registro = {'Nome': ' ', 'Ano': ' ', 'Carteira': ' '}
registro['Nome'] = str(input('Digite o nome da pessoa: ')).strip().title()
registro['Ano'] = int(input('Digite o ano de nascimento: '))
idade = date.today().year - registro['Ano']
registro['Carteira'] = int(input('Digite a carteira de trabalho: '))
if registro['Carteira'] != 0:
    registro['Contratação'] = int(input('Ano de contratação: '))
    registro['Salário'] = int(input('Salário: R$'))
    print()
    print(f'O nome é {registro["Nome"]}.')
    print(f'A idade é {idade}.')
    print(f'A CTPS tem valor {registro["Carteira"]}.')
    print(f'O salário é R${registro["Salário"]}.')
    aposentadoria = 65 - idade
    if aposentadoria >= 30:
        print(f'A idade de aposentadoria será {idade+30} anos.')
        print()
    else:
        print(f'A idade de aposentadoria será de 65 anos.')
        print()
else:
    print(f'O nome é {registro["Nome"]}.')
    print(f'A idade é {idade}.')
    print(f'A pessoa não possui carteira de trabalho, sendo este com valor {registro["Carteira"]}.')
    print()
