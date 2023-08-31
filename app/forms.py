from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Cadastro(FlaskForm):
    nome = StringField('nome', validators = [DataRequired()] )
    email = EmailField('email', validators = [DataRequired()] )
    password = PasswordField('password', validators = [DataRequired()] )
    enviar = SubmitField('enviar')