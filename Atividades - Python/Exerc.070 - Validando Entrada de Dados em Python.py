def leiaInt(n):
    if n.isnumeric():
        return f'O número digitado foi o {n}.'
    else:
        while n != n.isnumeric():
            print('\033[01:31mErro! Digite um número inteiro válido.\033[m')
            n = input('Digite um número: ')
            if n.isnumeric():
                return f'O número digitado foi o {n}.'
                break

n = input('Digite um número: ')
print(leiaInt(n))
print()
