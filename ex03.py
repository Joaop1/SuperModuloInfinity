'''Fácil 9-    Faça um programa que receba a idade de
cinco pessoas e que calcule e mostre a quantidade de pessoas
 com idade maior ou igual a 18 anos.'''

contador = 0
for i in range(0, 5, 1):
    idade = int(input(f'Informe a {i + 1}ª idade: '))
    if idade >= 18:
        contador += 1
print(f'Temos {contador} maiores de idade')