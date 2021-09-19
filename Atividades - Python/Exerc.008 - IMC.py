alt = float(input('Por favor digite sua altura em METROS: '))
peso = float(input('Por favor digite o seu peso em QUILOS: '))
IMC = peso/(alt*alt)
print(IMC)
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC >= 18.5 and IMC < 25:
    print('Você está com o peso ideal.')
elif IMC >= 25 and IMC < 30:
    print('Você está com sobrepeso.')
elif IMC >= 30 and IMC < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
