'''
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do
distribuidor e dos impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fá-
brica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos, calcule e mostre:
a) o valor correspondente ao lucro do distribuidor;
b) o valor correspondente aos impostos;
c) o preço final do veículo.
Autor:Jules do Nascimento Pires
Ex:015
Versão:V1
Data:04/07/2025
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
precoFabrica = float(input("Preço de fabrica R$:"))
percentualDistribuidor = float(input("Percentual de aumento %:"))
percentualImposto = float(input("Percentual de imposto %:"))

# Cálculo
lucroDistribuidor = precoFabrica * percentualDistribuidor / 100
valorImposto = precoFabrica * percentualImposto / 100
precoFinal = precoFabrica + lucroDistribuidor + percentualImposto

# Resultado
print("Lucro do distribuidor: R$ {}".format(lucroDistribuidor))
print("Percentual de imposto: R$ {}".format(valorImposto))
print("Preço final: R$ {}".format(precoFinal))