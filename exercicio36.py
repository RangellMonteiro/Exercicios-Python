#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input("Qual o valor do Imóvel? R$ "))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Em quantos anos deseja pagar? "))
meses = anos * 12
prestacao = valorCasa / meses

print("Para pagar uma casa de R${:.2f} em  {} anos a prestação será de R${:.2f}".format(valorCasa,anos, prestacao))

if prestacao > 30/100 * salario:
    print("Empréstimo negado pois a prestação excede 30% do salário")

else:
    print("Empréstimo aprovado")
