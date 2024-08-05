nome = str (input('Digite seu nome completo: ')).strip()#elinando os espaços antes e depois porém mantem fazendo contagem entre as palavras
print ('avaliando seu nome: ')
print('seu nome em maiusculo fica: {}'.format(nome.upper()))
print('seu nome em minusculo fica: {}'.format(nome.lower()))
print('lendo o seu nome sem os espaços contabiliza {} caracteres!'.format(len(nome)- nome.count(' ')))#substituindo os espaços por um espaço vazio ou seja nada
#o strip não funciona nesse caso pois removeria o espaçamento somente entre o começo e o fim por isso uso subtraio o espaço
print ('seu nome inicial tem {} letras !'.format(nome.find(' ')))#find = encontre / o primero espaço
