produto = preço = decisão = total = cont = cont1 = barato = custo = 0
menor = 'S'
print('-------------------- Lista de Produtos ---------------------\n')
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Qual o preço deste produto? R$'))
    total += preço
    cont1 += 1
    if preço > 1000:
        cont += 1
    if cont1 == 1:
        barato = preço
    if preço <= barato:
        barato = preço
        menor = produto
        custo = preço
    decisão = str(input('Você deseja continuar com a lista? [S/N] ')).strip().upper()[0]
    if decisão == 'N':
        break
print('--------------------- FIM DO PROGRAMA ---------------------\n')
print(f'O produto mais barato é o/a {menor}, custando R${custo}.')
print(f'O total gasto nas compras foi R${total:.2f}')
print(f'A quantidade de produtos com valor superior a R$1000,00 são {cont}.')
