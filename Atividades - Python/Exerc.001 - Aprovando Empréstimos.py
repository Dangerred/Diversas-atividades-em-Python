print('=-='*25)
print('Vamos fazer uma simulação de quanto tempo você poderá pagar sua casa \ncom o valor dela, seu salário e o tempo, em anos, que deseja pagar.')
print('=-='*25)
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Em quantos anos você deseja pagar sua casa? '))
mensalidade = casa/(anos*12)
print('O total do valor da prestação é de  R${:.2f}.'.format(mensalidade))
b = (salario*0.3)
if mensalidade < b:
    print('Parabéns, seu empréstimo foi aprovado e você poderá dar prosseguimento a compra da sua casa!')
else:
    print('Infelizmente seu empréstimo não foi aprovado.\n')
