frase = 'Curso em video python'
print (frase[3]) #fatiando o 4 caracter lembrando que começa do 0
print (frase[3:13])#fatiando a frase entre 4 e 12 lembrando que começa do 0 e ignora a ultima
print (frase [::2])#fatiando sem inicio e sem fim ou seja a frase toda com um espaço de 2 em 2 caracteres

print("""ashaushaushauhsauhsuahsuahasahsuahusahs
       haushaushaushauhsuahsaushaushaushaushausha
       ahsuahsuahsuahsuahsuahsuahshuahsuahsuahsua
       ahsuahsuahsuahsuahsuahushaushaushaushausha""")#com as asplas duplas triplas você consegue fazer um print maior

print (frase.count('o')) #fazendo a contagem de 'o' acordo com o conteudo da varivavel frase
print (frase.upper().count('O')) #fazendo a contagem de 'O' maiusculo lembrando que o upper transforma as letras em maiusculo
print (len(frase)) #contagem dos espaços ocupados na variavel frase
#.strip() tira os espaços da frente e de tras
print (frase.replace('python', 'Android')) #substituindo os caracteres python por android no print
print (frase)#aqui percebemos que o conteudo da variavel frase nao foi alterado pois em cima voce so substituiu no print
#para salvar a substituição (replace) voce deve fazer uma atribuicao
frase = frase.replace('python','android')
print ('Curso' in frase) # a palavra curso está na frase?
#true
print (frase.find('Curso'))
#curso se inicia na posição 0 o find vai mostrar aonde começa
print (frase.find('VIDEO'))
#percebemos no codigo acima que ele exibe o -1 pois VIDEO nao existe só video
print (frase.upper().find('VIDEO'))
#o UPPER vai transformar o conteudo da variavel frase em maiusculo
#fazendo que a palavra VIDEO esteja no conteudo e seja encontrada a 1 letra no caracter 9
print (frase.split())
#criou uma lista e dividiu e definiu as palavras pelo espaçamento
dividido = frase.split()
print (dividido[0])#mostrar somente a palavra separada que possui o espaço 0
print (dividido[2][3])#aqui no caso eu estou pegando o 2 dividido no caso 0 é curso 1 é em e 2 video
#e exibindo o 3 espaço entre esse caracter