"""
API en Python (Flask) - Persona 1
Seminario de Sistemas 1 - Hoja de Trabajo 2

Endpoints obligatorios:
  - GET /check -> HTTP 200 (health check para el balanceador de carga)
  - GET /info  -> JSON con la informacion de la instancia/API

Antes de desplegar en Azure, correr localmente y probar ambos endpoints.
"""

from flask import Flask, jsonify

app = Flask(__name__)

NOMBRE_INSTANCIA = "Maquina 1 - Api Python"
CURSO = "Seminario de Sistemas 1 A"
GRUPO = "Grupo 4"


@app.route("/check", methods=["GET"])
def check():
    # Health check: solo debe responder 200 OK
    return "OK", 200


@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "Instancia": NOMBRE_INSTANCIA,
        "Curso": CURSO,
        "Grupo": GRUPO
    }), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API Python activa. Ver /check y /info"}), 200


if __name__ == "__main__":
    # host 0.0.0.0 para que sea accesible desde fuera de la VM (Azure)
    app.run(host="0.0.0.0", port=5000)
