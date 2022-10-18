'''15. Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
isósceles ou escaleno. Dicas:

Três lados formam um triangulo quando a soma de quaisquer dos dois lados é maior que o terceiro.
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

a = float(input('Informe o primeiro lado do triangulo: '))
b = float(input('Informe outro lado do triangulo: '))
c = float(input('Informe mais um lado do triangulo: ' ))
if a < b + c and b < a + c and c < a + b:
    print('Temos um triangulo!')
    if a == b and b == c:
        print('Temos um triângulo equilátero!')
    elif a == b or b == c or c == a:
        print('Temos um triangulo isóceles!')
    else:
        print('Temos um triangulo escaleno!')
else:
    print('Não é um triângulo!')




