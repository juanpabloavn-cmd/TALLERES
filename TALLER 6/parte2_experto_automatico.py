# TALLER DE LABORATORIO FINAL
# EL EXPERTO AUTOMÁTICO


from sklearn.tree import DecisionTreeClassifier, export_text
import numpy as np


# 1. DATASET DE ENTRENAMIENTO

# Columnas:
# Edad, Horas_Online, Compras_Previas

X = np.array([
    [22, 2, 0],
    [25, 5, 1],
    [28, 6, 2],
    [35, 3, 0],
    [40, 7, 3],
    [45, 6, 2],
    [50, 2, 0],
    [30, 8, 4],
    [27, 7, 3],
    [55, 1, 0],
    [38, 5, 2],
    [42, 4, 1]
])


# Etiquetas:
# 1 = Hizo clic en el anuncio
# 0 = Ignoró el anuncio

Y = np.array([
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    1,
    0
])


# 2. ENTRENAMIENTO DEL ÁRBOL DE DECISIÓN

arbol = DecisionTreeClassifier(
    max_depth=3,
    random_state=0
)

arbol.fit(X, Y)


# 3. EXTRACCIÓN DE LAS REGLAS

nombres_variables = [
    "Edad",
    "Horas_Online",
    "Compras_Previas"
]

reglas_texto = export_text(
    arbol,
    feature_names=nombres_variables
)


# 4. RESULTADO

print("BASE DE REGLAS GENERADA AUTOMÁTICAMENTE:\n")

print(reglas_texto)