from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Registro(FlaskForm):
    nome = StringField('nome', validators = [DataRequired()] )
    email = EmailField('email', validators = [DataRequired()] )
    senha = PasswordField('senha', validators = [DataRequired()] )
    enviar = SubmitField('enviar')