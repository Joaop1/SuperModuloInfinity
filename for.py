nome = "Joao"
contador = 0
for i in nome:
    if i.lower() in ('a', 'e', 'i', 'o', 'u'):
        contador +=1
print(contador)