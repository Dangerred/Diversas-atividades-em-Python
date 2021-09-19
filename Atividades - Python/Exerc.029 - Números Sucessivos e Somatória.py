nb = count = num = 0
nb = int(input('Digite um número: '))
while nb != 999:
    num += nb
    count += 1
    nb = int(input('Digite um número: '))
print('O resultado final da somatória de números é {} e foram digitados {} números diferentes.'.format(num, count))
