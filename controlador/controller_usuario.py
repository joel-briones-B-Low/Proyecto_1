from flask import request
from respuestas.respuesta_error import respuestaError
from DAO.usuario_dao import loginDao, eliminarDao, getDao 


def loginContro(data,usu, pas):
    if data.method == 'POST':
        return loginDao(usu,pas)
    else:
        respuestaError('Error de Metodos')
        
def eliminarContro(id):
    return eliminarDao(id)

def getContro():
    return getDao()