from app import db


class TblCadastro(db.Model):  #tbl_cadastro
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128), nullable=False)
    senha = db.Column(db.String(128), nullable=False)


class TblLogin(db.Model):  # tbl_login
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    senha = db.Column(db.String(128), nullable=False)


class TblAulas(db.Model):  # tbl_aulas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    aula = db.Column(db.String(128), nullable=False)
    horario = db.Column(db.Time, nullable=True)



def __repr__(self):
    return "Criando o Cadastro de usuário"
