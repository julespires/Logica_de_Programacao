'''
Faça um programa que receba os anos de serviço de uma pessoa e o valor por ano, calcule o valor final com o bonus
Autor:Jules do Nascimento Pires
Ex
'''

anos = int(input("Anos de serviço:"))

valor_por_ano = float(input("Valor por ano:"))

bonus = anos * valor_por_ano

print("Bonus de R$ {:.2f}".format(bonus))