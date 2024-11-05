# Rodrigo Sá Teles Moraes - 494145
def somar(a, b):
    return a + b

print("Resultado da soma inicial:", somar(2, 3))

def subtrair(a, b):
    return a - b

print("Resultado da subtração inicial:", subtrair(4, 3))

def multiplicar(a, b):
    return a * b

print("Resultado da multiplicação inicial:", multiplicar(2, 5))

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"
    
print("Resultado da divisão por 0:", dividir(2, 0))
print("Resultado da divisão inteira:", dividir(6, 2))

def exponenciar(a, b):
    return a ** b

print("Resultado da exponenciação:", exponenciar(2, 5))


def modulo(a, b):
    return a % b

print("Resultado do módulo da divisão:", modulo(5, 2))

