from app.Model.configBancoModel import conexao
import sqlite3



def adicionar_gasto(data, valor, categoria_nome):
    con = conexao()
    try:
        cur = con.cursor()
        
        # Verificar se a categoria já existe
        cur.execute("SELECT id FROM Categorias WHERE nome = ?", (categoria_nome,))
        categoria = cur.fetchone()
        
        # Se a categoria não existir, criá-la
        if categoria is None:
            cur.execute("INSERT INTO Categorias (nome) VALUES (?)", (categoria_nome,))
            con.commit()  # Confirma a inserção da nova categoria
            categoria_id = cur.lastrowid  # Pega o id da categoria recém criada
        else:
            categoria_id = categoria['id']  # Pega o id da categoria existente

        # Agora que temos o categoria_id, podemos inserir o gasto
        cur.execute("INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)", (data, valor, categoria_id))
        con.commit()

        return "Gasto adicionado com sucesso!"
    except Exception as e:
        con.rollback()
        return f"Erro ao adicionar gasto: {str(e)}"
    finally:
        con.close()

def obter_gasto_por_id(gasto_id):
    con = conexao()
    con.row_factory = sqlite3.Row
    try:
        cur = con.cursor()
        cur.execute("SELECT Gastos.id, Gastos.data, Gastos.valor, Categorias.nome AS categoria_nome FROM Gastos LEFT JOIN Categorias ON Gastos.categoria_id = Categorias.id WHERE Gastos.id = ?", (gasto_id,))
        return cur.fetchone()  # Retorna apenas um único gasto
    except Exception as e:
        print(f"Erro ao obter gasto: {str(e)}")
    finally:
        con.close()
        
def listar_gastos(gasto_id=None):
    con = conexao()
    con.row_factory = sqlite3.Row
    try:
        cur = con.cursor()
        if gasto_id is not None:
            cur.execute("SELECT * FROM Gastos WHERE id = ?", (gasto_id,))
            return cur.fetchone()  # Retorna apenas um gasto
        else:
            cur.execute("SELECT * FROM Gastos")
            return cur.fetchall()  # Retorna todos os gastos
    except Exception as e:
        print(f"Erro ao listar gastos: {str(e)}")
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

def converte_gasto_horas(gastos, ganho_por_hora):
    for gasto in gastos:
        gasto.valor = gasto.valor /ganho_por_hora
    return gastos
    