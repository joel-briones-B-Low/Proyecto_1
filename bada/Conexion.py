from flask_mysqldb import MySQL

mysql = MySQL()

def iniciarConexion(app):
    """
    Configura y inicializa la conexión con la base de datos.
    """
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'proyecto_1'
    
    mysql.init_app(app)  