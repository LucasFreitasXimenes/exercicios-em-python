ano = int (input('Digite o ano em que nasceu:'))
anoatual = 2024
idade = anoatual-ano
print('você tem',idade,'anos!')
if (idade<=9):
    print ('CATEGORIA MIRIM')
elif (idade <=14):
    print ('CATEGORIA INFANTIL')
elif (idade<=19):
    print ('CATEGORIA JÚNIOR')
elif (idade<=25 ):
    print ('CATEGORIA SÊNIOR')
else:
    print ('CATEGORIA MASTER')
