import sqlite3
import os

DB_PATH = os.path.join("app", "database", "database.db")


def gerar_tabela_de_categorias(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """
    )


def gerar_tabela_de_gastos(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                valor REAL NOT NULL,
                categoria_id INTEGER,
                FOREIGN KEY (categoria_id) REFERENCES categorias (id)
            )
        """
    )


def gerar_tabela_de_usuarios(cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Usuario (
                        CPF INTEGER PRIMARY KEY AUTOINCREMENT,  
                        nome TEXT NOT NULL, 
                        idade INTEGER NOT NULL, 
                        email TEXT UNIQUE NOT NULL,
                        senha TEXT NOT NULL)"""
    )


def CriarBancoDados():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        gerar_tabela_de_categorias(cursor)
        gerar_tabela_de_gastos(cursor)
        gerar_tabela_de_usuarios(cursor)

        conn.commit()
        return "Tabelas setadas com sucesso"
    except Exception as e:
        if conn:
            conn.rollback()
        return f"Erro ao setar tabelas: {str(e)}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def conexao():
    con = sqlite3.connect(DB_PATH)
    return con
