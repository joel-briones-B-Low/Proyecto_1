from flask import jsonify

def respuestaError(mensaje):
    return jsonify({"error": mensaje}), 400

