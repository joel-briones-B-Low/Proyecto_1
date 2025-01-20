"""
Este archivo es el principal de mi aplicacion    
"""

from flask  import Flask
from rendertemplates.render_login import *
from end_points.login_end import InicioSesion
from bada.Conexion import *

app = Flask(__name__)

iniciarConexion(app)

@app.route('/')
def index():
    """_summary_:
    esta duncion devuelve el template de login
    """
    return render_login()

app.register_blueprint(InicioSesion)

if __name__ == '__main__':
    app.run(port=8080, debug=True)