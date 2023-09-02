from app import app
from flask import render_template, request, flash, redirect
from app.forms import Registro
from app.models import TblCadastro
from app import db



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/registro', methods = ["GET"])
def registro():
    registro = Registro()
    novo_cadastro = TblCadastro()
    nome = registro.nome.data
    email = registro.email.data
    senha = registro.senha.data

    #identificar porque os valores abaixo estão sendo atribuidos como none **
    if nome != 0 and email != 0 and senha != 0:
        flash("Usuário cadastrado com sucesso!")
        novo_cadastro.nome = nome
        novo_cadastro.email = email
        novo_cadastro.senha = senha
        redirect('index.html')

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