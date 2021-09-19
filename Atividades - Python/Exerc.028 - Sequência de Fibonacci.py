t1 = 0
t2 = 1
fibo = int(input('Digite um número: '))
print('{}, {}, '.format(t1, t2), end='')
count = 0
while count < fibo:
    t3 = t1 + t2
    print('{},'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    count += 1
print('FIM')
