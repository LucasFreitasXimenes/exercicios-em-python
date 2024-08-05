m = float (input('digite a quantidade que deseja calcular em metros : '))

mili = m * 1000
cent = m  * 100
km = m/1000
hecto = m / 100
decame = m / 10
decime = 10 *  m

print ('A quantidade em metros: {} , em milimetros: {:.0f} e em centimentros: {:.0f}, \n em km : {}, em hectometros: {} em decametros: {}, e em decimetros {}!'.format(m,mili,cent,km,hecto,decame,decime))