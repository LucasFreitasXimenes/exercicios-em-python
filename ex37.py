n =  int (input('Digite um número inteiro qualquer: '))
print ('Escolha a base de conversão')
print ('1 = binario')
print ('2 = octal')
print ('3 = hexadecimal')

opcao = int (input('Qual opção você escolhe: '))

if (opcao == 1):
    print ('O numéro em binário:')
    print(bin(n)[2:])
    
elif (opcao ==2):
    print('O número em octadecimal')
    print(oct(n)[2:])

elif (opcao ==3):
    print('O número em hexadecimal')
    print(hex(n)[2:])

else:
    print ('Escolha uma opção válida!')