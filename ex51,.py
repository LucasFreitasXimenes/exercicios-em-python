a1 = int(input('Insira o valor do primeiro termo: '))
r = int(input('Insira o valor da razão: '))
pa = a1 + (9 * r)
for c in range(a1, pa, r):
    print(c)