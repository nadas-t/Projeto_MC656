import unittest
from unittest.mock import patch, MagicMock
from app.Model.usuarioModel import UsuarioDB, Usuario
from app.Controller.usuarioController import UsuariosController


class TestUsuarios(unittest.TestCase):

    def setUp(self):
        self.usuario_db = UsuarioDB()

    @patch("app.Model.usuarioModel.BaseDB.executar_transacao")
    def test_adicionar_usuario(self, mock_db):
        mock_db.return_value = True
        usuario = Usuario(CPF="12345678900", nome="Teste", idade=30, email="teste@email.com", senha="senha123")
        response = self.usuario_db.adicionar(usuario)
        self.assertEqual(response, "Usuário cadastrado com sucesso!")
        mock_db.assert_called_with(
            comando="INSERT INTO Usuario (CPF, nome, idade, email, senha) VALUES (?,?,?,?,?)",
            params=("12345678900", "Teste", 30, "teste@email.com", "senha123"),
        )

    @patch("app.Model.usuarioModel.BaseDB.executar_transacao")
    def test_verifica_login_sucesso(self, mock_db):
        mock_db.return_value = (1, "Teste", "teste@email.com", "senha123", 30, None, None, None, "12345678900")
        usuario = Usuario(email="teste@email.com", senha="senha123")
        result = self.usuario_db.verificaLogin(usuario)
        self.assertIsNotNone(result)
        mock_db.assert_called_with(
            comando="SELECT * FROM Usuario WHERE email = ? AND senha = ?",
            params=("teste@email.com", "senha123"),
            fetchone=True,
        )

    @patch("app.Model.usuarioModel.BaseDB.executar_transacao")
    def test_verifica_login_falha(self, mock_db):
        mock_db.return_value = None
        usuario = Usuario(email="teste@email.com", senha="senhaErrada")
        result = self.usuario_db.verificaLogin(usuario)
        self.assertIsNone(result)

    @patch("app.Model.usuarioModel.BaseDB.executar_transacao")
    def test_atualizar_usuario(self, mock_db):
        mock_db.return_value = True
        usuario = Usuario(
            CPF="12345678900", nome="Novo Nome", idade=35, email="novo@email.com",
            senha="novaSenha", salario=5000, limite=2000, horas_trabalho=160
        )
        response = self.usuario_db.atualizar(usuario)
        self.assertEqual(response, "Usuário atualizado com sucesso!")
        mock_db.assert_called_with(
            comando="UPDATE Usuario SET nome = ?, idade = ?, email = ?, senha = ?, salario = ?, limite = ?, horas_trabalho = ? WHERE CPF = ?",
            params=("Novo Nome", 35, "novo@email.com", "novaSenha", 5000, 2000, 160, "12345678900"),
        )

    @patch("app.Model.usuarioModel.BaseDB.executar_transacao")
    def test_modificar_senha(self, mock_db):
        mock_db.return_value = True
        usuario = Usuario(CPF="12345678900", senha="novaSenha")
        response = self.usuario_db.modificarSenha(usuario)
        self.assertEqual(response, "Senha atualizada com sucesso!")
        mock_db.assert_called_with(
            comando="UPDATE Usuario SET senha = ? WHERE CPF = ? ",
            params=("novaSenha", "12345678900"),
        )

    @patch("app.Model.usuarioModel.BaseDB.executar_transacao")
    def test_adicionar_salario(self, mock_db):
        mock_db.return_value = True
        usuario = Usuario(CPF="12345678900", salario=5000, horas_trabalho=160)
        response = self.usuario_db.adicionarSalario(usuario)
        self.assertEqual(response, "Dados financeiros inseridos com sucesso!")
        mock_db.assert_called_with(
            comando="UPDATE Usuario SET salario = ?, horas_trabalho = ? WHERE CPF = ?",
            params=(5000, 160, "12345678900"),
        )


if __name__ == "__main__":
    unittest.main()