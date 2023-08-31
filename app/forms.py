from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Cadastro(FlaskForm):
    nome = StringField('nome', validators = [DataRequired()] )
    email = EmailField
    password = PasswordField
    