print ('Loja Lucas Ximenes')
preco = float (input('Digite o valor da compra? R$'))

print ('1 - Dinheiro/Cheque = 10%off')
print ('2 - Cartão 1X = 5%off')
print ('3 - Cartão 2X = preço normal')
print ('4 - Cartão 3x ou + = 20%juros')

pagamento = int (input('Qual forma de pagamento: '))


if  pagamento == 1:
    din =  preco - (preco * 10/100) 
    print = ('o valor da compra no dinheiro ou no cheque será: ',din)
elif pagamento == 2:
    cardav=  preco - (preco*5/100) 
    print ('O valor da compra em 1x fica: ',cardav,'R$')
elif pagamento == 3:
    parc2 = preco/2
    print ('O valor da compra foi ',preco,'R$ em 2x de',parc2,'R$')
    
elif pagamento == 4:
    parcelas = int (input('Quantas vezes você deseja parcelar?')) 
    juros = preco+(preco*20/100)
    jrseparcelas = juros/parcelas
    print('O valor da compra foi {}R$, com o juros de 20% pelas parcelas, ficou no total de: {}R$ parcelado em {} vezes o total de {}R$ por parcela' .format(preco,juros,parcelas,jrseparcelas))
    
