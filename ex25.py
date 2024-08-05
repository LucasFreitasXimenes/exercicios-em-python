nome = str (input('Digite seu nome: ')).strip()

print ('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print ('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))
