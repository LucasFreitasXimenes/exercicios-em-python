from random import shuffle
a1 = str (input('Digite um aluno: '))
a2 = str (input('Digite outro aluno: '))
a3 = str (input ('Digite outro aluno: '))
a4 = str (input('Digite outro aluno: '))

lista =  [a1,a2,a3,a4]#criando uma lista com os dados armazenados nas variaveis
shuffle(lista)#método de embaralhar
print ('A ordem sorteada entre os alunos foi')
print (lista)