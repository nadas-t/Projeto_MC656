import unittest
from unittest.mock import patch, MagicMock
from app.Model.receitasModel import ReceitasDB, Receitas
from app.Controller.receitasController import ReceitasController


class TestReceitas(unittest.TestCase):

    def setUp(self):
        self.receita_db = ReceitasDB()

    @patch("app.Model.receitasModel.BaseDB.executar_transacao")
    def test_registrar_receita(self, mock_db):
        mock_db.return_value = True
        receita = Receitas(data="2024-12-01", valor=500.0)
        response = self.receita_db.registrar_receita(1, receita, "123456789")
        self.assertEqual(response, "Receita cadastrada com sucesso!")
        mock_db.assert_called_with(
            comando="INSERT INTO Receitas (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=("2024-12-01", 500.0, 1, "123456789"),
        )

    @patch("app.Model.receitasModel.BaseDB.executar_transacao")
    def test_atualizar_receita(self, mock_db):
        mock_db.return_value = True
        receita = Receitas(data="2024-12-02", valor=750.0, id=1)
        response = self.receita_db.atualizar_receita("Investimento", receita)
        self.assertEqual(response, "Receita atualizada com sucesso!")
        self.assertEqual(mock_db.call_count, 2)  # Garantir que duas queries foram executadas

    @patch("app.Model.receitasModel.BaseDB.executar_transacao")
    def test_listar_receitas(self, mock_db):
        mock_db.return_value = [
            (1, "2024-12-01", 500.0, "Salário"),
            (2, "2024-12-05", 300.0, "Freelance"),
        ]
        receitas = self.receita_db.listar_receitas(Receitas(id=None), "123456789")
        self.assertEqual(len(receitas), 2)
        self.assertEqual(receitas[0]["data"], "2024-12-01")

    @patch("app.Model.receitasModel.BaseDB.executar_transacao")
    def test_deletar_receita(self, mock_db):
        mock_db.return_value = True
        response = self.receita_db.deletar_receita(1)
        self.assertEqual(response, "Receita deletada com sucesso!")
        mock_db.assert_called_with(
            comando="DELETE FROM Receitas WHERE id = ?",
            params=(1,),
        )

if __name__ == "__main__":
    unittest.main()