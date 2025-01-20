from flask_cors import cross_origin

def corsPublico(funcion):
    @cross_origin()  
    def envoltura(*args, **kwargs):
        return funcion(*args, **kwargs)
    return envoltura
