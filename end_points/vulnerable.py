from flask import Blueprint, request, jsonify
from decoradores.decorador_cors import *
import requests

vulnerable = Blueprint('vulnerable', __name__)
@vulnerable.route('/consulta', methods=['POST'])
@corsPublico
def peticion():
    try:
        url = request.json.get('url')
        
        # Realiza la solicitud GET a la URL
        response = requests.get(url)

        # Verifica si la respuesta fue exitosa
        if response.status_code == 200:
            return jsonify({'data': response.text, 'status_code': response.status_code}), 200
        else:
            return jsonify({'error': 'Error al hacer la solicitud al servidor remoto'}), response.status_code

    except requests.exceptions.RequestException as e:
        # Maneja cualquier error de la solicitud
        return jsonify({'error': str(e)}), 500
