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


@app.route('/registro', methods=["GET", "POST"])
def registro():
    registro = Registro()
    
    if request.method == "POST" and registro.validate_on_submit():
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        novo_cadastro = TblCadastro(nome=nome, email=email, senha=senha)
        session.add(novo_cadastro)
        session.commit() 

        flash("Usuário cadastrado com sucesso!")
        return redirect('index.html')

    return render_template('registro.html', registro=registro)


@app.route('/login')
def login():
    login = LoginForm()

    if login.validate_on_submit():
        email = login.email.data
        senha = login.senha.data

        # Consultar o banco de dados para encontrar o usuário pelo e-mail
        usuario = TblCadastro.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.senha_hash, senha):
            # Login bem-sucedido
            session['usuario_id'] = usuario.id  # Armazene o ID do usuário na sessão
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('user'))  # Redirecione para a página do usuário após o login
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', login=login)
@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/financeiro')
def financeiro():
    return render_template("financeiro.html")

