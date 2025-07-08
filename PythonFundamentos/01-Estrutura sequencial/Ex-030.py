'''
Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se
que este sofreu um desconto de 10%.
Autor:Jules do Nascimento Pires
Ex:030
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
preco = float(input("Informe o preço do produto R$:"))

# Cálculo
desconto = preco * 0.10
precoFinal = preco - desconto

# Resultado
print("O produto que custava R$ {} irá custar R$ {} com desconto de 10%".format(preco, precoFinal))