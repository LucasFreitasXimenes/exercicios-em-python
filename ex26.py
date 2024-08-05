nome = str (input('digite seu nome: ')).strip().upper()
qtd = nome.count('A')

print ('A letra A aparece {} vezes em seu nome!'.format(qtd))
print ('A primeira letra apareceu na {} posição'.format(nome.find('A')+1))#encontre a primeira aparição da string A
print ('A ultima letra apareceu na {} posição'.format(nome.rfind('A')+1))#encontre a ultima posicao apareceu a string A
