import unittest
from app.Controller.usuario import adicionarUsuario, atualizarUsuario, deletarUsuario

class TestUsuario(unittest.TestCase):

    def test_adicionar_usuario(self):
        # Aqui você chamaria a função real
        resultado = adicionarUsuario('200', 'teste', '25', 'email@email.com')

        # Verifique se o resultado está correto
        self.assertEqual(resultado, "Usuário cadastrado com sucesso!")

    def test_adicionar_usuario_erro(self):
        # Aqui você chamaria a função real
        resultado = adicionarUsuario('', '', '', '')

        # Verifique se o resultado está correto
        self.assertEqual(resultado, "Erro ao cadastrar usuário")

    def test_atualizar_usuario(self):
        # Aqui você chamaria a função real
        resultado = atualizarUsuario('200', 'teste2', '30', 'email2@email.com')

        # Verifique se o resultado está correto
        self.assertEqual(resultado, "Usuário atualizado com sucesso!")

    def test_remover_usuario(self):
        # Aqui você chamaria a função real
        resultado = deletarUsuario('200')

        # Verifique se o resultado está correto
        self.assertEqual(resultado, "Usuário removido com sucesso!")

if __name__ == '__main__':
    unittest.main()