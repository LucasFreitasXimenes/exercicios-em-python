peso = float (input('Digite seu peso: (KG)'))

altura = float (input ('Digite sua altura: (M)'))

imc = peso / (altura**2)

print ('Seu IMC é: ',imc)

if (imc<18.50):
    print('Está abaixo do peso!')
elif (imc >= 18.50 and imc <=25.00):
    print('Está no peso ideal')
elif (imc >=25.00 and imc <=30.00):
    print ('Sobrepeso')
elif (imc >=30.00 and imc <=40.0):
    print('Obesidade')
elif(imc>40.00):
    print ('Obesidade mórbida')