from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Criação do db:
# No terminal, iniciar flask shell
# Comando: db.create_all() para criar o database conforme definido em user.py
# Comando: db.session.commit() para subir efetivar a modificação/criação no banco de dados