'''
Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber,
sabendo-se que o funcionário tem gratificação de R$ 50 e paga imposto de 10% sobre o salário base.
Autor:Jules do Nascimento Pires
Ex:007
Versão:V1
Data:01/07/2025
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
sal = float(input("Salário base R$:"))

# Limpa a tela
os.system('cls')

# Cálculo
imposto = sal * 10 / 100
novosal = sal + 50 - imposto

# resultado
print("O novo salário com aumento de R$ 50 e imposto de 10% = R$: {}".format(novosal))