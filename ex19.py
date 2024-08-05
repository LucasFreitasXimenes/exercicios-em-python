from random import choice # dentro da biblioteca random quero utilizar a funcionalidade de escolha (choice)
a = str(input ('Digite o nome de um aluno: '))
a2 = str(input ('Digite o nome de outro aluno: '))
a3 = str(input ('Digite o nome de outro aluno: '))
a4 = str(input ('Digite o nome de outro aluno: '))

lista = [a,a2,a3,a4]#entre as chaves você cria uma lista para o python
escolhido = choice(lista)#faça uma escolha aleatoria dentro da variavel que armazena a lista
print ('O aluno escolhido foi {}'.format(escolhido))