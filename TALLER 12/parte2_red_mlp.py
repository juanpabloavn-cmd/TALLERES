# TALLER 12
# REDES NEURONALES DENSAS O MULTICAPA

import numpy as np


# 1. FUNCIÓN DE ACTIVACIÓN SIGMOIDE

def sigmoide(x):

    return 1 / (1 + np.exp(-x))


# ==================================================
# PARTE 1 - UN SOLO CLIENTE
# ==================================================

print("========================================")
print("PARTE 1 - PROCESAMIENTO DE UN CLIENTE")
print("========================================")


# Entrada X:
# Edad, Ingresos, Deuda

X = np.array([
    0.5,
    0.8,
    0.2
])


# ------------------------------------------
# CAPA OCULTA
# 3 entradas x 4 neuronas
# ------------------------------------------

W1 = np.array([
    [0.1, 0.2, -0.3, 0.4],
    [-0.5, 0.6, 0.7, -0.8],
    [0.9, -0.1, 0.2, 0.3]
])


b1 = np.array([
    0.1,
    -0.2,
    0.3,
    -0.4
])


# Combinación lineal de la capa oculta

Z1 = np.dot(X, W1) + b1


# Activación de la capa oculta

A1 = sigmoide(Z1)


print("\nEntrada X:")
print(X)

print("\nValores Z1 de la capa oculta:")
print(np.round(Z1, 4))

print("\nValores A1 después de Sigmoide:")
print(np.round(A1, 4))


# ------------------------------------------
# CAPA DE SALIDA
# 4 neuronas ocultas x 1 salida
# ------------------------------------------

W2 = np.array([
    0.5,
    -0.6,
    0.7,
    0.8
])


b2 = np.array([
    -0.1
])


# Combinación lineal de salida

Z2 = np.dot(A1, W2) + b2


# Activación final

salida_final = sigmoide(Z2)


print("\nPredicción final del cliente:")

print(
    np.round(
        salida_final[0],
        4
    )
)


# ==================================================
# PARTE 2 - PROCESAMIENTO DE DOS CLIENTES
# ==================================================

print("\n========================================")
print("PARTE 2 - PROCESAMIENTO POR LOTES")
print("========================================")


# Dos clientes al mismo tiempo

X_lote = np.array([
    [0.5, 0.8, 0.2],
    [0.1, 0.9, 0.9]
])


print("\nMatriz de entrada X:")
print(X_lote)

print(
    "\nDimensión de X:",
    X_lote.shape
)


# ------------------------------------------
# CAPA OCULTA PARA LOS DOS CLIENTES
# ------------------------------------------

Z1_lote = np.dot(
    X_lote,
    W1
) + b1


A1_lote = sigmoide(
    Z1_lote
)


print("\nValores Z1 de los dos clientes:")
print(
    np.round(
        Z1_lote,
        4
    )
)


print("\nValores A1 después de Sigmoide:")
print(
    np.round(
        A1_lote,
        4
    )
)


print(
    "\nDimensión de A1:",
    A1_lote.shape
)


# ------------------------------------------
# CAPA DE SALIDA PARA LOS DOS CLIENTES
# ------------------------------------------

Z2_lote = np.dot(
    A1_lote,
    W2
) + b2


salida_lote = sigmoide(
    Z2_lote
)


print("\nPredicciones finales:")

print(
    np.round(
        salida_lote,
        4
    )
)


# ------------------------------------------
# RESULTADOS INDIVIDUALES
# ------------------------------------------

print("\n========================================")
print("RESULTADOS POR CLIENTE")
print("========================================")


print(
    "Cliente 1:",
    round(
        salida_lote[0],
        4
    )
)


print(
    "Cliente 2:",
    round(
        salida_lote[1],
        4
    )
)


print("\nProcesamiento por lotes completado correctamente.")
