'''Fácil 19 – Faça um programa que receba dez números e
usando laços de repetição calcule e mostre a quantidade
de números entre 30 e 90.'''
contador = 0
for i in range(10):
    num = int(input(f'Informe o {i + 1}º numero: '))
    if num >= 30 and num <= 90:
        contador += 1
print(contador)
