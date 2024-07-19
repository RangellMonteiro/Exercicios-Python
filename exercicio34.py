#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Digite aqui o salário do funcionário R$"))
aumento = 0

if salario > 1250:
    aumento = (10/100) * salario

if salario <= 1250:
    aumento = (15/100)* salario

print("Quem ganhava {:.2f} vai passar a ganhar {:.2f}".format(salario, salario + aumento))


