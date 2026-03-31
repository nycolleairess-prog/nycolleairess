#Elabore um algoritmo que receba dois números, calcule a multiplicação entre eles e apresente o resultado.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
resultado = a * b
print("O resultado da multiplicação é: ", resultado)

#Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o resultado final.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
d = float(input("Digite o quarto número: "))
e = float(input("Digite o quinto número: "))
resultado = (a + b + c + d + e) / 5
print("A média aritmédica é: ", resultado)

#Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um acréscimo de 8% de imposto.

valor = float(input("Digite o valor do produto: "))
acrescimo = valor * 0.08 
preco_final = valor + acrescimo
print(f"O preço final com acréscimo é: {preco_final:.2f}")

#Elabore um algoritmo que receba dois números e apresente o resultado da subtração entre eles.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
resultado = a - b
print("O resultado da subtração é: ", resultado)

#Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa Corporal (IMC).

altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = (altura * altura) / peso
print("Seu índice de massa corporal é: ", imc)

#Elabore um algoritmo que receba a temperatura em graus Celsius e apresente o valor convertido para graus Fahrenheit.

celsius = float(input("Digite a temperatura em celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em fahrenheit é: ", fahrenheit)

#Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor da hora trabalhada, calculando o salário total.

quantidade = float(input("Digite a quantidade de horas trabalhadas: "))
valor = float(input("Digite o valor da hora trabalhada: "))
salario = quantidade * valor
print(f"O salário do funcionário é: {salario:.2f}")