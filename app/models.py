from app import db

class TblCadastro(db.Model): #tbl_cadastro
     id = db.column(db.integer, primary_key = True)
     nome = db.column(db.String(128), nullable = False)
     email = db.column(db.String(128), nullable = False)
     senha = db.column(db.String(128), nullable = False)

