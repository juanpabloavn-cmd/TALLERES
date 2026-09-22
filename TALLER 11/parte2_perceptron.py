# TALLER 11
# REDES NEURONALES - EL PERCEPTRÓN

import numpy as np


# 1. FUNCIÓN DE ACTIVACIÓN ESCALÓN

def funcion_escalon(z):

    if z >= 0:
        return 1

    else:
        return 0


# 2. ESTRUCTURA DEL PERCEPTRÓN

def perceptron(X, W, b):

    # Producto punto o combinación lineal
    Z = np.dot(X, W) + b

    # Función de activación
    salida = funcion_escalon(Z)

    return Z, salida


# -------------------------------------------
# PARTE 1 - EJEMPLO DEL CRÉDITO
# -------------------------------------------

print("================================")
print("PARTE 1 - EJEMPLO DEL CRÉDITO")
print("================================")


# Entradas:
# X1 = Ingresos
# X2 = Deudas

entradas_credito = np.array([
    50,
    20
])


# Pesos dados por el ejercicio

pesos_credito = np.array([
    0.8,
    -0.5
])


# Sesgo

sesgo_credito = -10


# Inferencia

Z_credito, salida_credito = perceptron(
    entradas_credito,
    pesos_credito,
    sesgo_credito
)


print("Entradas:", entradas_credito)

print("Pesos:", pesos_credito)

print("Sesgo:", sesgo_credito)

print("Valor Z:", Z_credito)

print("Salida:", salida_credito)


if salida_credito == 1:

    print("Resultado: CRÉDITO APROBADO")

else:

    print("Resultado: CRÉDITO RECHAZADO")


# -------------------------------------------
# PARTE 2 - COMPUERTA AND
# -------------------------------------------

print("\n================================")
print("PARTE 2 - COMPUERTA AND")
print("================================")


# Pesos de la compuerta AND

pesos_and = np.array([
    0.5,
    0.5
])


# Sesgo de AND

sesgo_and = -0.8


# Todas las combinaciones posibles

entradas_logicas = [

    np.array([0, 0]),

    np.array([0, 1]),

    np.array([1, 0]),

    np.array([1, 1])

]


for entrada in entradas_logicas:

    Z, salida = perceptron(
        entrada,
        pesos_and,
        sesgo_and
    )

    print(
        "Entrada:",
        entrada,
        "Z:",
        round(Z, 2),
        "Salida:",
        salida
    )


# -------------------------------------------
# PARTE 3 - COMPUERTA OR
# -------------------------------------------

print("\n================================")
print("PARTE 3 - COMPUERTA OR")
print("================================")


# Se conservan los pesos

pesos_or = np.array([
    0.5,
    0.5
])


# Se modifica el sesgo

sesgo_or = -0.5


for entrada in entradas_logicas:

    Z, salida = perceptron(
        entrada,
        pesos_or,
        sesgo_or
    )

    print(
        "Entrada:",
        entrada,
        "Z:",
        round(Z, 2),
        "Salida:",
        salida
    )


# -------------------------------------------
# RESULTADO FINAL
# -------------------------------------------

print("\n================================")
print("RESULTADO FINAL")
print("================================")


print("\nValores utilizados para AND:")

print(
    "Pesos:",
    pesos_and
)

print(
    "Sesgo:",
    sesgo_and
)


print("\nValores encontrados para OR:")

print(
    "Pesos:",
    pesos_or
)

print(
    "Sesgo:",
    sesgo_or
)


print("\nTabla esperada de OR:")

print("[0, 0] -> 0")

print("[0, 1] -> 1")

print("[1, 0] -> 1")

print("[1, 1] -> 1")
