from utilidadesmod1 import moeda, dados

escolha = 'S'    
while escolha in 'Ss':
    preço = dados.leiadinheiro()
    moeda.resumo(preço, 20, 10)
    escolha = str(input('Deseja continuar realizando operações? [S/N]')).strip()[0]
    while escolha not in 'Nn' and escolha not in 'Ss':
        escolha = str(input('\033[0;31mInválido!\033[m Por favor escolha [S/N]: ')).strip()[0]
print('-'*32)
print('  VOLTE SEMPRE QUE PRECISAR!!!')
print('-'*32)     
