from flask import jsonify

def respuestaError():
    return jsonify({"error": "Error en la solicitud"}), 400
