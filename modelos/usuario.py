from bada.Conexion import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    idUsuario = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(50), unique=True, nullable=False)
    contrasenia = db.Column(db.String(50), nullable=False)

    def __str__(self):
        usuario = {
            'nombre': self.nombreUsuario,
            'contrasenia': self.contrasenia
        }
        return usuario

    def respuesta(self):
        usuario = {
            'id': self.idUsuario,
            'nombre': self.nombreUsuario,
            'contrasenia': self.contrasenia
        }
        return usuario

    def usuario_to_dict(self):
        return {
        'idUsuario': self.idUsuario,
        'nombreUsuario': self.nombreUsuario,
        'contrasenia': self.contrasenia,  
        }
    
