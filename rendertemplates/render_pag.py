
"""_summary_:
este Archivo renderiza templates en login
"""

from flask import render_template

def render_login():
    return render_template('login.html')

def render_vul():
    return render_template('vulnerable.html')

def render_usu():
    return render_template('usuario.html')
