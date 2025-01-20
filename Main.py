"""
Este archivo es el principal de mi aplicacion    
"""

from flask  import Flask

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port=8080, debug=True)