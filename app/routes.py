from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    nome = "Matheus"
    dados = "SENAC"
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/registro')
def registro():
    return render_template("registro.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/financeiro')
def financeiro():
    return render_template("financeiro.html")