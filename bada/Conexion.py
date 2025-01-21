#from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()  

def iniciarConexion(app):
    """
    Configura y inicializa la conexión con la base de datos.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/proyecto_1'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)