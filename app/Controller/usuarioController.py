from app.Model.usuarioModel import *
from flask import request

class UsuariosController:
    @staticmethod
    def adicionarUsuario():
        
        CPF = request.form.get('CPF')
        nome = request.form.get('nome')  
        idade = request.form.get('idade')
        email = request.form.get('email')
        senha1 = request.form.get('senha1')        
        senha2 = request.form.get('senha2')
        
        if senha1 != senha2:
            return "As senhas não coincidem"

        usuario = Usuario(CPF=CPF, nome=nome, idade=idade, email=email, senha=senha1)
        usuario_db = UsuarioDB()
        resultado = usuario_db.adicionar(usuario)
        return resultado
    
    @staticmethod
    def login(email, senha):
        usuario = Usuario(email=email, senha=senha)
        usuario_db = UsuarioDB()
        resultado = usuario_db.verificaLogin(usuario)
        return resultado
    
    @staticmethod
    def atualizarUsuario(CPF, nome, idade, email, senha):
        usuario = Usuario(CPF=CPF, nome=nome, idade=idade, email=email, senha=senha)
        usuario_db = UsuarioDB()
        resultado = usuario_db.atualizar(usuario)
        return resultado
    
    @staticmethod
    def atualizarSenha(email, senha, senha1, senha2):
        resultado = ""

        if(senha1 != senha2):
            resultado = "Senhas novas não coincidem!"
    
        elif(senha1 == ""):
            resultado = "A senha nova não pode ser vázia!"

        else:
            usuario = Usuario(email=email, senha=senha)
            usuario_db = UsuarioDB()
            result_list = usuario_db.verificaLogin(usuario)  # Presume-se que verificarUsuario retorna uma lista
    
            if result_list:
                row = result_list[0]
                usuario = Usuario(CPF=row, senha=senha1)
                resultado = usuario_db.modificarSenha(usuario)
            else:
                resultado = "Senha incorreta!"

        return resultado
    