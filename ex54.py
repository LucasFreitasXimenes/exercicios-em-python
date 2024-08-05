contador_maior = 0
contador_menor = 0

for c in range(0, 7):
    idade = int(input('Digite sua idade: '))
    
    if idade >= 18:
        contador_maior += 1
    else:
        contador_menor += 1

print("Total de idades maiores de 18:", contador_maior)
print("Total de idades menores de 18:", contador_menor)
