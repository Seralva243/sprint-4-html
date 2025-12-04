from models.rutina_base import Rutina

RUTINAS_FUTBOL = [

    # PRINCIPIANTE - GIMNASIO
    Rutina(
        deporte="Futbol",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Base de fuerza para futbolistas",
        descripcion="Entrenamiento para mejorar fuerza general y prevenir lesiones.",
        duracion="30 min",
        pasos=[
            {"nombre": "Prensa de pierna", "detalle": "3x12"},
            {"nombre": "Curl femoral", "detalle": "3x12"},
            {"nombre": "Elevaciones de gemelos", "detalle": "3x15"},
            {"nombre": "Plancha", "detalle": "3x30s"}
        ],
        evitar_flags=["lesion_articular"]
    ),

    # PRINCIPIANTE - AIRE LIBRE
    Rutina(
        deporte="Futbol",
        nivel="Principiante",
        tipo_sesion="Campo",
        titulo="Técnica básica con balón",
        descripcion="Mejora conducción, pase y recepción.",
        duracion="40 min",
        pasos=[
            {"nombre": "Conducción recta", "detalle": "4x20m"},
            {"nombre": "Zig-zag entre conos", "detalle": "3 repeticiones"},
            {"nombre": "Pase a la pared", "detalle": "3x10"},
            {"nombre": "Tiros a portería", "detalle": "10 intentos"}
        ]
    ),

    # INTERMEDIO - GIMNASIO
    Rutina(
        deporte="Futbol",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Fuerza explosiva",
        descripcion="Desarrolla potencia en tren inferior.",
        duracion="40 min",
        pasos=[
            {"nombre": "Sentadilla con barra", "detalle": "4x8"},
            {"nombre": "Zancadas", "detalle": "3x12"},
            {"nombre": "Peso muerto", "detalle": "3x10"},
            {"nombre": "Core en polea", "detalle": "3x15"}
        ]
    ),

    # INTERMEDIO - AIRE LIBRE
    Rutina(
        deporte="Futbol",
        nivel="Intermedio",
        tipo_sesion="Campo",
        titulo="Velocidad y control",
        descripcion="Mejora capacidad aeróbica y técnica con balón.",
        duracion="45 min",
        pasos=[
            {"nombre": "Sprints", "detalle": "6x20m"},
            {"nombre": "Zig-zag entre conos", "detalle": "4 repeticiones"},
            {"nombre": "Pases en movimiento", "detalle": "3x12"},
            {"nombre": "Tiros a portería", "detalle": "15 intentos"}
        ]
    ),

    # AVANZADO - GIMNASIO
    Rutina(
        deporte="Futbol",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Potencia y core avanzado",
        descripcion="Entrenamiento de fuerza máxima y core funcional.",
        duracion="50 min",
        pasos=[
            {"nombre": "Peso muerto", "detalle": "5x5"},
            {"nombre": "Sentadilla con barra", "detalle": "5x5"},
            {"nombre": "Plank leg raises", "detalle": "3x20s por pierna"},
            {"nombre": "Elevaciones frontales", "detalle": "3x12"}
        ]
    ),

    # AVANZADO - AIRE LIBRE
    Rutina(
        deporte="Futbol",
        nivel="Avanzado",
        tipo_sesion="Campo",
        titulo="Alta intensidad táctica",
        descripcion="Simula situaciones reales de juego.",
        duracion="55 min",
        pasos=[
            {"nombre": "Sprints", "detalle": "8x20m"},
            {"nombre": "Zig-zag entre conos", "detalle": "6 repeticiones"},
            {"nombre": "Pase y desmarque", "detalle": "4x8"},
            {"nombre": "Tiros a portería", "detalle": "20 intentos"}
        ]
    ),
]
