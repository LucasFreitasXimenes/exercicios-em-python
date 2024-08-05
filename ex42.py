r1 = float (input('Digite o primeiro lado: '))
r2 = float (input('Digite o segundo lado: '))
r3 = float (input('Digite o terceiro lado: '))

if r1 < r2 +r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('=='*20)
    print ('Os segmentos formaram um triangulo ', end='')
   #condição aninhada
    if r1 == r2 == r3:
        print = ("equilatero")
    elif r1 != r2 and r2 != r3 and r1!= r3:
        print ("escaleno")
    else:
        print ("isoceles")
else:
    print ('=='*20)
    print ('Não é possivel formar um triangulo')
    print ('=='*20)
