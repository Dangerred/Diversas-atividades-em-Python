cont = soma = 0
while True:
    num = int(input('Digite um número (para quando for 999): '))   
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de números digitados foram {cont} e o valor da sua soma é {soma}.')
