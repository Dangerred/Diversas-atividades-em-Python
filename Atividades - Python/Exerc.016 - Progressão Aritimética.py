count = 0
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desta PA: '))
a10 = a1 + (10 - 1)*r
for c in range(a1, a10+r, r):
    count += 1
    print('O {}° número da PA é o {}. '.format(count, c))
print('Acabou!')
