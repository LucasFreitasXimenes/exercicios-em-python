nome = str (input('Digite seu nome completo:')).strip()
n = nome.split() #separando o nome por lista
print ('Muito prazer em te conhecer! {}'.format(nome)) 
print ('Seu primeiro nome é: {}'.format(n[0])) #exibindo o item 0 da lista
print ('Seu último nome é: {}'.format(n[len(n)-1])) 
#lendo todos os itens da lista e no final ele contabiliza o ultimo item