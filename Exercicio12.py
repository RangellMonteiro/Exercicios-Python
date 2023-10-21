# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salario do funcionário aqui: R$"))
aumento = (15 * salario) / 100
novoSalario = salario + aumento 
print("Um funcionário que ganhava R${:.2f} com 15% de aumento passa a ganhar R${:.2f}".format(salario,novoSalario))
