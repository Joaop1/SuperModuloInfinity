'''18. Faça um Programa que peça um número inteiro e determine se ele e par ou ímpar.
 Dica: utilize o operador módulo (resto da divisão);'''
num = int(input('Informe um número: '))
if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O numero {num} é ímpar!')
