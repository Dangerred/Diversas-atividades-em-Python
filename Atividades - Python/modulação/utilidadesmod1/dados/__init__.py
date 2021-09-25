def leiadinheiro():
    while True:
        preçov = input('\nDigite um valor: R$')
        if preçov.isascii() == True and preçov.isalnum() == False and preçov != ' '*len(preçov) and preçov.count(' ') == 0 or preçov.isnumeric() == True:
            if preçov.count(',') == 1 and preçov.count('.') == 0 or preçov.count('.') == 1 and preçov.count(',') == 0: 
                return float(preçov.replace(',','.'))
            elif preçov.count('.') > 1 or preçov.count(',') > 1:
                print(f"ERRO! O termo digitado '{preçov}' não é um termo válido!")
            else:
                return float(preçov)
        else:
            print(f"\033[1;31mERRO! O termo digitado '{preçov}' não é um termo válido!\033[m")
