for c in range (0,6):
    n= int (input('Digite um valor'))
    par = (n%2)==0
    if c%2==0:
        soma = par*c==0 
        print ('os pares são: {}  '.format(c))