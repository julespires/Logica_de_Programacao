'''
Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre
o valor do aumento e o novo salário.
Autor:Jules do Nascimento Pires
Ex:006
Versão:V1
Data:01/07/2025
'''

import os

os.system('cls')

sal = float(input("Salário R$"))
perc = float(input("Percentual de aumento %"))

os.system('cls')

# Cálculo
aumento = sal * perc / 100
novosal = sal + aumento

# Resultado
print("Valor do aumento R$:{}".format(aumento))
print("Novo salário R$:{} ".format(novosal))