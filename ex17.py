#Maneira matemática sem importção 
#co = float (input('Digite o comprimento do cateto oposto: '))
#ca = float (input('Digite o comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print ('A hipotenusa vale: {}!'.format(hi))


#Importando a funcionalidade de calculo de hipotenusa (hypot)
from math import hypot
co = float (input('Digite o comprimento do cateto oposto: '))
ca = float (input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print ('A hipotenusa é: {}'.format(hi))