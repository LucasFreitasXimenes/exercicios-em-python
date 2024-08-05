soma_idades = 0
quantidade_homens = 0
quantidade_mulheres_menos_de_21 = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""

# Loop para coletar informações de 4 pessoas
for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [F/M] '))

    if sexo.upper() == 'M':
        quantidade_homens += 1
        if quantidade_homens == 1 or idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    elif sexo.upper() == 'F' and idade < 21:
        quantidade_mulheres_menos_de_21 += 1

    # Adicionando a idade à soma das idades
    soma_idades += idade

# Calculando a média das idades
media_idades = soma_idades / 4

# Imprimindo a média das idades
print('A média das idades é:', media_idades)

# Imprimindo o nome do homem mais velho
if quantidade_homens > 0:
    print('O homem mais velho é:', nome_homem_mais_velho)
else:
    print('Não há homens nesta lista.')

# Imprimindo a quantidade de mulheres com menos de 21 anos
print('A quantidade de mulheres com menos de 21 anos é:', quantidade_mulheres_menos_de_21)
