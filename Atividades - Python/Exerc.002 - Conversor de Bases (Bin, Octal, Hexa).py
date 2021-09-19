numero = int(input('Digite um número: '))
conversor = int(input('Escolha qual será a opção de conversão do seu número, sendo: \n1 - Binário \n2 - Octal \n3 - Hexadecimal \n'))
if conversor == 1:
    print('O número em binário é {}.'.format(bin(numero)[2:]))
elif conversor == 2:
    print('O número em Octal é {}.'.format(oct(numero)[2:]))
else:
    print('O número em Hexadecimal é {}.'.format(str.upper(hex(numero)[2:])))
