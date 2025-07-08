'''
Faça um programa que receba três números, calcule e mostre a multiplicação desses números.
Autor:Jules do Nascimento Pires
Ex-027
Versão:V1
'''

# Biblioteca
import os

os.system('cls')

# Entrada de dados
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))
num3 = int(input("Terçeiro valor:"))

# Multiplicação
mult = num1 * num2 * num3

# Resultado
print("A multiplicação entre {} * {} * {} =".format(num1, num2, num3, mult))

# Fim