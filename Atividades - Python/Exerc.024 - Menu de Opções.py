print('=-=-=-=-=-=-=-=-= Menu Operacional =-=-=-=-=-=-=-=-=')
num1 = float(input('Digite o número: '))
num2 = float(input('Digite outro número: '))
print("""Escolha qual dentre as opções abaixo será a sua opção para realização da operação:\n
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Maior Dentre os Números
[5] Novos números
[6] Sair do Menu de Opções\n""")
escolha = int(input('Escolha sua opção: '))
while escolha != 6:
    if escolha == 1:
        print('A soma entre {} e {} é {}.'.format(num1, num2, num1+num2))
        escolha = str(input('Deseja realizar mais alguma operação? (S/N) ')).strip().upper()[0]
        if escolha == 'S':
            escolha = int(input('Escolha a sua opção: '))
        else:
            escolha = 6
    if escolha == 2:
        print('A subtração entre {} e {} é {}.'.format(num1, num2, num1-num2))
        escolha = str(input('Deseja realizar outra operação? (S/N) ')).strip().upper()[0]
        if escolha == 'S':
            escolha = int(input('Escolha a opção: '))
        else:
            escolha = 6
    if escolha == 3:
        print('A multiplicação entre {} e {} é {}.'.format(num1, num2, num1*num2))
        escolha = str(input('Deseja realizar outra operação? (S/N) ')).strip().upper()[0]
        if escolha == 'S':
            escolha = int(input('Escolha a opção: '))
        else:
            escolha = 6
    if escolha == 4:
        if num1 > num2:
            print('O número {} é maior que o número {}.'.format(num1, num2))
        else:
            print('O número {} é maior que o número {}.'.format(num2, num1))
        escolha = str(input('Deseja realizar outra operação? (S/N) ')).strip().upper()[0]
        if escolha == 'S':
            escolha = int(input('Escolha a opção: '))
        else:
            escolha = 6
    if escolha == 5:
        print('Você deve escolher outros números.')
        num1 = float(input('Digite o número: '))
        num2 = float(input('Digite outro número: '))
        escolha = int(input('Escolha a opção: '))
print('\n=-=-=-=-=-=-= Menu de opções Finalizado. =-=-=-=-=-=-=')