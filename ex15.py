km = float (input('Digite a distância que percorrereu no carro alugado em KM: '))
dia = int (input('Por quantos dias você alugou o carro?'))
pagar = km * 0.15
pagar2 = dia * 60
total = pagar + pagar2

print ('Você percorreu {} KM e pagará {}'.format(km,pagar))
print ('Você alugou por {} dia(s) e pagará {}'.format(dia,pagar2))
print ('total {}'.format(total))
