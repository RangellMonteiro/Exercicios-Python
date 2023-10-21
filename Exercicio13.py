#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperatura = float(input("Digite a temperatura que deseja converter: "))
conversor = temperatura * c / 5 + 32
print("{:.2f}C° são {:.2f}F°".format(temperatura,conversor))