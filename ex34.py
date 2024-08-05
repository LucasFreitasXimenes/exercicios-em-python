salario = float (input('Digite seu salário: '))
if salario >1250:
    aumento = (salario*10)/100
    print ('Houve um aumento de {} no seu salario'.format(aumento))
else:
    aumento = (salario*15)/100
    print ('Houve um aumento de {} no seu salario'.format(aumento))
