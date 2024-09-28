import sqlite3
import os

def CriarBancoDados():
    conn = None  # Inicializa a conexão como None
    cursor = None  # Inicializa o cursor como None
    try:    
        # Caminho completo para o arquivo database.db dentro da pasta 'database'
        db_path = os.path.join('app/database', 'database.db')

        # Criar a conexão com o SQLite (o arquivo será criado automaticamente se não existir)
        conn = sqlite3.connect(db_path)

        # Criar um cursor
        cursor = conn.cursor()

        # Criar a tabela de categorias primeiro
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)

        # Criar a tabela de Gastos depois, que depende da tabela categorias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                valor REAL NOT NULL,
                categoria_id INTEGER,
                FOREIGN KEY (categoria_id) REFERENCES categorias (id)
            )
        """)

        # Criar a tabela de Usuário
        cursor.execute('''CREATE TABLE IF NOT EXISTS Usuario (
                        CPF INTEGER PRIMARY KEY AUTOINCREMENT,  
                        nome TEXT NOT NULL, 
                        idade INTEGER, 
                        email TEXT UNIQUE)''')

        # Confirmar as alterações
        conn.commit()
        return "Tabelas setadas com sucesso"
    except Exception as e:
        if conn:  # Verifica se a conexão foi criada antes de tentar fazer rollback
            conn.rollback()
        return f"Erro ao setar tabelas: {str(e)}"
    finally:
        if cursor:  # Fecha o cursor apenas se ele foi criado
            cursor.close()
        if conn:  # Fecha a conexão apenas se ela foi criada
            conn.close()


def conexao():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '../database', 'database.db')
    con = sqlite3.connect(DB_PATH)
    return con