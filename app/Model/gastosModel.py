from database import conexao
import sqlite3

def criar_tabela_gastos():
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                valor REAL NOT NULL,
                categoria_id INTEGER,
                FOREIGN KEY (categoria_id) REFERENCES categorias (id)
            )
        """)
        con.commit()
    except Exception as e:
        print(f"Erro ao criar tabela gastos: {str(e)}")
    finally:
        con.close()

def adicionar_gasto(data, valor, categoria_id):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO gastos (data, valor, categoria_id) VALUES (?, ?, ?)", (data, valor, categoria_id))
        con.commit()
        return "Gasto adicionado com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao adicionar gasto: {str(e)}"
    finally:
        con.close()

def listar_gastos():
    con = conexao()
    con.row_factory = sqlite3.Row
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM gastos")
        return cur.fetchall()
    except Exception as e:
        print(f"Erro ao listar gastos: {str(e)}")
    finally:
        con.close()

def atualizar_gasto(id, data, valor, categoria_id):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("""
            UPDATE gastos 
            SET data = ?, valor = ?, categoria_id = ?
            WHERE id = ?
        """, (data, valor, categoria_id, id))
        con.commit()
        return "Gasto atualizado com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao atualizar gasto: {str(e)}"
    finally:
        con.close()

def deletar_gasto(id):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM gastos WHERE id = ?", (id,))
        con.commit()
        return "Gasto deletado com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao deletar gasto: {str(e)}"
    finally:
        con.close()
