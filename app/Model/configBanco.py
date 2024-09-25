import sqlite3
import os

def CriarBancoDados():
    # Caminho completo para o arquivo database.db dentro da pasta 'database'
    db_path = os.path.join('app/database', 'database.db')

    # Criar a conexão com o SQLite (o arquivo será criado automaticamente se não existir)
    conn = sqlite3.connect(db_path)

    conn.execute('''CREATE TABLE IF NOT EXISTS Usuario (
                    CPF INTEGER PRIMARY KEY AUTOINCREMENT,  
                    nome TEXT NOT NULL, 
                    idade INTEGER, 
                    email TEXT UNIQUE)''')

    # Não esqueça de fechar a conexão quando terminar
    conn.close()

def conexao():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '../database', 'database.db')
    con = sqlite3.connect(DB_PATH)
    return con