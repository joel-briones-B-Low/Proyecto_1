from flask import Blueprint, request, jsonify
from decoradores.decorador_cors import *
import requests
import os
from urllib.parse import urlparse


vulnerable = Blueprint('vulnerable', __name__)


@vulnerable.route('/consulta', methods=['POST'])
@corsPublico
def peticion():
    try:
        url = request.json.get('url')
        
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify({'data': response.text, 'status_code': response.status_code}), 200
        else:
            return jsonify({'error': 'Error al hacer la solicitud al servidor remoto'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


@vulnerable.route('/consulta/archivo', methods=['POST'])
def leer():
    try:
        url = request.json.get('url')
        parsed_url = urlparse(url)  # Analiza la URL
        nombre = parsed_url.path.lstrip("/")  # Elimina el prefijo /
        archivo = os.path.join(os.getcwd(), 'static/js', nombre + '.js')  # Ruta al archivo

        if os.path.exists(archivo):
            with open(archivo, 'r') as file:
                contenido = file.read()
            return jsonify({'data': contenido, 'status_code': 200}), 200
        else:
            return jsonify({'error': 'El archivo no existe'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500