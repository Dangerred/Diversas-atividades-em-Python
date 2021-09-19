saque = int(input('Qual valor deseja sacar? R$'))
total = saque
ced = 50
tot = 0
while True:
    if saque >= 50:
        total -= 50
        saque = total
        tot += 1
        print(f'Nota {tot}.')
    elif saque >= 20:
            total -= 20
            saque = total
            tot += 1
    elif saque < 20 and saque >= 10:        
        total -= 10
        saque = total
        tot += 1
    break
