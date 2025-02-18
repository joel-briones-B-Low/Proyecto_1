"""
Este archivo es el principal de mi aplicacion    
"""

from flask  import Flask
from rendertemplates.render_pag import *
from end_points.usuario_end import UsuarioEnd
from end_points.vulnerable import vulnerable
from bada.Conexion import iniciarConexion, db

# cors publico
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

iniciarConexion(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """_summary_:
    esta duncion devuelve el template de login
    """
    return render_login()

@app.route('/vulnerable')
def vulnerable_pag():
    return render_vul()

@app.route('/usuarios')
def usuarios():
    return render_usu()

app.register_blueprint(UsuarioEnd)
app.register_blueprint(vulnerable)


if __name__ == '__main__':
    app.run(port=8080, debug=True)