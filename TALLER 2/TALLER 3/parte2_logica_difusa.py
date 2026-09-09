# TALLER DE LABORATORIO
# LÓGICA DIFUSA COMERCIAL


# 1. FUNCIÓN DE MEMBRESÍA TRIANGULAR

def membresia_triangular(x, a, b, c):

    # Caso especial para cuando el valor está en el punto máximo
    if x == b:
        return 1.0

    # Fuera del rango del triángulo
    if x <= a or x >= c:
        return 0.0

    # Lado ascendente del triángulo
    elif a < x < b:
        return (x - a) / (b - a)

    # Lado descendente del triángulo
    elif b < x < c:
        return (c - x) / (c - b)

    return 0.0


# 2. AÑOS DE EXPERIENCIA DE LOS CONDUCTORES

conductores = [3, 6, 12]


# 3. EVALUACIÓN DE LOS CONDUCTORES

for experiencia in conductores:

    grado_novato = membresia_triangular(
        experiencia, 0, 0, 5
    )

    grado_intermedio = membresia_triangular(
        experiencia, 2, 5, 8
    )

    grado_experto = membresia_triangular(
        experiencia, 5, 10, 20
    )


    # Se guardan los grados de membresía

    categorias = {
        "Novato": grado_novato,
        "Intermedio": grado_intermedio,
        "Experto": grado_experto
    }


    # Se busca la categoría con mayor grado de membresía

    mejor_categoria = max(
        categorias,
        key=categorias.get
    )


    # 4. RESULTADOS

    print("\nConductor con", experiencia, "años de experiencia")

    print(
        "Grado Novato:",
        round(grado_novato, 2)
    )

    print(
        "Grado Intermedio:",
        round(grado_intermedio, 2)
    )

    print(
        "Grado Experto:",
        round(grado_experto, 2)
    )

    print(
        "Categoría principal:",
        mejor_categoria
    )