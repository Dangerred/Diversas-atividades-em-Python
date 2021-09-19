matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac3 = p = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite os números para compor a matriz na posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
for l in range(0, 3):
    if matriz[l][2] >= 0:
        somac3 += matriz[l][2]
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if matriz[1][c] >= p:
            p = matriz[1][c]
print()
print(f'A somatória de TODOS os números pares desta matriz vale {somap}.')
print(f'A soma dos valores da terceira coluna da matriz vale {somac3}.')
print(f'O maior número da segunda linha da matriz é {p}.')
