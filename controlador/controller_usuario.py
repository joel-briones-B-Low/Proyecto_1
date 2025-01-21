from flask import request
from DAO.usuario_dao import loginDao
from respuestas.respuesta_error import respuestaError


def loginContro(data,usu, pas):
    if data.method == 'POST':
        return loginDao(usu,pas)
    else:
        respuestaError('Error de Metodos')
        
        