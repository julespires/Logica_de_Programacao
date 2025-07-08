'''
Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se
que este sofreu um aumento de 25%.
Autor:Jules do Nascimento Pires
Ex:005
Versão:V1
Data:01/07/2025
'''

# Biblioteca
import os

#Limpa a tela
os.system('cls')

# Entrada de dados
sal = float(input("Salário do funcionário R$"))

# Cálculo
novoSal = sal + sal * 25 / 100

# Resultado
print("O novo salário com 25% de aumento é R$:", novoSal)

# Fim