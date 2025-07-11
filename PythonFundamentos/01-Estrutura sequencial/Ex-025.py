'''
Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo.
Esse programa deverá calcular e mostrar a quantidade de convites que devem ser vendidos para que,
pelo menos, o custo do espetáculo seja alcançado.
Autor:Jules do Nascimento Pires
Ex:025
Versão:V1
'''

# Bibliotca
import os

# Limpa a tela
os.system('cls')

#Entrada dos dados
custo = float(input("Custo do Espetáculo R$:"))
preco = float(input("Preço do Convite R$:"))

# Cálculo
quantidadeConvite = custo / preco

# Resultado
print("Para cobrir o custo do espetáculo, você deverá vender {} convites.".format(quantidadeConvite))