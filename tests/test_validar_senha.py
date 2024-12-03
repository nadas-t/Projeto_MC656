import unittest
from parameterized import parameterized
from app.Controller.usuarioController import UsuariosController

class TestUsuariosController(unittest.TestCase):

    # A senha correta no seu código deve ter pelo menos 8 caracteres, uma letra maiúscula, um número e um caractere especial.
    
    @parameterized.expand([
        ("senha válida", "Senha1@123", True, []),
        ("senha com menos de 8 caracteres", "Senha1@", False, ["Sua senha deve ter 8 ou mais caracteres."]),
        ("senha sem letra maiúscula", "senha123@", False, ["Sua senha deve ter ao menos 1 letra maiúscula."]),
        ("senha sem número", "Senha@abc", False, ["Sua senha deve ter ao menos 1 número."]),
        ("senha sem caractere especial", "Senha1234", False, ["Sua senha deve ter ao menos 1 caractere especial."]),
          ])
    def test_validar_senha(self, descricao, senha, esperado_resultado, esperado_erros):
        resultado, erros = UsuariosController.validar_senha(senha)
        self.assertEqual(resultado, esperado_resultado, f"Falha no teste: {descricao}")
        self.assertEqual(erros, esperado_erros, f"Falha no teste: {descricao}")

if __name__ == '__main__':
    unittest.main()
