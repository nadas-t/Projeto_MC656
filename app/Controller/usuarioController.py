from app.Model.usuarioModel import *
from flask import request
import re

class UsuariosController:
    @staticmethod
    def adicionarUsuario():
        
        CPF = request.form.get('CPF')
        nome = request.form.get('nome')  
        idade = request.form.get('idade')
        email = request.form.get('email')
        senha1 = request.form.get('senha1')        
        senha2 = request.form.get('senha2')
        
        
         # Restrições para a senha
        resultado,erros=UsuariosController.validar_senha(senha1)
        if not resultado:
            return "\n".join(erros)
        
        if senha1 != senha2:
            return "As senhas não coincidem"

        usuario = Usuario(CPF=CPF, nome=nome, idade=idade, email=email, senha=senha1)
        usuario_db = UsuarioDB()
        resultado = usuario_db.adicionar(usuario)
        return resultado
    
    @staticmethod
    def validar_senha(senha):
        erros=[]
        if len(senha) < 8:
            erros.append("Sua senha deve ter 8 ou mais caracteres.")
            
        if not re.search(r'[A-Z]', senha):
            erros.append("Sua senha deve ter ao menos 1 letra maiúscula.")
            
        if not re.search(r'[0-9]', senha):
            erros.append("Sua senha deve ter ao menos 1 número.")
            
        if not re.search(r'[\W_]', senha):  # O padrão \W corresponde a qualquer caractere não alfanumérico (exceto _)
            erros.append("Sua senha deve ter ao menos 1 caractere especial.")
    
        if erros:
            return False, erros
        
        # Se não houver erros, retorna True
        return True, []
    
    @staticmethod
    def login(email, senha):
        usuario = Usuario(email=email, senha=senha)
        usuario_db = UsuarioDB()
        resultado = usuario_db.verificaLogin(usuario)
        return resultado
    
    @staticmethod
    def atualizarUsuario(CPF, nome, idade, email, senha, salario, limite, horas_trabalho):
        usuario = Usuario(CPF=CPF, nome=nome, idade=idade, email=email, senha=senha, 
                          salario=salario, limite=limite, horas_trabalho=horas_trabalho)
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
    
    @staticmethod
    def adicionarSalario(CPF, salario, horas_trabalho):
        usuario = Usuario(CPF=CPF, salario=salario, horas_trabalho=horas_trabalho)
        usuario_db = UsuarioDB()
        resultado = usuario_db.adicionarSalario(usuario)
        return resultado
    