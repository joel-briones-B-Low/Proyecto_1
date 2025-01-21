from flask import Blueprint, request, jsonify
from bada.Conexion import *
from decoradores.decorador_cors import *
from respuestas.respuesta_error import *
from respuestas.respuesta_get import *

InicioSesion = Blueprint('login', __name__)




@InicioSesion.route('/login', methods=['POST'])
@corsPublico
def login():
    
    """_summary_:
    este tipo de metodo cuenta con una gran problema debido a que puede 
    haber inyeccion de sql
    
    data = request.get_json()
    usuario = data.get('usuario')
    contrasenia = data.get('contrasenia')

    cursor = mysql.connection.cursor()
    peticion = f"SELECT * FROM usuario WHERE nombreusuario= '{usuario}' AND contrasenia = '{contrasenia}'"
    cursor.execute(peticion)
    datos = cursor.fetchall()
    cursor.close()

    print(datos)
    
    // lo coreecto seria hacerlo con parametros seguros:
"""
    data = request.get_json()
    if not data:
        return respuestaError()

    usuario = data.get('usuario')
    contrasenia = data.get('contrasenia')

    if not contrasenia or not usuario:
        return respuestaError()

    cursor = mysql.connection.cursor()
    peticion = "SELECT * FROM usuario WHERE nombreUsuario = %s AND contrasenia = %s"
    cursor.execute(peticion, (usuario, contrasenia))
    datos = cursor.fetchall()
    cursor.close()
    
    """
    esto lo que evita es una inyeccion de sql al hacer parametros seguros
    """

    return respuestaGet(obj='USUARIO', datos=datos)
