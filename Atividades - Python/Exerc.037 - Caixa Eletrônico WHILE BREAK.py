saque = int(input('Usuário informe qual será o valor a ser sacado. R$'))
nota50 = nota20 = nota10 = nota1 = 0
while True:
    if saque >= 50:
        nota50 = saque // 50
        print(f'O total de notas de R$50 é de {nota50}.')
        saque = saque - nota50*50
    if saque < 50 and saque >= 20:
        nota20 = (saque % 50) // 20
        print(f'O total de notas de R$20 é de {nota20}.')
        saque = saque - nota20*20
    if saque < 20 and saque >= 10:
        nota10 = ((saque%50)%20) // 10
        print(f'O total de notas de R$10 é de {nota10}.')
        saque = saque - nota10*10
    if saque < 10 and saque >= 1:
        nota1 = ((saque%50)%20)%10
        print(f'O total de notas de R$1 é de {nota1}.')
    break
print('\nSaque efetuado com SUCESSO!')
