from models.rutina_base import Rutina

RUTINAS_NATACION = [

    # PRINCIPIANTE – GIMNASIO
    Rutina(
        deporte="Natacion",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Fortalecimiento básico para nadadores",
        descripcion="Fortalece espalda, hombros y core.",
        duracion="30 min",
        pasos=[
            {"nombre": "Jalón al pecho", "detalle": "3x12"},
            {"nombre": "Remo sentado", "detalle": "3x12"},
            {"nombre": "Rotadores externos con banda", "detalle": "3x15"},
            {"nombre": "Plancha", "detalle": "3x25s"},
            {"nombre": "Estiramiento de dorsales", "detalle": "3 min"},
        ],
        evitar_flags=["discapacidad_superior"]
    ),

    # PRINCIPIANTE – PISCINA
    Rutina(
        deporte="Natacion",
        nivel="Principiante",
        tipo_sesion="Piscina",
        titulo="Bases del estilo crol",
        descripcion="Aprende flotación, respiración y patada.",
        duracion="40 min",
        pasos=[
            {"nombre": "Flotación ventral", "detalle": "3 min"},
            {"nombre": "Patada con tabla", "detalle": "4x25m"},
            {"nombre": "Respiración bilateral", "detalle": "3x25m"},
            {"nombre": "Crol suave", "detalle": "4x25m"},
        ],
        evitar_flags=["respiratorio"]
    ),

    # INTERMEDIO – GIMNASIO
    Rutina(
        deporte="Natacion",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Fuerza y estabilidad del tronco",
        descripcion="Mejora velocidad y técnica.",
        duracion="40 min",
        pasos=[
            {"nombre": "Pull-over con mancuerna", "detalle": "3x12"},
            {"nombre": "Remo de pie cuerda", "detalle": "3x12"},
            {"nombre": "Plancha lateral", "detalle": "3x30s"},
            {"nombre": "Elevaciones frontales", "detalle": "3x12"},
        ]
    ),

    # INTERMEDIO – PISCINA
    Rutina(
        deporte="Natacion",
        nivel="Intermedio",
        tipo_sesion="Piscina",
        titulo="Nado continuo moderado",
        descripcion="Coordina brazada + respiración + patada.",
        duracion="45 min",
        pasos=[
            {"nombre": "Crol suave", "detalle": "2x50m"},
            {"nombre": "Crol técnica", "detalle": "4x25m"},
            {"nombre": "Crol ritmo medio", "detalle": "3x50m"},
            {"nombre": "Patada lateral", "detalle": "4x25m"},
        ],
        evitar_flags=["cardiaco"]
    ),

    # AVANZADO – GIMNASIO
    Rutina(
        deporte="Natacion",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Potencia máxima de brazada",
        descripcion="Ideal para nadadores competitivos.",
        duracion="50 min",
        pasos=[
            {"nombre": "Jalón al pecho", "detalle": "5x6 (pesado)"},
            {"nombre": "Remo con barra", "detalle": "4x6 (pesado)"},
            {"nombre": "Core en polea", "detalle": "4x15"},
            {"nombre": "Rotación explosiva", "detalle": "4x12"},
        ]
    ),

    # AVANZADO – PISCINA
    Rutina(
        deporte="Natacion",
        nivel="Avanzado",
        tipo_sesion="Piscina",
        titulo="Entrenamiento de velocidad",
        descripcion="Máxima velocidad y técnica competitiva.",
        duracion="55 min",
        pasos=[
            {"nombre": "Crol velocidad", "detalle": "6x25m"},
            {"nombre": "Crol rápido", "detalle": "4x50m"},
            {"nombre": "Salidas explosivas", "detalle": "10 reps"},
            {"nombre": "Virajes rápidos", "detalle": "4 rondas"},
        ],
        evitar_flags=["cardiaco"]
    ),
]
