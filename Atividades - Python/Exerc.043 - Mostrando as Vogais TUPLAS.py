palavras = ('Carro', 'Celular', 'Programacao', 'Video', 'Papel', 'Filme',
            'Cascata', 'Carne', 'Fruta', 'Cama', 'Numero', 'Gravata', 'Dinheiro')
for c in range(0, len(palavras)):
    print(f'{palavras[c]} tem as vogais:', end=' ')
    for letra in range(0, len(palavras[c])):
        if palavras[c][letra].lower() in 'aeiou':
            print(f'{palavras[c][letra]}', end=' ')
    print('\n')
