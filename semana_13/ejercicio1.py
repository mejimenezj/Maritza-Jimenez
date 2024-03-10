def calcular_temperatura_promedio(temperaturas):
    # Inicializar una lista para almacenar los promedios de temperatura de cada ciudad
    promedios = []

    # Iterar sobre cada ciudad en los datos de temperaturas
    for ciudad in temperaturas:
        # Inicializar la suma total de temperaturas y el total de días para cada ciudad
        suma_temperaturas = 0
        total_dias = 0

        # Iterar sobre cada semana en la ciudad
        for semana in ciudad:
            # Iterar sobre cada día en la semana
            for dia in semana:
                # Sumar la temperatura de cada día a la suma total de temperaturas
                suma_temperaturas += dia['temp']
                # Incrementar el total de días
                total_dias += 1

        # Calcular el promedio de temperatura para la ciudad actual
        promedio_ciudad = suma_temperaturas / total_dias

        # Agregar el promedio de temperatura de la ciudad a la lista de promedios
        promedios.append(promedio_ciudad)

    # Devolver la lista de promedios de temperatura de cada ciudad
    return promedios


temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 28}
        ]

    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ]

    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ]

    ]

]
promedios_ciudades = calcular_temperatura_promedio(temperaturas)
# Imprimir los resultados
for i, promedio in enumerate(promedios_ciudades):
    print(f"Temperatura promedio de la Ciudad {i + 1}: {promedio:.2f}°C")

# Pruebas de la función en la ciudad 1
print("PRUEBAS")

temperaturas_ciudad_1 = [  # Ciudad 1
    [  # Semana 1
        {"day": "Lunes", "temp": 25},
        {"day": "Martes", "temp": 26},
        {"day": "Miércoles", "temp": 24},
        {"day": "Jueves", "temp": 27},
        {"day": "Viernes", "temp": 26},
        {"day": "Sábado", "temp": 28},
        {"day": "Domingo", "temp": 25}
    ],
    [  # Semana 2
        {"day": "Lunes", "temp": 26},
        {"day": "Martes", "temp": 27},
        {"day": "Miércoles", "temp": 26},
        {"day": "Jueves", "temp": 28},
        {"day": "Viernes", "temp": 25},
        {"day": "Sábado", "temp": 29},
        {"day": "Domingo", "temp": 27}
    ],
    [  # Semana 3
        {"day": "Lunes", "temp": 24},
        {"day": "Martes", "temp": 25},
        {"day": "Miércoles", "temp": 26},
        {"day": "Jueves", "temp": 27},
        {"day": "Viernes", "temp": 28},
        {"day": "Sábado", "temp": 25},
        {"day": "Domingo", "temp": 26}
    ],
    [  # Semana 4
        {"day": "Lunes", "temp": 27},
        {"day": "Martes", "temp": 28},
        {"day": "Miércoles", "temp": 25},
        {"day": "Jueves", "temp": 26},
        {"day": "Viernes", "temp": 27},
        {"day": "Sábado", "temp": 26},
        {"day": "Domingo", "temp": 28}
    ]

]
# Calculamos el promedio manualmente
suma_manual = sum(dia['temp'] for semana in temperaturas_ciudad_1 for dia in semana)
total_dias = len(temperaturas_ciudad_1) * 7  # 4 semanas * 7 días/semana
promedio_manual = suma_manual / total_dias

# Calculamos el promedio usando la función
promedio_funcion = calcular_temperatura_promedio([temperaturas_ciudad_1])[0]

# los resultados
print("Promedio calculado manualmente:", promedio_manual)
print("Promedio calculado con la función:", promedio_funcion)
if (promedio_manual == promedio_funcion):
    print("Prueba correcta")
else:
    print("Prueba fallida")