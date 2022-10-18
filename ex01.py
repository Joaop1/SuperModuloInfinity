'''1- Faça um programa que peça dois números e verifique (usando if e else)
e imprima o maior deles;'''
num1 = int(input('informe um número: '))
num2 = int(input('informe outro número: '))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print('Os números são iguais')
