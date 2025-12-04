from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
from types import SimpleNamespace
import requests

load_dotenv()

from models.firebase import (
    initialize_firebase,
    obtener_historial_usuario,
    guardar_sesion_rutina,
)
from viewmodels.rutinas_vm import crear_usuario_desde_form, obtener_rutinas_para_usuario

from collections import defaultdict
from datetime import datetime
from models.firebase import (
    initialize_firebase,
    obtener_historial_usuario,
    guardar_sesion_rutina,
    obtener_usuario_desde_firebase,   
)

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

initialize_firebase()


@app.route("/")
def index():
    return redirect(url_for("encuesta"))


@app.route("/Encuesta", methods=["GET", "POST"])
def encuesta():
    if request.method == "POST":
        usuario = crear_usuario_desde_form(request.form)
        session["usuario_actual"] = usuario.nombre
        return redirect(url_for("rutina"))

    return render_template("Encuesta.html")


@app.route("/Rutina", methods=["GET", "POST"])
def rutina():
    nombre = session.get("usuario_actual")

    if not nombre:
        flash("Completa la encuesta primero.", "warning")
        return redirect(url_for("encuesta"))

    if request.method == "POST":
        deporte = request.form.get("deporte")
        tipo_sesion = request.form.get("tipo_sesion")
        titulo = request.form.get("titulo")
        duracion = request.form.get("duracion")

        peso_str = request.form.get("peso", "").strip()
        try:
            peso_actual = int(peso_str) if peso_str else None
        except:
            peso_actual = None

        rutina_obj = SimpleNamespace(
            deporte=deporte,
            tipo_sesion=tipo_sesion,
            titulo=titulo,
            duracion=duracion
        )

        guardar_sesion_rutina(nombre, rutina_obj, peso_actual)
        flash("Rutina registrada en tu historial de progreso.", "success")
        return redirect(url_for("historial"))

    data = obtener_rutinas_para_usuario(nombre)

    return render_template(
        "Rutina.html",
        rutinas=data["rutinas"],
        deporte=data["deporte"],
        nivel=data["nivel"],
        complicacion=data["complicacion"]
    )


@app.route("/Historial")
def historial():
    nombre = session.get("usuario_actual")
    if not nombre:
        flash("Completa la encuesta primero para generar tu historial.", "warning")
        return redirect(url_for("encuesta"))

    sesiones = obtener_historial_usuario(nombre)

    fechas_peso = []
    pesos = []

    minutos_por_dia = defaultdict(int)
    rutinas_por_dia = defaultdict(int)

    for s in sesiones:
        fecha_str = s.get("fecha", "")
        if not fecha_str:
            continue

        try:
            fecha = datetime.fromisoformat(fecha_str)
            fecha_dia = fecha.strftime("%Y-%m-%d")
        except Exception:
            fecha_dia = fecha_str[:10]

        peso = s.get("peso")
        if peso is not None:
            fechas_peso.append(fecha_dia)
            pesos.append(peso)

        try:
            minutos_por_dia[fecha_dia] += int(s.get("minutos", 0))
        except:
            pass

        rutinas_por_dia[fecha_dia] += 1

    fechas_tiempo = sorted(minutos_por_dia.keys())
    minutos_diarios = [minutos_por_dia[f] for f in fechas_tiempo]

    fechas_rutinas = sorted(rutinas_por_dia.keys())
    rutinas_diarias = [rutinas_por_dia[f] for f in fechas_rutinas]

    return render_template(
        "Historial.html",
        historial=sesiones,
        fechas_peso=fechas_peso,
        pesos=pesos,
        fechas_tiempo=fechas_tiempo,
        minutos_diarios=minutos_diarios,
        fechas_rutinas=fechas_rutinas,
        rutinas_diarias=rutinas_diarias
    )


@app.route("/Usuario")
def usuario():
    nombre = session.get("usuario_actual")
    if not nombre:
        flash("Completa la encuesta primero para ver tu perfil.", "warning")
        return redirect(url_for("encuesta"))

    data = obtener_usuario_desde_firebase(nombre)
    if not data:
        flash("No se encontró información del usuario.", "warning")
        return redirect(url_for("encuesta"))

    return render_template("Usuario.html", usuario=data)


@app.route("/Alarmas")
def alarmas():
    return render_template("Alarmas.html")


@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    if not user_msg:
        return {"reply": "No recibí ningún mensaje."}

    LM_URL = "http://192.168.68.131:1234/v1/chat/completions"

    payload = {
        "model": "qwen2.5-7b-instruct-1m",
        "messages": [
            {
                "role": "system",
                "content": """Actúa como un entrenador personal experto en ejercicio, rutinas, fuerza, movilidad, estiramientos, calentamientos y nutrición deportiva.
Responde con mensajes cortos, directos y solo con lo esencial.

Si la pregunta no es sobre ejercicio, deporte o entrenamiento, responde únicamente:
"Solo puedo ayudarte con temas de ejercicio y entrenamiento."

No uses emojis. Sé conciso y profesional."""
            },
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.4,
        "max_tokens": 150
    }

    try:
        response = requests.post(LM_URL, json=payload)
        res = response.json()

        reply = res["choices"][0]["message"]["content"]
        return {"reply": reply}

    except Exception as e:
        return {"reply": f"Error al conectar con LM Studio: {e}"}


if __name__ == "__main__":
    app.run(debug=True)
