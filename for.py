for c in range (6,0,-1):# o ultimo na contagem ele ignora
 #o ultimo campo é a iteração ou seja oq vai acontecer no laço nessa situação ele está exibindo de trás pra frente
    print (c)

n = int (input('Digite um numero'))
for c in range(0,n+1):
    print(c)


inicio = int(input('inicio'))
fim = int(input('fim'))
passo = int(input('passo'))
for c in range(inicio,fim+1,passo):
    print(c)

s=0
for c in range(0,7):#lembrando que ele só armazena um valor
    n = int(input('Digite um valor'))
    s= s+n
print('O somatório de todos os valores foi{}'.format(s))