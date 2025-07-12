'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado. 
'''

# Biblioteca
import os

#
os.system('cls')

# Entrada de dados
peso = float(input("Informe o seu peso:"))

# Cálculo
pesoEngordar = peso + (peso * 0.15)
pesoEmagrecer = peso - (peso * 0.20)

# Resultado
print("Novo peso se você engordar 15%:{:.2f}".format(pesoEngordar))
print("Novo peso se você emagreçer 20%:{:.2f}".format(pesoEmagrecer))