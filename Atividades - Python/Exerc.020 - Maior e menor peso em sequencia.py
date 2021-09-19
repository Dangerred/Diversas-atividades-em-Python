maior = 0
menor = 0
for p in range(1, 6):
    print('Por favor digite o {}º'.format(p), end=' ')
    peso = float(input("peso: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior)
print(menor)
