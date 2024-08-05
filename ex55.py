primeiro_peso = float(input('Digite o primeiro peso: '))
maior_peso = primeiro_peso
menor_peso = primeiro_peso

for _ in range(1, 6):
    peso = float(input('Digite seu peso: '))
    
    if peso > maior_peso:
        maior_peso = peso
    
    if peso < menor_peso:
        menor_peso = peso

print('O maior peso foi:', maior_peso)
print('O menor peso foi:', menor_peso)
