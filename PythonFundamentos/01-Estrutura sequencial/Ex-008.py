'''
Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o
valor do rendimento e o valor total depois do rendimento.
Autor:Jules do Nascimento Pires
Ex:008
Versão:V1
Data:02/07/2025
'''
# Biblioteca os
import os

# Limpa a tela       
os.system('cls')

# Entrada de dados
deposito = float(input("Informe o valor do depósito R$:"))
taxa = float(input("Informe o valor da taxa de juros:"))

# Cálculo
rendimento = deposito * taxa / 100
valorfinal = deposito + rendimento

# Resultado
print("Rendimento R$: {}".format(rendimento))
print("Valor final do rendimento R$: {}".format(valorfinal))

# Fim