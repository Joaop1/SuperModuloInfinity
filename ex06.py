'''25 – Escreva um programa que pergunte o raio de uma circunferência, e em seguida mostre o
diâmetro, comprimento e área da circunferência;'''
raio = float(input('Informe o raio da circunferência: '))
diametro = raio * 2
print(f'O diametro da circunferência é {diametro}')
comp = raio * 3.14 * 2
print(f'O comprimento dessa circunferência é {comp}')
area = 3.14 * (raio * raio)
print(f'A área dessa circunferência é {area}')
