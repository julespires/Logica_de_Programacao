import math

# Entrada de dados
angulo_graus = float(input("Digite o ângulo formado com o chão (em graus): "))
altura = float(input("Digite a altura da parede (em metros): "))

# Converter graus para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcular o comprimento da escada
escada = altura / math.sin(angulo_radianos)

# Mostrar o resultado
print(f"O comprimento da escada é: {escada:.2f} metros")

# Fim