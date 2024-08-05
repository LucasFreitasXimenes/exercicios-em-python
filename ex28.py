from random import randint

n = int (input('Digite um numero inteiro entre 0 e 5: '))
pc = randint(0,5)
if n==pc:
    print('Parabéns você acertou o numero')
else:
    print ('Eita tente de novo! o numero certo era {}'.format(pc))
if n > 5:
    print ('O numero deve ser de 0 a 5')