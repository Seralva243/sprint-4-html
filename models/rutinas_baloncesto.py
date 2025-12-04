from models.rutina_base import Rutina

RUTINAS_BALONCESTO = [
    # PRINCIPIANTE – GIMNASIO
    Rutina(
        deporte="Baloncesto",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Fuerza básica para baloncesto",
        descripcion="Primeros pasos de fuerza para salto y bote.",
        duracion="30 min",
        pasos=[
            {"nombre": "Caminadora", "detalle": "5 min"},
            {"nombre": "Prensa", "detalle": "3x12"},
            {"nombre": "Extensión cuádriceps", "detalle": "3x12"},
            {"nombre": "Press militar", "detalle": "3x10"},
            {"nombre": "Remo sentado", "detalle": "3x12"},
        ]
    ),

    # PRINCIPIANTE – AIRE LIBRE
    Rutina(
        deporte="Baloncesto",
        nivel="Principiante",
        tipo_sesion="Aire libre",
        titulo="Fundamentos de bote",
        descripcion="Coordinación básica y tiro suave.",
        duracion="35 min",
        pasos=[
            {"nombre": "Bote mano dominante", "detalle": "2 min"},
            {"nombre": "Bote no dominante", "detalle": "2 min"},
            {"nombre": "Entradas", "detalle": "10 por lado"},
            {"nombre": "Tiros cortos", "detalle": "20"},
        ]
    ),

    # INTERMEDIO – GIMNASIO
    Rutina(
        deporte="Baloncesto",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Potencia de salto",
        descripcion="Fuerza + pliometría.",
        duracion="40 min",
        pasos=[
            {"nombre": "Sentadilla", "detalle": "4x8"},
            {"nombre": "Saltos verticales", "detalle": "3x10"},
            {"nombre": "Zancadas laterales", "detalle": "3x12"},
            {"nombre": "Press militar", "detalle": "3x10"},
        ]
    ),

    # INTERMEDIO – AIRE LIBRE
    Rutina(
        deporte="Baloncesto",
        nivel="Intermedio",
        tipo_sesion="Aire libre",
        titulo="Desplazamientos avanzados",
        descripcion="Agilidad y tiros en movimiento.",
        duracion="45 min",
        pasos=[
            {"nombre": "Desplazamientos laterales", "detalle": "3 rondas"},
            {"nombre": "Tiros en suspensión", "detalle": "25"},
            {"nombre": "1 vs 1 suave", "detalle": "5-7 min"},
        ]
    ),

    # AVANZADO – GIMNASIO
    Rutina(
        deporte="Baloncesto",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Explosividad profesional",
        descripcion="Salto y fuerza máxima.",
        duracion="50 min",
        pasos=[
            {"nombre": "Sentadilla pesada", "detalle": "5x5"},
            {"nombre": "Pliometría avanzada", "detalle": "4x10"},
            {"nombre": "Press militar pesado", "detalle": "4x6"},
        ]
    ),

    # AVANZADO – AIRE LIBRE
    Rutina(
        deporte="Baloncesto",
        nivel="Avanzado",
        tipo_sesion="Aire libre",
        titulo="Simulación de juego real",
        descripcion="Alta intensidad ofensiva y defensiva.",
        duracion="55 min",
        pasos=[
            {"nombre": "Bote explosivo", "detalle": ""},
            {"nombre": "Tiros en movimiento", "detalle": "25"},
            {"nombre": "Partido reducido", "detalle": "8-10 min"},
        ]
    ),
]
