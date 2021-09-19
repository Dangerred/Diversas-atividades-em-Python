print('\n')
print('=='*13, 'LISTA DE PREÇOS','=='*13)
print('\n')
listagem = ('Processador AMD R7 5800X', 2600.00, 'Sapphire NITRO+ RX 6800XT', 9000.00, 
            'Placa Mãe MSI Tomahawk', 1399.97, 'SSD 1TB', 750.00)
list = len(listagem[0])
for c in range(0, len(listagem)):
    if type(listagem[c]) == str:
        print('{:.<57}R$'.format(listagem[c]), end='')
    else:
        print(f'{listagem[c]:>9.2f}')
print('\n')
