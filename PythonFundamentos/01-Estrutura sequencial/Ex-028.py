''' 
Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo
segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar
com validações.
Autor:Jules do Nascimento Pires
Ex-028
'''

# Biblioteca
import os

# Limpa a tela
os.system('cls')

# Entrada de dados
num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

# Divisão
div = num1 / num2

# Resultado
print("A divisão entre {} / {} = {}".format(num1, num2, div))