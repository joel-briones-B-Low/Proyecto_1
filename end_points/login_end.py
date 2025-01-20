from flask import Blueprint, request, jsonify
from bada.Conexion import *
from decoradores.decorador_cors import *

InicioSesion = Blueprint('login', __name__)


@InicioSesion.route('/login', methods=['POST'])
@corsPublico
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasenia = data.get('contrasenia')

    cursor = mysql.connection.cursor()
    peticion = f"SELECT * FROM usuario WHERE nombreusuario= '{usuario}' AND contrasenia = '{contrasenia}'"
    cursor.execute(peticion)
    datos = cursor.fetchall()
    cursor.close()

    print(datos)

    return jsonify(datos)    
