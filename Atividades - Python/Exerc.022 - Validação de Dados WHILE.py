sexo = str(input('Por favor, digite seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('Dados inválidos! Por favor, digite seu sexo (H/F): ')).strip().upper()[0]
if sexo == 'M':
    print('Seu sexo é Masculino.')
if sexo == 'F':
    print('Seu sexo é Feminino.')
