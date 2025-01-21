from flask import jsonify

def respuestaGet(obj,datos):
    return jsonify({obj: datos})