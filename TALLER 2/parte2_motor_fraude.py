# TALLER DE LABORATORIO
# MOTOR DE FRAUDE BANCARIO


# 1. BASE DE CONOCIMIENTOS ESTRUCTURADA

hechos = {
    "monto": 7500,
    "pais_extranjero": True
}


# Se evalúa si el monto de la transacción supera los 5000
hechos["monto_alto"] = hechos["monto"] > 5000


reglas = [

    {
        "id": "R1",
        "condiciones": {
            "monto_alto": True
        },
        "conclusion": {
            "transaccion_inusual": True
        }
    },

    {
        "id": "R2",
        "condiciones": {
            "transaccion_inusual": True,
            "pais_extranjero": True
        },
        "conclusion": {
            "bloquear_tarjeta": True
        }
    },

    {
        "id": "R3",
        "condiciones": {
            "bloquear_tarjeta": True
        },
        "conclusion": {
            "alerta_fraude": True
        }
    },

    {
        "id": "R4",
        "condiciones": {
            "alerta_fraude": True
        },
        "conclusion": {
            "revision_manual": True
        }
    }

]


# 2. MOTOR DE INFERENCIA FORWARD CHAINING

nuevos_hechos = True

while nuevos_hechos:

    nuevos_hechos = False

    for regla in reglas:

        # Verifica si todas las condiciones de la regla se cumplen
        condiciones_cumplidas = all(
            hechos.get(clave) == valor
            for clave, valor in regla["condiciones"].items()
        )

        if condiciones_cumplidas:

            for clave, valor in regla["conclusion"].items():

                # Verifica que la conclusión sea un hecho nuevo
                if clave not in hechos:

                    hechos[clave] = valor
                    nuevos_hechos = True

                    print(
                        f"Disparando {regla['id']} -> "
                        f"Nuevo hecho: {clave}={valor}"
                    )


# 3. RESULTADO FINAL

print("\nMemoria final:")
print(hechos) 