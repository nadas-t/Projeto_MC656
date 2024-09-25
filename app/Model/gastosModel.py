from app.Model.configBancoModel import conexao
import sqlite3



def adicionar_gasto(data, valor, categoria_id):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)", (data, valor, categoria_id))
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
        cur.execute("SELECT * FROM Gastos")
        return cur.fetchall()
    except Exception as e:
        print(f"Erro ao listar Gastos: {str(e)}")
    finally:
        con.close()

def atualizar_gasto(id, data, valor, categoria_id):
    con = conexao()
    try:
        cur = con.cursor()
        cur.execute("""
            UPDATE Gastos 
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
        cur.execute("DELETE FROM Gastos WHERE id = ?", (id,))
        con.commit()
        return "Gasto deletado com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao deletar gasto: {str(e)}"
    finally:
        con.close()
