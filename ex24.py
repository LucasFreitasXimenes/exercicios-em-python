cidade = str (input('Digite a cidade de seu nascimento: ')).strip()#removendo os espaços antes e depois

print (cidade[:5].upper() == 'SANTO')#transformando a cidade em maiuscula e comparando com a palavra SANTO se tiver 5 espaços na primeira palavra sera true caso contrario false