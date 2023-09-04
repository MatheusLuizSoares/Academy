from app import app
from flask import render_template, request, flash, redirect, url_for
from app.forms import Registro, LoginForm
from app.models import TblCadastro
from app import db
from werkzeug.security import check_password_hash

session = db.session


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/registro', methods=["GET"])
def registro():
    registro = Registro()
    
    if request.method == "POST" and registro.validate_on_submit(): ## possivel problema validação nao está funcionando
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        novo_cadastro = TblCadastro(nome=nome, email=email, senha=senha)
        session.add(novo_cadastro)
        session.commit() 

        flash("Usuário cadastrado com sucesso!")
        print(f"Usuário cadastrado: {nome}, {email}, {senha}")  # Mensagem de depuração
        return redirect(url_for('index'))

    return render_template('registro.html', registro=registro)


@app.route('/login', methods=['GET','POST'])
def login():
    login = LoginForm()

    # if request.method == 'GET':
    #     email = request.form['email']
    #     senha = request.form['senha']

    #     # executando a consulta sql para encontrar o usuário pelo e-mail...
    #     usuario = TblCadastro.query.filter_by(email=email).first()
       

    #     if usuario and check_password_hash(usuario.senha_hash, senha):
    #         # Login bem-sucedido
    #         session['usuario_id'] = usuario.id # armazenado id na sessao
    #         flash('Login bem-sucedido!', 'success')
    #         return redirect(url_for('user'))  # redirecionando para a página do usuário após o login
    #     else:
    #         flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', login=login)


@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/financeiro')
def financeiro():
    return render_template("financeiro.html")
