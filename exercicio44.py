#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

preco = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    precoFinal = preco - (preco * 10/100)
    print("Sua compra no valor de {:.2f}R$ com os 10% de desconto a vista vai custar {:.2f} no final ".format(preco,precoFinal))
elif opcao == 2:
    precoFinal = preco - (preco * 5/100)
    print("Sua compra no valor de {:.2f}R$ com os 5% de desconto a vista vai custar {:.2f} no final ".format(preco,precoFinal))
elif opcao == 3:
    precoFinal = preco
    parcelas = precoFinal / 2
    print("Sua compra será parcelada em 2x de {}".format(parcelas))
elif opcao == 4:
    precoFinal = preco + (preco * 20/100)
    parcelamento = int(input("Deseja parcelar em quantas vezes?"))
    parcelas = precoFinal / parcelamento
    print("Sua compra no valor de {:.2f}R$ com o acréscimo de 20% de juros custará  {:.2f} no final, e o valor das parcelas será de {:.2f} ".format(preco,precoFinal, parcelas))
else:
    print("Opção inválida!")




        

