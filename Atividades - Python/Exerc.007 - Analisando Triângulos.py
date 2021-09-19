print('\nVamos agora descobrir se as medidas que você tem serão capazes de formar um triângulo e qual o tipo de triâgulo formado.\n')
a = int(input('Digite o valor de um dos lados da figura: '))
b = int(input('Digite o valor de outro lado da figura: '))
c = int(input('Digite o valor do terceiro lado da figura: '))
a1 = b + c
b1 = a + c
c1 = a + b
if a1 > a and b1 > b and c1 > c and a == b == c:
    print('Triângulo possível e é um do tipo EQUILATERO.\n')
elif a1 > a and b1 > b and c1 > c and (a == b != c or a == c != b or b == c != a):
    print('Triângulo possível e é um do tipo ISOSCELES.\n')
elif a1 > a and b1 > b and c1 > c and a != b != c != a:
    print('Triângulo possível e é um do tipo ESCALENO.\n')
elif b1 > b and a1 > a and c1 > c and a == b == c:
    print('Triâgulo possível e é um do tipo EQUILATERO.\n')
elif b1 > b and a1 > a and c1 > c and (a == b != c or a == c != b or b == c != a):
    print('Triângulo possível e é um do tipo ISOSCELES.\n')
elif b1 > b and a1 > a and c1 > c and a != b != c != a:
    print('Triângulo possível e é um do tipo ESCALENO.\n')
elif c1 > c and a1 > a and b1 > b and a == b == c:
    print('Triângulo possível e é um do tipo EQUILATERO.\n')
elif c1 > c and a1 > a and b1 > b and (a == b != c or a == c != b or c == b != a):
    print('Triângulo possível e é um do tipo ISOSCELES.\n')
elif c1 > c and a1 > a and b1 > b and a != b != c != a:
    print('Triângulo possível e é um do tipo ESCALENO.\n')
else:
    print('Com essas medidas, seu triângulo é IMPOSSÍVEL.\n')
