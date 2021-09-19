from random import randint
números = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram {números}.')
nord = sorted(números)
print(f'O menor número é o {nord[0]} e o maior é o {nord[4]}.\n')
