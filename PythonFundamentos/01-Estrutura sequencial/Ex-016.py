'''
Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo, calcule e
mostre o salário a receber, seguindo estas regras:
a) a hora trabalhada vale a metade do salário mínimo.
b) o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada.
c) o imposto equivale a 3% do salário bruto.
d) o salário a receber equivale ao salário bruto menos o imposto.
Autor:Jules do Nascimento Pires
Ex:016
Versão:V1
Data:04/07/2025
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
horasTrabalhadas = int(input("Horas trabalhadas:"))
salarioMinimo = float(input("Salário mínimo: R$"))

# cálculo
valorHorasTrabalhadas = salarioMinimo / 2
valorSalarioBruto = valorHorasTrabalhadas  * horasTrabalhadas
imposto = valorSalarioBruto * 3 / 100
salarioLiquido = valorSalarioBruto - imposto

# Resultado
print("Salário líquido: R$ {}".format(salarioLiquido))

# Fim