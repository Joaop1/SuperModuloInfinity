16.
Faça
um
programa
que
calcule as raízes
de
uma
equação
do
segundo
grau, na
forma
ax2 + bx + c.O
programa
deverá
pedir
os
valores
de
a, b
e
c
e
fazer as consistências, informando
ao
usuário
nas
seguintes
situações:

a.Se
o
usuário
informar
o
valor
de
A
igual
a
zero.a
equação
não
e
do
segundo
grau
e
o
programa
não
deve
fazer
pedir
os
demais
valores, sendo
encerrado;
b.Se
o
delta
calculado
for negativo, a equação não possui raízes reais.Informe ao usuário e encerre o programa;
c.Se
o
delta
calculado
for igual a zero a equação possui apenas uma raiz real; informe ao usuário;
d.Se
o
delta
for positivo, a equação possui duas raízes reais; informe- as ao usuário;

a = float(input("Digite o valor de A: "))
if a == 0:
    print("A equação não é do segundo grau!")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    delta = (b * b) - (4 * a * c)

    print(delta)

    if delta < 0:
        print("A equação não possui raizes reais!")
    elif delta == 0:
        print("A equação possui apenas uma raiz!")
    else:
        print("A equação possui duas raizes!")