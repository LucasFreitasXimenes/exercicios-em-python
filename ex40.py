nota1 = float (input('Digite sua primeira nota: '))
nota2 = float (input('Digite sua segunda nota: '))
media = (nota1 + nota2)/2
print ('A média das sua notas foi: ',media)
if (media<5):
    print('REPROVADO!')
elif (media>=5 and media <7):
    print ('RECUPERAÇÃO')
else:
    print ('APROVADO!')