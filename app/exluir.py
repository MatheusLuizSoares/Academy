from app import db  
from app import TblCadastro  # Importe o modelo de dados

# Substitua com o email e senha do registro que você deseja excluir
email_a_excluir = 'josimar.wow@gmail.com'
senha_a_excluir = 'vhceb3is'

# Consulte o registro a ser excluído
registro_a_excluir = TblCadastro.query.filter_by(email=email_a_excluir, senha=senha_a_excluir).first()

if registro_a_excluir:
    db.session.delete(registro_a_excluir)
    db.session.commit()
    print("Registro excluído com sucesso!")
else:
    print("Registro não encontrado.")