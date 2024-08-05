from time import sleep
n = int (input ('Digite um número: '))
print('A tabuada de seu número é:')
sleep(1)

for c in range (1,10+1,1):
    conta = n * c
    print (n,'x',c ,'=', conta)
    
      
