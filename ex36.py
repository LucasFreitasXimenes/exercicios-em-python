nome = str (input('Digite seu nome: '))
print ('Olá sejá bem vindo',nome,'!')
salario = float (input('Qual seu salário atual?'))
print ('Certo, seu salário atual é de',salario,'R$!')
vlr = float (input('Qual o valor da casa que deseja comprar: '))
ano = int (input('Em quantos anos deseja pagar a casa?'))
prestacao = vlr/ano
print ('voce pagara',prestacao,'ao ano!')
parcela = prestacao/12
print (nome,'você pagará',parcela,'por mês, em',ano,'anos')
salario2= salario *30/100

if (parcela<=salario2):
    print (nome,'parabéns, seu empréstimo foi aprovado!')
else:
    print('infelizmente, seu empréstimo foi negado!')