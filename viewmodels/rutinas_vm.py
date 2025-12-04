REGLAS_COMPLICACIONES = {
    "fatiga extrema": {
        # Quitamos max_duracion para no eliminar rutinas largas,
        # la reducción de duración la haremos en adaptar_rutina_intensidad.
        "evitar_palabras": ["salto", "explos", "sprint", "velocidad"]
    },
    "golpes de calor": {
        "max_duracion": 30,
        "evitar_palabras": ["sprint", "velocidad", "carrera", "cardio"]
    },
    "complicaciones respiratorias": {
        "evitar_palabras": ["caminadora", "cardio", "crol", "respiración"],
    },
    "complicaciones cardiovasculares": {
        "evitar_palabras": ["velocidad", "sprint", "carrera", "saltos"],
        "nivel_max": "Intermedio"
    }
    # ... resto igual
}

import re
from models.rutina_base import Rutina
from models.usuario import Usuario
from models.firebase import guardar_usuario_en_firebase, obtener_usuario_desde_firebase
from models.rutinas_futbol import RUTINAS_FUTBOL
from models.rutinas_baloncesto import RUTINAS_BALONCESTO
from models.rutinas_natacion import RUTINAS_NATACION
from models.rutinas_tenis import RUTINAS_TENIS
from static.img.imagenes_ejercicios import IMAGENES_EJERCICIOS, GIF_POR_DEFECTO

# Unificar todas las rutinas
TODAS_LAS_RUTINAS = (
    RUTINAS_FUTBOL +
    RUTINAS_BALONCESTO +
    RUTINAS_NATACION +
    RUTINAS_TENIS
)

EJERCICIOS_ALTERNATIVOS = {
    "sentadilla": "sentadilla guiada",
    "zancada": "extensión de cuádriceps",
    "saltos": "elevaciones de gemelos",
    "sprints": "caminadora",
    "caminadora": "bicicleta",
    "crol": "flotación dorsal",
    "press militar": "elevaciones laterales",
    "peso muerto": "extensión de cuádriceps"
}

def mapear_experiencia(valor):
    if valor == "a":
        return "Principiante"
    if valor == "b":
        return "Intermedio"
    if valor == "c":
        return "Avanzado"
    return valor

def obtener_flags(complicacion, discapacidad=""):
    texto = (complicacion + " " + discapacidad).lower()
    flags = []

    if "inferior" in texto:
        flags.append("discapacidad_inferior")
    if "superior" in texto:
        flags.append("discapacidad_superior")
    if "motriz" in texto:
        flags.append("discapacidad_motriz")
    if "articular" in texto or "osteoarticular" in texto:
        flags.append("lesion_articular")

    if "cardio" in texto:
        flags.append("cardiaco")
    if "respira" in texto or "asma" in texto:
        flags.append("respiratorio")

    return flags

def crear_usuario_desde_form(form):
    nombre = form["usuario"]
    contrasena = form["contrasena"]
    genero = form["genero"]
    deporte = form["deporte"]

    # Edad
    edad_str = form.get("edad", "").strip()
    try:
        edad = int(edad_str)
    except:
        edad = 0

    nivel = mapear_experiencia(form["experiencia"])

    # Complicación médica general
    complicacion = form.get("tipoComplicacion", "") if form["complicaciones"] == "si" else ""

    # NUEVAS VARIABLES
    frecuencia = form.get("frecuencia", "")
    duracion = form.get("duracion", "")
    calentamiento = form.get("calentamiento", "")
    discapacidad = form.get("tipoDiscapacidad", "")

    usuario = Usuario(
        nombre=nombre,
        contrasena=contrasena,
        genero=genero,
        deporte=deporte,
        edad=edad,
        nivel=nivel,
        complicacion=complicacion,
        frecuencia=frecuencia,
        duracion=duracion,
        calentamiento=calentamiento,
        discapacidad=discapacidad
    )

    guardar_usuario_en_firebase(usuario)
    return usuario

def asignar_gif_a_pasos(rutina: Rutina):
    nuevos_pasos = []

    for paso in rutina.pasos:
        if isinstance(paso, dict):
            nombre = paso.get("nombre", "").strip()
            detalle = paso.get("detalle", "").strip()
        else:
            # Separar nombre y detalle si es un string plano tipo "Ejercicio: 3x12"
            if ":" in paso:
                nombre, detalle = map(str.strip, paso.split(":", 1))
            else:
                nombre = paso.strip()
                detalle = ""

        clave_encontrada = None
        paso_lower = nombre.lower()

        for clave in IMAGENES_EJERCICIOS.keys():
            if clave in paso_lower:
                clave_encontrada = clave
                break

        gif = IMAGENES_EJERCICIOS.get(clave_encontrada, GIF_POR_DEFECTO)

        nuevos_pasos.append({
            "nombre": nombre,
            "detalle": detalle,
            "gif": gif
        })

    rutina.pasos = nuevos_pasos
    return rutina

def reemplazar_ejercicios_peligrosos(rutina: Rutina):
    nuevos_pasos = []

    for paso in rutina.pasos:
        nombre_original = paso["nombre"].lower()
        reemplazo_final = paso["nombre"]

        for clave, reemplazo in EJERCICIOS_ALTERNATIVOS.items():
            if clave in nombre_original:
                reemplazo_final = reemplazo.capitalize()
                break

        nuevos_pasos.append({
            "nombre": reemplazo_final,
            "detalle": paso["detalle"],
            "gif": paso.get("gif", "")
        })

    rutina.pasos = nuevos_pasos
    return rutina

def asignar_imagen_a_rutina(rutina: Rutina):
    texto = (rutina.titulo + " " + " ".join(p['nombre'] for p in rutina.pasos)).lower()
    for clave, archivo in IMAGENES_EJERCICIOS.items():
        if clave in texto:
            rutina.imagen = archivo
            return rutina
    rutina.imagen = GIF_POR_DEFECTO
    return rutina

def adaptar_rutina_intensidad(rutina: Rutina, complicacion: str):
    c = complicacion.lower()
    nueva = rutina  # seguimos trabajando sobre el mismo objeto

    # adaptar duración
    try:
        minutos = int(nueva.duracion.split()[0])
    except:
        minutos = 30

    if "fatiga extrema" in c:
        minutos = max(15, minutos - 15)

        if "(versión ligera)" not in nueva.titulo:
            nueva.titulo += " (versión ligera)"

        texto_extra = " Esta versión reduce la carga para manejar la fatiga."
        if texto_extra.strip() not in nueva.descripcion:
            nueva.descripcion += texto_extra

    elif "golpes de calor" in c:
        minutos = max(15, minutos - 10)

        texto_extra = " Realiza esta rutina en horarios frescos y con buena hidratación."
        if texto_extra.strip() not in nueva.descripcion:
            nueva.descripcion += texto_extra

    nueva.duracion = f"{minutos} min"
    return nueva

def adaptar_pasos_intensidad(rutina: Rutina, complicacion: str):
    """
    Reduce automáticamente la carga de los pasos (repeticiones, tiempo, distancia)
    cuando hay fatiga extrema o golpes de calor.
    """
    c = complicacion.lower()
    if "fatiga extrema" not in c and "golpes de calor" not in c:
        return rutina

    nuevos_pasos = []

    for paso in rutina.pasos:
        detalle = paso.get("detalle", "")
        if not detalle:
            nuevos_pasos.append(paso)
            continue

        # Función interna para reducir números
        def reducir(match):
            n = int(match.group())
            # No tocar números muy pequeños (1,2,3,4)
            if n <= 4:
                return match.group()
            # Reducir a un ~60% de la carga original
            nuevo = max(1, int(round(n * 0.6)))
            return str(nuevo)

        detalle_nuevo = re.sub(r"\d+", reducir, detalle)

        paso_mod = paso.copy()
        paso_mod["detalle"] = detalle_nuevo
        nuevos_pasos.append(paso_mod)

    rutina.pasos = nuevos_pasos
    return rutina

def obtener_rutinas_para_usuario(nombre_usuario: str):
    data = obtener_usuario_desde_firebase(nombre_usuario)
    if not data:
        return {"deporte": "", "nivel": "", "complicacion": "", "rutinas": []}

    deporte = data["deporte"]
    nivel = data["nivel"]
    complicacion = data.get("complicacion", "")
    frecuencia = data.get("frecuencia", "")
    duracion_pref = data.get("duracion", "")
    calentamiento = data.get("calentamiento", "")
    discapacidad = data.get("discapacidad", "")

    user_flags = obtener_flags(complicacion, discapacidad)

    # 1. Rutinas base por deporte y nivel + flags (discapacidad, etc.)
    rutinas_usuario = [
        r for r in TODAS_LAS_RUTINAS
        if r.deporte == deporte
        and r.nivel == nivel
        and all(f not in r.evitar_flags for f in user_flags)
    ]

    # 2. REGLAS SEGÚN COMPLICACIÓN
    reglas = REGLAS_COMPLICACIONES.get(complicacion.lower(), {})

    # Evitar tipos de sesión (si alguna complicación lo define)
    if "evitar_tipos" in reglas:
        rutinas_usuario = [
            r for r in rutinas_usuario
            if r.tipo_sesion.lower() not in reglas["evitar_tipos"]
        ]

    # Evitar palabras en título / descripción
    if "evitar_palabras" in reglas:
        nuevas = []
        for r in rutinas_usuario:
            texto = (r.titulo + " " + r.descripcion).lower()
            if not any(p in texto for p in reglas["evitar_palabras"]):
                nuevas.append(r)
        rutinas_usuario = nuevas

    # Duración máxima por complicación
    if "max_duracion" in reglas:
        def minutos(rt):
            return int(rt.duracion.split()[0])
        rutinas_usuario = [
            r for r in rutinas_usuario
            if minutos(r) <= reglas["max_duracion"]
        ]

    # Nivel máximo permitido
    if reglas.get("nivel_max") == "Intermedio":
        rutinas_usuario = [
            r for r in rutinas_usuario
            if r.nivel in ["Principiante", "Intermedio"]
        ]

    # 3. Adaptación por FRECUENCIA
    if frecuencia == "a":   # <1/semana
        rutinas_usuario = [r for r in rutinas_usuario if r.nivel != "Avanzado"]

    # 4. Adaptación por DURACIÓN ELEGIDA (preferencia del usuario)
    if duracion_pref:
        limites = {
            "a": 20,
            "b": 40,
            "c": 60,
            "d": 200
        }
        limite = limites.get(duracion_pref, 200)

        def minutos(rt):
            return int(rt.duracion.split()[0])

        rutinas_usuario = [
            r for r in rutinas_usuario
            if minutos(r) <= limite
        ]

    # 5. Adaptación por CALENTAMIENTO
    if calentamiento == "a":  # 0–5 min → evitar cosas muy explosivas
        rutinas_usuario = [
            r for r in rutinas_usuario
            if "explos" not in r.descripcion.lower()
            and "salto" not in r.titulo.lower()
        ]

    # ⭐ PLAN B: si después de todo esto no quedó nada, usar rutinas estándar
    if not rutinas_usuario:
        rutinas_usuario = [
            r for r in TODAS_LAS_RUTINAS
            if r.deporte == deporte and r.nivel == nivel
        ]
    # 6. Adaptar intensidad (duración / mensajes) según complicación
    rutinas_adaptadas = []
    for r in rutinas_usuario:
        r = adaptar_rutina_intensidad(r, complicacion)
        r = adaptar_pasos_intensidad(r, complicacion)
        rutinas_adaptadas.append(r)
    # 7. Añadir gifs, reemplazos y una imagen principal
    rutinas_con_imagen = []
    for r in rutinas_adaptadas:
        r = asignar_gif_a_pasos(r)
        r = reemplazar_ejercicios_peligrosos(r)
        r = asignar_imagen_a_rutina(r)
        rutinas_con_imagen.append(r)
    return {
        "deporte": deporte,
        "nivel": nivel,
        "complicacion": complicacion,
        "rutinas": rutinas_con_imagen
    }
