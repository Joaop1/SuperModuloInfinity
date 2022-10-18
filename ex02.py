#9- Faça um programa que leia três números e mostre-os em ordem decrescente;
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
num3 = int(input('Informe mais um número: '))
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)


