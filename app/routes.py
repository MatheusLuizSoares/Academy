from app import app
from flask import render_template
from app.forms import Registro



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# @app.route('/registro', methods=['GET'])
# def registro():
#     return render_template("registro.html")

@app.route('/registro')
def registro():
    registro = Registro()
    nome = registro.nome.data
    email = registro.email.data
    senha = registro.senha.data
    return render_template('registro.html', registro = registro)



@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/financeiro')
def financeiro():
    return render_template("financeiro.html")