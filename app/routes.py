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
        return redirect(url_for('index'))

    return render_template('registro.html', registro=registro)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = LoginForm()

    if login.validate_on_submit():
        email = login.email.data
        senha = login.senha.data

        # Conectar ao banco de dados
        conn = db.connect()
        cursor = conn.cursor()

        # Execute a consulta SQL para encontrar o usuário pelo e-mail
        cursor.execute("SELECT * FROM TblCadastro WHERE email=?", (email,))
        usuario = cursor.fetchone()

        # Feche a conexão com o banco de dados
        conn.close()

        if usuario and check_password_hash(usuario[2], senha):
            # Login bem-sucedido
            session['usuario_id'] = usuario[0]  # armazenado id na sessao
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('user'))  # redirecionando para a página do usuário após o login
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', login=login)


@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/financeiro')
def financeiro():
    return render_template("financeiro.html")
