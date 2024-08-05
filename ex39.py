ano = int (input('Digite o ano em que nasceu: '))
anoatual = 2024
idade = anoatual - ano
print ('Você tem',idade,'anos')
if(idade<18):
    print('Você ainda vai se alistar ao serviço militar!')
    print ('falta',18-idade,'ano(s) para se alistar')
elif (idade==18):
    print ('Está no ano de se alistar, boa sorte!')
else:
    print('Já passou do tempo de alistamento.')    
    print (idade-18,'ano(s) que passou o prazo')