from dataclasses import dataclass
from app.Model.databaseManager import DBTransactionManager, BaseDB

class ErroAoCadastrarUsuario(Exception):
    pass

@dataclass
class Usuario:
    nome: str = None
    email: str = None
    senha: str = None
    idade: int = None
    CPF: int = None  # Alterar para str

    def __post_init__(self):
        pass
    
class UsuarioDB: 
    def __init__(self):
        self._db = BaseDB()

    def adicionar(self, usuario: Usuario):
        with DBTransactionManager() as db_manager:
            db_manager.executar_transacao(
                comando="INSERT INTO Usuario (CPF, nome, idade, email, senha) VALUES (?,?,?,?,?)",
                params=(usuario.CPF, usuario.nome, usuario.idade, usuario.email, usuario.senha),
            )
        return "Usuário cadastrado com sucesso!"  # Mensagem de sucesso
    
    def verificaLogin(self, usuario: Usuario):
            with DBTransactionManager() as db_manager:
                valor = db_manager.executar_transacao(
                    comando="SELECT * FROM Usuario WHERE email = ? AND senha = ?",
                    params=(usuario.email, usuario.senha),
                    fetchone=True,
            )
            if not valor:
                return None
            return valor
        
    def atualizar(self, usuario: Usuario):
            with DBTransactionManager() as db_manager:
                db_manager.executar_transacao(
                    comando="UPDATE Usuario SET nome = ?, idade = ?, email = ?, senha = ? WHERE CPF = ?",
                    params=(usuario.nome, usuario.idade, usuario.email, usuario.senha, usuario.CPF),
                )
            return "Usuário atualizado com sucesso!"  # Mensagem de sucesso
        
        
    def modificarSenha(self, usuario: Usuario):
            with DBTransactionManager() as db_manager:
                db_manager.executar_transacao(
                    comando="UPDATE Usuario SET senha = ? WHERE CPF = ? ",
                    params=(usuario.senha, usuario.CPF),
                )
            return "Senha atualizada com sucesso!"  # Mensagem de sucesso
