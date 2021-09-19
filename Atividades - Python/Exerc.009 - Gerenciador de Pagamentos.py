print('Escolha sua opção de pagamento listada abaixo')
print("1 - Pagamento a vista em dinheiro com 10% de desconto")
print("2 - Pagamento a vista com 5% de desconto")
print("3 - Pagamento parcelado em 2x com preço normal.")
print("4 - Pagamento parcelado em 3x ou mais com juros de 20%")
op = int(input('Digite a opção que deseja realizar seu pagamento: '))
preço = float(input('Qual é o preço do produto? R$'))
dinheiro = 1
cartão = 2
cartão1 = 3
cartão2 = 4
if op == dinheiro:
    print('Seu pagamento receberá um desconto de 10 % no a vista e será um total de R${:.2f}.'.format(preço*0.9))
elif op == cartão:
    print('Seu pagamento receberá 5% no pagamento a vista do cartão de crédito e será um total de R${:.2f}'.format(preço*0.95))
elif op == cartão1:
    print('Seu pagamento não terá desconto e será dividido em 2x sem juros sendo um total de R${:.2f} e parcelas de R${:.2f} cada.'.format(preço, preço/2))
else:
    print('Seu pagamento será parcelado e por ser acima de 2x terá juros de 20%.')
