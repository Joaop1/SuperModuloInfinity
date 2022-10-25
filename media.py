notas = 0
for i in range(4):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    notas += nota
media = notas / 4
print(media)