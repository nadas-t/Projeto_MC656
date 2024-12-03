import unittest
from unittest.mock import patch, MagicMock
from app.Model.gastosModel import GastosDB, Gastos
from app.Controller.gastosController import GastosController

class TestGastos(unittest.TestCase):

    def setUp(self):
        self.gasto_db = GastosDB()

    @patch("app.Model.gastosModel.BaseDB.executar_transacao")
    def test_registrar_gasto(self, mock_db):
        mock_db.return_value = True
        gasto = Gastos(data="2024-12-01", valor=100.0)
        response = self.gasto_db.registrar_gasto(1, gasto, "123456789")
        self.assertEqual(response, "Gasto inserido com sucesso!")
        mock_db.assert_called_with(
            comando="INSERT INTO Gastos (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=("2024-12-01", 100.0, 1, "123456789"),
        )

    @patch("app.Model.gastosModel.BaseDB.executar_transacao")
    def test_atualizar_gasto(self, mock_db):
        mock_db.return_value = True
        gasto = Gastos(data="2024-12-01", valor=150.0, id=1)
        response = self.gasto_db.atualizar_gasto("Alimentação", gasto)
        self.assertEqual(response, "Gasto atualizado com sucesso!")
        self.assertEqual(mock_db.call_count, 2)  # Garantir que duas queries foram executadas

    @patch("app.Model.gastosModel.BaseDB.executar_transacao")
    def test_listar_gastos(self, mock_db):
        mock_db.return_value = [
            (1, "2024-12-01", 100.0, "Alimentação"),
            (2, "2024-12-02", 200.0, "Transporte"),
        ]
        gastos = self.gasto_db.listar_gastos(Gastos(id=None), "123456789")
        self.assertEqual(len(gastos), 2)
        self.assertEqual(gastos[0]["data"], "2024-12-01")

    @patch("app.Model.gastosModel.BaseDB.executar_transacao")
    def test_deletar_gasto(self, mock_db):
        mock_db.return_value = True
        response = self.gasto_db.deletar_gasto(1)
        self.assertEqual(response, "Gasto deletado com sucesso!")
        mock_db.assert_called_with(
            comando="DELETE FROM Gastos WHERE id = ?",
            params=(1,),
        )

    @patch("app.Model.gastosModel.BaseDB.executar_transacao")
    def test_listar_gasto_mes(self, mock_db):
        mock_db.return_value = [
            (1, "2024-12-01", 100.0, "Alimentação"),
            (2, "2024-12-15", 200.0, "Transporte"),
        ]
        gastos = self.gasto_db.listar_gasto_mes("12", "123456789")
        self.assertEqual(len(gastos), 2)
        self.assertEqual(gastos[1]["data"], "2024-12-15")


if __name__ == "__main__":
    unittest.main()