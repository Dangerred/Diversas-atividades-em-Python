from datetime import datetime
print('\nNeste programa vamos dizer se você está na idade obritória para alistamento militar.')
print('=-=-='*20)
sexo = str(input('Você é HOMEM ou MULHER? Digite H ou M. ')).upper()
if sexo == 'M':
    print('Não é necessário seu alistamento. O alistamento é obrigatório apenas para HOMENS.')
    quit()
if sexo == 'H':
    alist = int(input('Por favor, digite seu ano de nascimento: ')) 
    data = datetime.now()
    ano = int(data.strftime('%Y'))
    id = ano - alist
    print('\nSua idade é de {} anos.\n'.format(id))
if id > 18:
    print('Não é mais necessário seu alistamento militar, pois já passou do período. Você deveria ter se alistado há {} anos.\nSeu alistamento foi no ano de {}.'.format(id-18, ano-(id-18)))
elif id < 18 and id != 17:
    print('Ainda não está no período para seu alistamento. Faltam ainda {} anos para você se alistar.'.format(18-id))
elif id == 17:
    print('Seu alistamento está próximo e ocorrerá no ano em que fizer 18 anos.')
elif id == 18:
    print('Aliste-se IMEDIATAMENTE.')

