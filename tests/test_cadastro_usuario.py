import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, request
from app.Controller.usuarioController import UsuariosController


class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    @patch("app.Controller.usuarioController.UsuarioDB")
    def test_adicionar_usuario(self, mock_usuario_db):
        mock_usuario = MagicMock()
        mock_usuario.adicionar.return_value = "Usuário cadastrado com sucesso!"
        mock_usuario_db.return_value = mock_usuario

        with self.app.test_request_context(
            "/adicionar_usuario",
            data={
                "CPF": "200",
                "nome": "teste",
                "idade": "25",
                "email": "email@email.com",
                "senha": "senha123",
                "confirmar_senha": "senha123",
            },
        ):
            resultado = UsuariosController.adicionarUsuario()

        mock_usuario.adicionar.assert_called_once()
        self.assertEqual(resultado, "Usuário cadastrado com sucesso!")

    @patch("app.Controller.usuarioController.UsuarioDB")
    def test_adicionar_usuario_erro(self, mock_usuario_db):
        mock_usuario = MagicMock()
        mock_usuario.adicionar.side_effect = Exception("Erro ao cadastrar usuário")
        mock_usuario_db.return_value = mock_usuario

        with self.app.test_request_context(
            "/adicionar_usuario",
            data={
                "CPF": "",
                "nome": "",
                "idade": "",
                "email": "",
                "senha": "",
                "confirmar_senha": "",
            },
        ):
            with self.assertRaises(Exception) as context:
                UsuariosController.adicionarUsuario()

        self.assertEqual(str(context.exception), "Erro ao cadastrar usuário")

    @patch("app.Controller.usuarioController.UsuarioDB")
    def test_atualizar_usuario(self, mock_usuario_db):
        # Configurar mock para atualizar usuário
        mock_usuario = MagicMock()
        mock_usuario.atualizar.return_value = "Usuário atualizado com sucesso!"
        mock_usuario_db.return_value = mock_usuario

        resultado = UsuariosController.atualizarUsuario(
            CPF="200",
            nome="teste2",
            idade="30",
            email="email2@email.com",
            senha="senha123",
        )

        mock_usuario.atualizar.assert_called_once()
        self.assertEqual(resultado, "Usuário atualizado com sucesso!")
