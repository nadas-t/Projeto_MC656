from app.Model.usuarioModel import *

def listarUsuario():
    rows = listar()
    return rows

def verificarUsuario(CPF):
    resultado = obter_dados_usuario(CPF)
    return resultado

def adicionarUsuario(CPF, nome, idade, email, senha):
    resultado = adicionar(CPF, nome, idade, email, senha)
    return resultado

def atualizarUsuario(CPF, nome, idade, email, senha):
    resultado = atualizar(CPF, nome, idade, email, senha)
    return resultado

def atualizarSenha(email, senha, senha1, senha2):
    resultado = ""

    if(senha1 != senha2):
        resultado = "Senhas novas não coincidem!"
    
    elif(senha1 == ""):
        resultado = "A senha nova não pode ser vázia!"

    else:

        result_list = verificaLogin(email, senha)  # Presume-se que verificarUsuario retorna uma lista
    
        if result_list:
            row = result_list[0]
            resultado = modificarSenha(row['CPF'], senha1)
        else:
            resultado = "Senha incorreta!"

    return resultado

def deletarUsuario(CPF):
    resultado = deletar(CPF)
    return resultado

def login(email, senha):
    resultado = verificaLogin(email, senha)
    return resultado

def adicionarUsuario(CPF, nome, idade, email, senha1, senha2):
    
    if (senha1 == senha2):
        resultado = adicionar(CPF, nome, idade, email, senha1)
    else:
        resultado = "As senhas não são iguais!"

    return resultado