'''nota = 0
contador = 0
while contador < 4:
    x = float(input(f'Digite a {contador + 1}ª nota: '))
    nota += x
    contador += 1
media = nota/4
print(media)'''
nota = 0
contador = 1
while True:
    x = float(input('Digite uma nota:'))
    nota += x

    if contador == 4:
        break
media = nota /4
print(media)