from flask import request, redirect, url_for, jsonify
from bada.Conexion import db
from modelos.usuario import Usuario

def loginDao(usu, pas):
    usuario = Usuario.query.filter_by(nombreUsuario=usu, contrasenia=pas).first()
    if usuario:
        return usuario.respuesta()
    else: return None
    
def eliminarDao(id):
    usuario = Usuario.query.filter_by(idUsuario=id).first()
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    else:
        return None
    
def getDao():
    usuarios = Usuario.query.all()
    return [usuario.usuario_to_dict() for usuario in usuarios]  