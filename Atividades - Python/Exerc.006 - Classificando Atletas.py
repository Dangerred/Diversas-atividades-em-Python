idade = int(input('Qual a idade do aluno para que possamos direcionar a devida categoria: '))
if idade <= 9:
    print('A categoria desse aluno é a MIRIM.')
elif idade > 9 and idade <= 14:
    print('A categoria desse aluno é a INFANTIL.')
elif idade > 14 and idade <= 19:
    print('A categoria desse aluno é a JÚNIOR.')
elif idade <= 25:
    print('A categoria desse aluno é a SÊNIOR.')
else:
    print('A categoria deste aluno é a MASTER.')
