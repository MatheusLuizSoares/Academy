from app import app
from flask import render_template
from app.forms import Cadastro



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/registro', methods=['GET'])
def registro():
    return render_template("registro.html")

# @app.route('/registro', methods=['POST'])
# def registro():
#     # cadastro = Cadastro()
#     # nome = Cadastro.nome.date
#     # email = Cadastro.email.date
#     # senha = Cadastro.senha.date

#     return render_template('cadastro.html', cadastro = cadastro)



@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/financeiro')
def financeiro():
    return render_template("financeiro.html")