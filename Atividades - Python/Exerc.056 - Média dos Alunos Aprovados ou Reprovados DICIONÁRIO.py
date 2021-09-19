média = {'Nome': ' ', 'Média': ' ', 'Situação': ' '}
print()
média['Nome'] = str(input('Digite o nome do aluno: ')).strip().title()
média['Média'] = float(input('Digite a média desse aluno: '))
print()
if 5 <= média['Média'] < 7:
    média['Situação'] = 'Recuperação'
elif média['Média'] < 5:
    média['Situação'] = 'Reprovado'
else:
    média['Situação'] = 'Aprovado'
print(f'O nome do aluno é {média["Nome"]}.')
print(f'Sua média é {média["Média"]}.')
print(f'E sua situação atual é {média["Situação"]}.')
