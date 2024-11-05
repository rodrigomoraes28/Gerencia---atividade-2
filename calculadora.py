# Rodrigo Sá Teles Moraes - 494145
# Data da atividade: 5/11/2024 às 14:40

#Essa operação é a de soma
def somar(a, b):
    return a + b

print("Resultado da soma inicial:", somar(2, 3))

#Essa operação é a de subtração
def subtrair(a, b):
    return a - b

print("Resultado da subtração inicial:", subtrair(4, 3))

#Essa operação é a de multiplicação
def multiplicar(a, b):
    return a * b

print("Resultado da multiplicação inicial:", multiplicar(2, 5))

#Essa operação é a de divisão
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"
    
print("Resultado da divisão por 0:", dividir(2, 0))
print("Resultado da divisão inteira:", dividir(6, 2))

#Essa operação é a de exponenciação
def exponenciar(a, b):
    return a ** b

print("Resultado da exponenciação:", exponenciar(2, 5))

#Essa operação é a de módulo da divisão
def modulo(a, b):
    return a % b

print("Resultado do módulo da divisão:", modulo(5, 2))

