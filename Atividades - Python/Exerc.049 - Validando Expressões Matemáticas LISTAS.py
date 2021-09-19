expressão = []
cont = cont1 = 0
mat = str(input('Digite uma expressão númerica para ser avaliada. '))
for pos, c in enumerate(mat):
        if c == '(':
            cont += 1
        elif c == ')':
            cont1 += 1
expressão.append(mat)
if cont == cont1:
    print('A expressão é válida.')
else:
    print('A expressão é inválida!')
