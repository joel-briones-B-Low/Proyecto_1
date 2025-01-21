from flask import Blueprint, request
from bada.Conexion import *
from decoradores.decorador_cors import corsPublico
from respuestas.respuesta_error import respuestaError
from respuestas.respuesta_get import respuestaGet
from CQRS.usuario_cqrs import verificarDato
from controlador.controller_usuario import loginContro

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

    
    data = request
    datos = data.get_json()
    verificarDato(datos)

    usuario = datos.get('usuario')
    contrasenia = datos.get('contrasenia')

    verificarDato(usuario, contrasenia)
    
    
    peticion = loginContro(data=data,usu=usuario, pas=contrasenia)
    
    
    
    """
    esto lo que evita es una inyeccion de sql al hacer parametros seguros
    """

    return respuestaGet(obj='USUARIO', datos=peticion)
