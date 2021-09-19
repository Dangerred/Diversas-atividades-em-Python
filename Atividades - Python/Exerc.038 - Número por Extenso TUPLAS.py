contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cindo',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
           'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 
           'dezoito', 'dezenove', 'vinte')
número = -1
while número < 0 or número > 20:
    número = int(input('Digite um número de 0 a 20: '))
    if número >= 0 and número <= 20:
        break
    else:
        print('Tente novamente!', end=' ')
print(f'O número digitado foi o {contagem[número]}.')
