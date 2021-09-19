midade = 0
idhma = 0
idfme = 0
count = 0
for p in range(1, 5):
    print('============== {}ª Pessoa =============='.format(p))
    nome = str(input('Digite seu nome completo: ')).upper().strip()
    id = int(input('Digite a sua idade: ').format(p))
    sexo = str(input('Qual seu sexo? (M/F) ')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo inválido! Por favor, digite seu sexo novamente: ')).upper().strip()
    #Identificando qual o homem mais VELHO
    if sexo == 'M' and p == 1:
        idhma = id
        h = nome
    if sexo == 'M' and id > idhma:
        idhma = id
        h = nome
    #OUTRA FORMA DE FAZER A IDENTIFICAÇÃO DO HOMEM MAIS VELHO USANDO CONTADOR
    #if sexo == 'MASCULINO' and count == 0:
     #   idhma = id
      #  idhme = id
      #  count += 1
      #  h = nome
    #else:
    #    if sexo == 'MASCULINO' and id > idhma:
    #        idhma = id
    #        h = nome
    #Identificando quantas mulheres tem idade abaixo dos 20 anos
    if sexo == 'F':
        if id < 20:
            idfme += 1
    #Média de IDADE do GRUPO
    midade += id
print('A média de idade de todos do grupo é {} anos.'.format(midade/4))
print('O nome do homem mais velho é {} e sua idade é {}.'.format(h.title(), idhma))
print('A quantidade de mulheres com idade abaixo dos 20 anos é {}.'.format(idfme))
