import moeda   
    
preço = float(input('Digite o preço: R$'))
print(f'A metade do valor colocado é {moeda.moeda(moeda.metade(preço))}.')
print(f'O dobro do valor colocado é {moeda.moeda(moeda.dobro(preço))}.')
print(f'Esse valor aumentado em 10% resulta em {moeda.moeda(moeda.porcentagem(preço, 10))}.')
print(f'Esse valor reduzido em 12% resulta em {moeda.moeda(moeda.redução(preço, 12))}.\n')
