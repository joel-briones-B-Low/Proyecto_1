from flask import request, redirect, url_for
from bada.Conexion import db
from modelos.usuario import Usuario

def loginDao(usu, pas):
    usuario = Usuario.query.filter_by(nombreUsuario=usu, contrasenia=pas).first()
    if usuario:
        return usuario.respuesta()
    else: return None
    