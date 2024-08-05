n = float(input("Digite um número para verificar se ele é primo: "))

# Verificar se o número é maior que 1
if n > 1:
    # Verificar se o número é divisível apenas por 1 e por ele mesmo
    for i in range(2, int(n)):
        if (n % i) == 0:
            print("O {} não é primo!".format(n))
            break
    else:
        print("O {} é primo!".format(n))
else:
    print("O {} não é primo!".format(n))
