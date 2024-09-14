from app.Model.usuarioModel import listar, verifica, adicionar, atualizar, deletar, obter_dados_usuario

def listarUsuario():
    rows = listar()
    return rows

def verificarUsuario(CPF):
    resultado = obter_dados_usuario(CPF)
    return resultado

def adicionarUsuario(CPF, nome, idade, email):
    resultado = adicionar(CPF, nome, idade, email)
    return resultado

def atualizarUsuario(CPF, nome, idade, email):
    resultado = atualizar(CPF, nome, idade, email)
    return resultado

def deletarUsuario(CPF):
    resultado = deletar(CPF)
    return resultado

def feature1Logica(valor1, valor2, valor3, valor4):
    return valor1

def feature2Logica(valor1, valor2, valor3, valor4):
    return valor1