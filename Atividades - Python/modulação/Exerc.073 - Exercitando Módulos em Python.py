import moeda   
    
preço = float(input('Digite o preço: R$'))
print(f'A metade do valor colocado é {moeda.metade(preço, True)}.')
print(f'O dobro do valor colocado é {moeda.dobro(preço, True)}.')
print(f'Esse valor aumentado em 10% resulta em {moeda.porcentagem(preço, 10, True)}.')
print(f'Esse valor reduzido em 12% resulta em {moeda.redução(preço, 12, True)}.\n')
