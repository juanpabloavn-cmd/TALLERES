# TALLER DE LABORATORIO
# CLASIFICADOR UNIVERSAL KNN


import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# 1. DATASET DE ENTRENAMIENTO
# Columnas: Edad, Salario, Numero_Hijos

X_entrenamiento = np.array([
    [20, 30, 0],
    [40, 50, 2],
    [35, 45, 1],
    [25, 32, 0],
    [45, 55, 3],
    [30, 40, 1],
    [50, 60, 2],
    [28, 35, 0],
    [42, 52, 2],
    [38, 48, 1]
])


# Etiquetas:
# 0 = NO COMPRA
# 1 = COMPRA

Y_entrenamiento = np.array([
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    0,
    1,
    1
])


# 2. NUEVO CLIENTE

nuevo_cliente = np.array([
    [33, 42, 1]
])


# 3. MODELO KNN CON K = 1

modelo_k1 = KNeighborsClassifier(
    n_neighbors=1
)

modelo_k1.fit(
    X_entrenamiento,
    Y_entrenamiento
)

prediccion_k1 = modelo_k1.predict(
    nuevo_cliente
)


print("RESULTADO CON K = 1")

print(
    "Clase predicha:",
    prediccion_k1[0]
)

if prediccion_k1[0] == 1:
    print("El cliente COMPRA")
else:
    print("El cliente NO COMPRA")


# 4. MODELO KNN CON K = 5

modelo_k5 = KNeighborsClassifier(
    n_neighbors=5
)

modelo_k5.fit(
    X_entrenamiento,
    Y_entrenamiento
)

prediccion_k5 = modelo_k5.predict(
    nuevo_cliente
)


print("\nRESULTADO CON K = 5")

print(
    "Clase predicha:",
    prediccion_k5[0]
)

if prediccion_k5[0] == 1:
    print("El cliente COMPRA")
else:
    print("El cliente NO COMPRA")