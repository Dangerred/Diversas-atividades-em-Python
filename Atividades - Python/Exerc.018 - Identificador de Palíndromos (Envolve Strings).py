inverso = ''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
tam = len(junto)
for c in range(tam-1 , - 1, -1):
    inverso += junto[c]
if inverso == junto:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')
    