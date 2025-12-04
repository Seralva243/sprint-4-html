import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db
from models.usuario import Usuario
from datetime import datetime

load_dotenv()

_firebase_initialized = False


# =========================
#  SESIONES / HISTORIAL
# =========================

def guardar_sesion_rutina(nombre_usuario: str, rutina, peso_actual: int | None = None):
    """
    Guarda en /Historial/<usuario> un registro de rutina realizada,
    con fecha, deporte, tipo de sesión, título de rutina, minutos y peso (opcional).
    """
    initialize_firebase()
    ref = db.reference("/Historial").child(nombre_usuario)

    # intentar leer minutos desde rutina.duracion ("25 min")
    try:
        minutos = int(str(rutina.duracion).split()[0])
    except Exception:
        minutos = 0

    data = {
        "fecha": datetime.now().isoformat(),
        "deporte": getattr(rutina, "deporte", ""),
        "tipo_sesion": getattr(rutina, "tipo_sesion", ""),
        "rutina": getattr(rutina, "titulo", ""),
        "minutos": minutos,
        "peso": peso_actual
    }

    ref.push(data)
    return data


def obtener_historial_usuario(nombre_usuario: str):
    """
    Devuelve una lista de sesiones de rutina del usuario, ordenadas por fecha.
    Cada sesión incluye un campo 'id' con la clave en Firebase.
    """
    initialize_firebase()
    ref = db.reference("/Historial").child(nombre_usuario)
    data = ref.get() or {}

    sesiones = []
    for key, value in data.items():
        value["id"] = key
        sesiones.append(value)

    sesiones.sort(key=lambda x: x.get("fecha", ""))
    return sesiones


# =========================
#  INICIALIZACIÓN FIREBASE
# =========================

def initialize_firebase():
    global _firebase_initialized
    if _firebase_initialized:
        return

    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    db_url = os.getenv("DATABASE_URL")

    if not cred_path:
        raise RuntimeError("Falta GOOGLE_APPLICATION_CREDENTIALS en .env")
    if not db_url:
        raise RuntimeError("Falta DATABASE_URL en .env")

    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"databaseURL": db_url})

    _firebase_initialized = True


# =========================
#  USUARIOS
# =========================

def guardar_usuario_en_firebase(usuario: Usuario):
    """
    Guarda/actualiza los datos del usuario en /Usuarios/<nombre>.
    Incluye los campos nuevos: frecuencia, duracion, calentamiento, discapacidad.
    """
    initialize_firebase()

    ref = db.reference("/Usuarios")

    data = {
        "nombre": usuario.nombre,
        "contrasena": usuario.contrasena,
        "genero": usuario.genero,
        "deporte": usuario.deporte,
        "edad": usuario.edad,
        "nivel": usuario.nivel,
        "complicacion": getattr(usuario, "complicacion", ""),
        "frecuencia": getattr(usuario, "frecuencia", ""),
        "duracion": getattr(usuario, "duracion", ""),
        "calentamiento": getattr(usuario, "calentamiento", ""),
        "discapacidad": getattr(usuario, "discapacidad", "")
    }

    ref.child(usuario.nombre).set(data)
    return data


def obtener_usuario_desde_firebase(nombre: str):
    """
    Devuelve el diccionario de datos del usuario almacenado en Firebase,
    o None si no existe.
    """
    initialize_firebase()
    ref = db.reference("/Usuarios")
    return ref.child(nombre).get()
