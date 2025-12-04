from models.rutina_base import Rutina

RUTINAS_TENIS = [

    # PRINCIPIANTE - GIMNASIO
    Rutina(
        deporte="Tenis",
        nivel="Principiante",
        tipo_sesion="Gimnasio",
        titulo="Introducción al entrenamiento físico",
        descripcion="Rutina básica para mejorar fuerza y movilidad.",
        duracion="30 min",
        pasos=[
            {"nombre": "Caminadora", "detalle": "5 minutos"},
            {"nombre": "Sentadilla guiada", "detalle": "3x10"},
            {"nombre": "Press militar", "detalle": "3x10"},
            {"nombre": "Curl femoral", "detalle": "3x12"},
            {"nombre": "Plancha", "detalle": "3x20s"}
        ]
    ),

    # PRINCIPIANTE - AIRE LIBRE
    Rutina(
        deporte="Tenis",
        nivel="Principiante",
        tipo_sesion="Aire libre",
        titulo="Control de raqueta y desplazamiento",
        descripcion="Ejercicios técnicos básicos en cancha.",
        duracion="40 min",
        pasos=[
            {"nombre": "Desplazamientos laterales", "detalle": "4x10m"},
            {"nombre": "Golpes de derecha en estático", "detalle": "3x10"},
            {"nombre": "Golpes de revés en estático", "detalle": "3x10"},
            {"nombre": "Mini rally en media cancha", "detalle": "5 minutos"}
        ]
    ),

    # INTERMEDIO - GIMNASIO
    Rutina(
        deporte="Tenis",
        nivel="Intermedio",
        tipo_sesion="Gimnasio",
        titulo="Fuerza y coordinación para tenistas",
        descripcion="Enfocado en tren inferior, core y hombros.",
        duracion="45 min",
        pasos=[
            {"nombre": "Peso muerto", "detalle": "3x8"},
            {"nombre": "Remo con barra", "detalle": "3x10"},
            {"nombre": "Elevaciones laterales", "detalle": "3x12"},
            {"nombre": "Plank leg raises", "detalle": "3x15"},
            {"nombre": "Elevaciones de gemelos", "detalle": "3x20"}
        ]
    ),

    # INTERMEDIO - AIRE LIBRE
    Rutina(
        deporte="Tenis",
        nivel="Intermedio",
        tipo_sesion="Aire libre",
        titulo="Golpes en movimiento y consistencia",
        descripcion="Trabajo técnico y de desplazamiento.",
        duracion="50 min",
        pasos=[
            {"nombre": "Desplazamientos con golpe de derecha", "detalle": "3x10"},
            {"nombre": "Desplazamientos con revés", "detalle": "3x10"},
            {"nombre": "Rally cruzado controlado", "detalle": "5 minutos"},
            {"nombre": "Golpes con entrenador aleatorio", "detalle": "10 minutos"}
        ]
    ),

    # AVANZADO - GIMNASIO
    Rutina(
        deporte="Tenis",
        nivel="Avanzado",
        tipo_sesion="Gimnasio",
        titulo="Potencia explosiva y estabilidad",
        descripcion="Rutina exigente con énfasis funcional.",
        duracion="50 min",
        pasos=[
            {"nombre": "Sentadilla con barra", "detalle": "4x6"},
            {"nombre": "Fondos en paralelas", "detalle": "3x10"},
            {"nombre": "Rotaciones con cable", "detalle": "3x15"},
            {"nombre": "Peso muerto rumano", "detalle": "3x8"},
            {"nombre": "Plancha lateral", "detalle": "3x30s"}
        ]
    ),

    # AVANZADO - AIRE LIBRE
    Rutina(
        deporte="Tenis",
        nivel="Avanzado",
        tipo_sesion="Aire libre",
        titulo="Simulación de partido y potencia",
        descripcion="Trabajo de alta intensidad para situaciones reales.",
        duracion="60 min",
        pasos=[
            {"nombre": "Sprints cortos con frenado", "detalle": "6x10m"},
            {"nombre": "Rally profundo", "detalle": "5 minutos"},
            {"nombre": "Juego de puntos", "detalle": "20 minutos"},
            {"nombre": "Servicio + primer golpe", "detalle": "4x8"}
        ]
    ),
]
