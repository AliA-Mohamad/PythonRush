from array import *

# some os valores {10, 20, 30, 40, 50} usando array nativa.

inteiros = array('i', [10, 20, 30, 40, 50])
soma = 0

for inteiro in inteiros:
    soma += inteiro

print(f"Resultado: {soma}")

# converção de C para F  { Fórmula: (Celsius * 1.8) + 32 }

temperaturas = array('f', [0.0, 25.5, 30.0, 100.0])

for i in range(len(temperaturas)):
    temperaturas[i] = (temperaturas[i] * 1.8) + 32

print("resultado:", temperaturas)


# motre apenas os impares

dados_brutos = array('i', [1, 4, 7, 10, 13, 18, 21])
pares = array('i')

for numero in dados_brutos:
    if numero % 2 == 0:
        pares.append(numero)

print("resultado:", pares)