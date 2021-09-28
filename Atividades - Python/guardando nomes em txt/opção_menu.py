import colorpy, time

def menu(listados):
    c = 1
    print('-'*50)
    print(' '*17, 'MENU PRINCIPAL')
    print('-'*50)
    for i in range(0, 3):
        print(colorpy.cores[2], c, '-', colorpy.cores[3], listados[i], colorpy.cores[5])
        c+=1
    print('-'*50)
        

def list(valor):
    while True:
        try:
            op = int(input(valor))
            if op == 1:
                print('-'*50)
                print(' '*20, 'OPÇÃO 1')
                print('-'*50)
            elif op == 2:
                print('-'*50)
                print(' '*20, 'OPÇÃO 2')
                print('-'*50)
            elif op == 3:
                print('Saindo...')
                time.sleep(1.5)
                print('Volte Sempre!')
                break
            elif op > 3:
                print('Não existe essa opção, por favor, digite uma opção válida.')
        except (ValueError, TypeError):
            print(f'{colorpy.cores[0]}','Erro! O valor não corresponde a uma opção válida.',f'{colorpy.cores[5]}')
        except (KeyboardInterrupt):
            print(f'{colorpy.cores[0]}', 'O usuário decidiu encerrar o programa.', f'{colorpy.cores[5]}')
            return 0
