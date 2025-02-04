"""from flask import Blueprint, request, jsonify
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
        return jsonify({'error': str(e)}), 500"""
        
        
        
from flask import Blueprint, request, jsonify
from decoradores.decorador_cors import *
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse


vulnerable = Blueprint('vulnerable', __name__)
lugar = os.getcwd()

def logs(cliente, lugar):
    os.system('cls')
    print(lugar)
    archivo = open('logs.txt', 'a')
    archivo.write(f'cliente: {cliente} __ lugar:  {lugar}')
    archivo.close()

@vulnerable.route('/consulta', methods=['POST'])
def peticion():
    try:
        url = request.json.get('url')
        
        response = requests.get(url)
        """
        lo primero que podemos hacer para no evidenciar los js ni nada por el estilo de archivos clave es
        solo retornar lo queno sos importe
        lo segundo que podemos hacer es restringir los dominios:
        lo otro que podemos hacer es monitoreos        
        """
        cliente = request.remote_addr
        lugar = url
        logs(cliente, lugar)
        print()
        dominios = ['https://joelBriones.com']
        if url not in dominios:
            return jsonify({'error': 'El dominio no es permitido'}), 403
        if response.status_code == 200:
            texto = response.text
            convertido = BeautifulSoup(texto, 'html.parser')
            contenido = convertido.body
            texto = contenido.decode_contents()
            
            texto = texto[:-47]
            return jsonify({'data': texto, 'status_code': response.status_code}), 200
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