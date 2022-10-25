'''Fácil  1 – Faça um programa que receba um número e
usando laços de repetição calcule e mostre a tabuada
desse número.'''

num  = int(input('Informe um numero: '))

for i in range(1, 11, 1):
    multi = num * i
    print(f'{num} * {i} = {multi}')

