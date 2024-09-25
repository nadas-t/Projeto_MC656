from database import conexao
import sqlite3

def criar_tabela_categorias():
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE
            )
        """)
        con.commit()
    except Exception as e:
        print(f"Erro ao criar tabela categorias: {str(e)}")
    finally:
        con.close()

def adicionar_categoria(nome):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))
        con.commit()
        return "Categoria adicionada com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao adicionar categoria: {str(e)}"
    finally:
        con.close()

def listar_categorias():
    con = conexao()
    con.row_factory = sqlite3.Row
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM categorias")
        return cur.fetchall()
    except Exception as e:
        print(f"Erro ao listar categorias: {str(e)}")
    finally:
        con.close()

def atualizar_categoria(id, nome):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("""
            UPDATE categorias 
            SET nome = ?
            WHERE id = ?
        """, (nome, id))
        con.commit()
        return "Categoria atualizada com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao atualizar categoria: {str(e)}"
    finally:
        con.close()

def deletar_categoria(id):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM categorias WHERE id = ?", (id,))
        con.commit()
        return "Categoria deletada com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao deletar categoria: {str(e)}"
    finally:
        con.close()
