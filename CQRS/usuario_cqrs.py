from respuestas.respuesta_error import *

def verificarDato(*args):
    for elemento in args:
        if not elemento:
            return respuestaError('Elementos vacios')
    
    
        
    
