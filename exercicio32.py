# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual o salário do funcionário? R$"))

#Aumento de 10% para salários superiores a R$1250,00
if salario > 1250.00:
    aumento = (10 * salario) / 100
else:
    aumento = (15 * salario) / 100

novoSalario = salario + aumento

print("Quem ganhava R${:2f} passou a ganhar R${:.2f} agora".format(salario,novoSalario))


