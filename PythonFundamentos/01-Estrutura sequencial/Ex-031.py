'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa
que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu
salário final.
Autor:Jules do Nascimento Pires
Ex-031
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
salarioFixo = float(input("Salário Fixo R$:"))
valorVendas = float(input("Valor das vendas R$:"))

# Cálculo
comissao = salarioFixo * 4 / 100
salarioFinal = salarioFixo + comissao

# Resultado
print("Valor da comissão R${:.2f}".format(comissao))
print("Salário Final R$:{:.2f}".format(salarioFinal))