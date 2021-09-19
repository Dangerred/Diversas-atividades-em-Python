from random import randint
count = 0
escolhido = randint(0,10)
print('=-=-=-='*5,'JOGO DA ADIVINHAÇÃO','=-=-=-='*5)
print('\n')
print('O computador pensou em um número de 0 a 10. Será que você vai conseguir adivinhar qual o número escolhido?')
lista = int(input('Digite qual o número que o computador escolheu: '))
while lista != escolhido:
    if escolhido > lista:
        lista = int(input('Mais... Tente novamente: '))
    if escolhido < lista:
        lista = int(input('Menos... Tente novamente:'))
    count += 1
print('PARABÉNS! O número escolhido pelo computador foi o {}.\nForam necessárias {} tentativas para conseguir acertar.'.format(escolhido, count))
