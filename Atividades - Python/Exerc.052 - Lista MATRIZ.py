m1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        m1[l][c] = int(input(f'Digite um número para compor nossa matriz na posição [{l},{c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m1[l][c]:^7}]', end='')
    print()
