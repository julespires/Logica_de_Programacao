'''
Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.
Autor:Jules do Nascimento Pires
Ex-033
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
pesoPessoa = float(input("Informe o seu peso em Kg:"))

# Cálculo
pesoGramas = pesoPessoa * 1000

# Resultado
print("O seu peso de {}Kg em gramas é {}G".format(pesoPessoa, pesoGramas))