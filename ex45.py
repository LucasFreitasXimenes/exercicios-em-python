from random import randint
from time import sleep

print(20*'-')
print('Bora brincar de Joken PO contra a máquina?')
jogar = int(input('1 - sim / 2 - não.'))
print(20*'-')

if jogar == 1:
    itens = ('Pedra', 'Papel', 'Tesoura')  # Corrigido 'Tesoursa' para 'Tesoura'
    print('Suas opções')
    print('-='*10)
    print('[0]- Pedra')
    print('[1] - Papel')
    print('[2] - Tesoura')
    print('-='*10)
    escolha = int(input('Você quer pedra papel ou tesoura? '))
    print ('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    computador = randint(0, 2)
    print('-='*10)
    print('O computador escolheu {}'.format(itens[computador]))

    print('O jogador escolheu', itens[escolha])
    print('-='*10)
    if computador == 0:  # se o jogador jogou pedra
        if escolha == 0:
            print('Empate!')
        elif escolha == 1:
            print('Ops, o computador venceu!')
        elif escolha == 2:
            print('Parabéns você venceu a máquina')  

            print('Jogada inválida')

    elif computador == 1:  # se o jogador jogou papel
        if escolha == 0:
            print('Ops, o computador venceu!')
        elif escolha == 1:
            print('Empate!')
        elif escolha == 2:
            print('Parabéns você venceu a máquina')  
        else:
            print('Jogada inválida')

    elif computador == 2:  # se o jogador jogou tesoura
        if escolha == 0:
            print('Parabéns você venceu a máquina')  
        elif escolha == 1:
            print('Ops, o computador venceu!')
        elif escolha == 2:
            print('Empate!')
        else:
            print('Jogada inválida')

else:
    print('Que pena...')
    SystemExit()
