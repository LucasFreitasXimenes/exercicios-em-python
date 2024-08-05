print ('=='*20)
print ('Analisando triangulos')
print ('=='*20)
r1 = float (input('Digite o primeiro lado: '))
r2 = float (input('Digite o segundo lado: '))
r3 = float (input('Digite o terceiro lado: '))

if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('=='*20)
    print ('Os segmentos formaram um triangulo')
    print ('=='*20)
else:
    print ('=='*20)
    print ('Não é possivel formar um triangulo')
    print ('=='*20)

    