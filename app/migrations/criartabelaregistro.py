import sqlite3
db = sqlite3.connect("../db.sqlite")

cursor = db.cursor()

cursor.execute('create table registro(aluno_nome varchar, aluno_email varchar, aluno_senha varchar)')