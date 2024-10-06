import sqlite3
import os
from app.Model.configBancoModel import conexao

def adicionar(CPF, nome, idade, email, senha):
    
    resultado = ""
    try:
        # Connect to SQLite3 database and execute the INSERT
        con = conexao()
        cur = con.cursor()
        cur.execute("INSERT INTO Usuario (CPF, nome, idade, email, senha) VALUES (?,?,?,?,?)",
                     (CPF, nome, idade, email, senha))
        con.commit()
        resultado = "Usuário cadastrado com sucesso!"
    except:
        con.rollback()
        resultado = "Erro ao cadastrar usuário"

    finally:
        con.close()
        # Send the transaction message to result.html
    return resultado

def atualizar(CPF, nome, idade, email, senha):
    resultado = ""

    try:
        # Conectar ao banco de dados
        con = conexao()
        cur = con.cursor()
        # Usar placeholders (?) para evitar SQL Injection
        cur.execute(""" UPDATE Usuario SET nome = ?, idade = ?, email = ?, senha = ?
                WHERE CPF = ?
            """, (nome, idade, email, senha, CPF))

        con.commit()
        resultado = "Usuário atualizado com sucesso!"
    except Exception as e:
        con.rollback()
        resultado = f"Erro ao atualizar usuário! Detalhes: {str(e)}" 
    finally:
        con.close()
        return resultado
    
def modificarSenha(CPF, senha):
    resultado = ""

    try:
        # Conectar ao banco de dados
        con = conexao()
        cur = con.cursor()

        # Usar placeholders (?) para evitar SQL Injection
        cur.execute(""" UPDATE Usuario SET senha = ?
                WHERE CPF = ? 
            """, (senha, CPF))

        con.commit()
        resultado = "Senha atualizada com sucesso!"
    except Exception as e:
        con.rollback()
        resultado = f"Erro ao atulizar a senha usuário! Detalhes: {str(e)}" 
    finally:
        con.close()
        return resultado


def listar():

    con = conexao()    
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Usuario")

    lista = cur.fetchall()
    con.close()
    # Send the results of the SELECT to the list.html page
    return lista

def verifica(CPF):
    con = conexao()
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    # Execute a consulta para verificar a existência do usuário com o ID fornecido
    cur.execute("SELECT 1 FROM Usuario WHERE CPF = ?", (CPF,))
    
    # Fetch one result; if a result is found, user exists
    result = cur.fetchone()
    con.close()
    
    return result

def verificaLogin(email, senha):
    
    con = conexao()    
    con.row_factory = sqlite3.Row

    print(email)
    print(senha)

    cur = con.cursor()
    cur.execute("SELECT * FROM Usuario WHERE email = ? AND senha = ?", (email, senha))

    lista = cur.fetchall()

    con.close()

    print(f"Resultados: {lista}")

    if not lista:
        return None
    
    # Send the results of the SELECT to the list.html page
    return lista

def obter_dados_usuario(CPF):
    
    con = conexao()    
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Usuario WHERE CPF = ?", (CPF,))

    lista = cur.fetchall()
    con.close()

    if not lista:
        return None
    
    # Send the results of the SELECT to the list.html page
    return lista

def deletar(CPF):
    resultado = ""

    try:
        # Conectar ao banco de dados
        con = conexao()
        cur = con.cursor()
        # Usar placeholders (?) para evitar SQL Injection
        cur.execute("DELETE FROM Usuario WHERE CPF = ?", (CPF,))

        con.commit()
        resultado = "Usuário removido com sucesso!"
    except Exception as e:
        con.rollback()
        resultado = f"Erro ao deletar usuário! Detalhes: {str(e)}"
    finally:
        con.close()
        return resultado