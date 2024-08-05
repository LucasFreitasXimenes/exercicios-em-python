velo = float (input('Digite a velocidade que seu carro andou: '))
multa = (velo-80)*7
if velo > 80:
    print ('Você foi multado')
    print ('Pagará {} pelo velocidade'.format(multa))
else:
    print('Não tem multas pendentes!')    
    