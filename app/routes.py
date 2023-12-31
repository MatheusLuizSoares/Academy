from app import app, db, bcrypt
from flask import render_template, request, flash, redirect, session
from app.forms import Registro, LoginForm
from app.models import TblCadastro

 
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/registro', methods=["GET", "POST"])
def registro():
    registro = Registro()
    
    if request.method == "POST" and registro.validate_on_submit(): ## possivel problema validação nao está funcionando
        nome = registro.nome.data
        email = registro.email.data
        senha = registro.senha.data
        b_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        novo_cadastro = TblCadastro(nome=nome, email=email, senha=b_senha)
        db.session.add(novo_cadastro)
        db.session.commit() 

        flash("Usuário cadastrado com sucesso!")
        print(f"Usuário cadastrado: {nome}, {email}, {senha}")  # Mensagem de depuração
        return redirect('/registro')

    return render_template('registro.html', registro=registro)


@app.route('/login', methods=['GET','POST'])
def login():
    login = LoginForm()

    if request.method == 'POST':
        email = login.email.data
        senha = login.senha.data

        # executando a consulta sql para encontrar o usuário pelo e-mail...
        usuario = TblCadastro.query.filter_by(email=email).first()
       

        if usuario and bcrypt.check_password_hash(usuario.senha, senha):
            # Login bem-sucedido    
            session['usuario_id'] = usuario.id # armazenado id na sessao
            flash('Login bem-sucedido!', 'success')
            return redirect('/user')  # redirecionando para a página do usuário após o login
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')

    return render_template('login.html', login=login)


@app.route('/aulas')
def aulas():
    return render_template("aulas.html")

@app.route('/user')
def usuario():
    return render_template("user.html")

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

@app.route('/dados')
def dados():
    usuario = TblCadastro.query.all() #first() query.get(id)

    return render_template("dados.html", usuario = usuario)

@app.route('/dados/<int:id>')
def dadosid(id):
    usuario = TblCadastro.query.get(id) #first() query.get(id)

    return render_template("dados.html", usuario = usuario)

@app.route('/atualizar/<int:id>', methods = ['GET', 'POST'])
def atualizar(id):
    
    usuario = TblCadastro.query.get(id)
    
   
    if request.method == 'POST':
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            nome = request.form.get('name')
            email = request.form.get('email')
            senha = request.form.get('senha')
            print(nome)
            b_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            usuario = TblCadastro(nome=nome, email=email, senha=b_senha)
            db.session.add(usuario)
            db.session.commit() 
            return redirect('/dados')
        return f"Usuario com id = {id} Não existe!"
    return render_template("atualizar.html", usuario = usuario)

@app.route('/deletar/<int:id>', methods = ["GET", 'POST'])
def deletar(id):
    usuario = TblCadastro.query.filter_by(id=id).first()
    if request.method =="POST":
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return redirect('/user')
    
    return render_template("deletar.html")
