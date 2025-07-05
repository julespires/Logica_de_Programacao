'''
Um trabalhador recebeu seu salário e o depositou em sua conta bancária. Esse trabalhador emitiu dois
cheques e agora deseja saber seu saldo atual. Sabe-se que cada operação bancária de retirada paga
CPMF de 0,38% e o saldo inicial da conta está zerado.
Autor:Jules do Nascimento Pires
Ex:017
Versão:V1
Data:05/07/2025
'''

# Biblioteca de sistema
import os

# Limpa a tela do prompt
os.system('cls')

# Entrada de dados
salario = float(input("Salário: R$"))
cheque1 = float(input("Valor do Cheque 1:"))
cheque2 = float(input("Valor do Cheque 2:"))

# Cálculo
cpmf1 = cheque1 * 0.38 / 100
cpmf2 = cheque2 * 0.38 / 100
saldo = salario - cheque1 - cheque2 - cpmf1 - cpmf2

# Resultado
print("Seu saldo atual é:", saldo)

