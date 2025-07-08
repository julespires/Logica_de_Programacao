'''
Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.
Autor:Jules do Nascimento Pires
Ex-012
Versão:V1
Data:04/07/2025
'''

# Biblioteca
import os

os.system('cls')
# Entrada de dados
num1 = float(input("Digite o primeiro valor:"))
num2 = float(input("Digite o segundo valor:"))

# Cálculo dos valores
r1 = num1 ** num2
r2 = num2 ** num1

# Resultado
print("O número {} elevado a {} = {}".format(num1, num2, r1))
print("O número {} elevado a {} = {}".format(num2, num1, r2))

# Fim