import unittest
from unittest.mock import MagicMock
from app.Model.usuarioModel import Usuario, UsuarioDB

class TestUsuarioDB(unittest.TestCase):
    def setUp(self):
        # Inicializa o modelo e substitui o banco de dados por um mock
        self.usuario_db = UsuarioDB()
        self.usuario_db._db = MagicMock()
        self.usuario = Usuario(
            nome="João Silva",
            email="joao@email.com",
            senha="senha123",
            idade=30,
            salario=3000.0,
            limite=1000.0,
            horas_trabalho=40.0,
            CPF="12345678900"
        )

    def test_adicionar(self):
        # Testa a adição de um novo usuário
        resultado = self.usuario_db.adicionar(self.usuario)

        self.usuario_db._db.executar_transacao.assert_called_once_with(
            comando="INSERT INTO Usuario (CPF, nome, idade, email, senha) VALUES (?,?,?,?,?)",
            params=("12345678900", "João Silva", 30, "joao@email.com", "senha123"),
        )
        self.assertEqual(resultado, "Usuário cadastrado com sucesso!")
        
    def test_verifica_login(self):
        # Mock do retorno do banco de dados
        self.usuario_db._db.executar_transacao.return_value = {
            "CPF": "12345678900",
            "nome": "João Silva",
        }

        resultado = self.usuario_db.verificaLogin(self.usuario)

        self.usuario_db._db.executar_transacao.assert_called_once_with(
            comando="SELECT * FROM Usuario WHERE email = ? AND senha = ?",
            params=("joao@email.com", "senha123"),
            fetchone=True,
        )
        self.assertIsNotNone(resultado)
        
    def test_atualizar(self):
        resultado = self.usuario_db.atualizar(self.usuario)

        self.usuario_db._db.executar_transacao.assert_called_once_with(
            comando="UPDATE Usuario SET nome = ?, idade = ?, email = ?, senha = ?, salario = ?, limite = ?, horas_trabalho = ? WHERE CPF = ?",
            params=(
                "João Silva",
                30,
                "joao@email.com",
                "senha123",
                3000.0,
                1000.0,
                40.0,
                "12345678900",
            ),
        )
        self.assertEqual(resultado, "Usuário atualizado com sucesso!")
        
    def test_modificar_senha(self):
        self.usuario.senha = "novaSenha123"
        resultado = self.usuario_db.modificarSenha(self.usuario)

        self.usuario_db._db.executar_transacao.assert_called_once_with(
            comando="UPDATE Usuario SET senha = ? WHERE CPF = ? ",
            params=("novaSenha123", "12345678900"),
        )
        self.assertEqual(resultado, "Senha atualizada com sucesso!")
        
    def test_adicionar_salario(self):
        resultado = self.usuario_db.adicionarSalario(self.usuario)

        self.usuario_db._db.executar_transacao.assert_called_once_with(
            comando="UPDATE Usuario SET salario = ?, horas_trabalho = ? WHERE CPF = ?",
            params=(3000.0, 40.0, "12345678900"),
        )
        self.assertEqual(resultado, "Dados financeiros inseridos com sucesso!")