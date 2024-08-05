d = float (input('digite a distancia de uma viagem até a outra: '))
if d<=200:
    preco = d*0.50
    print('o preço a se pagar pela distancia é: {}'.format(preco))
else:
    preco = d*0.45
    print ('o preço a se pagar pela distancia é: {}'.format(preco))