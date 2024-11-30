import unittest
from unittest.mock import patch, MagicMock
from app.Model.gastosModel import GastosDB, Gastos, Categorias


class TestGastosDB(unittest.TestCase):
    @patch("app.Model.databaseManager.BaseDB")
    def test_adicionar_gasto_com_categoria_existente(self, mock_base_db):
        mock_db = MagicMock()
        mock_base_db.return_value = mock_db
        mock_db.executar_transacao.side_effect = [
            (1,),
        ]

        db = GastosDB()
        gasto = Gastos(data="2024-09-26", valor=100.50)
        categoria = Categorias(nome="Transporte")
        resultado = db.adicionar_gasto(gasto, categoria)

        mock_db.executar_transacao.assert_any_call(
            comando="SELECT id FROM Categorias WHERE nome = ?",
            params=("Transporte",),
            fetchone=True,
        )
        mock_db.executar_transacao.assert_any_call(
            comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            params=("2024-09-26", 100.50, 1),
        )
        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @patch("app.Model.databaseManager.BaseDB")
    def test_adicionar_gasto_com_categoria_nova(self, mock_base_db):
        mock_db = MagicMock()
        mock_base_db.return_value = mock_db
        mock_db.executar_transacao.side_effect = [
            None,
            None,
            (4,),
        ]

        db = GastosDB()
        gasto = Gastos(data="2024-09-26", valor=100.50)
        categoria = Categorias(nome="Viagem")
        resultado = db.adicionar_gasto(gasto, categoria)

        mock_db.executar_transacao.assert_any_call(
            comando="SELECT id FROM Categorias WHERE nome = ?",
            params=("Viagem",),
            fetchone=True,
        )
        mock_db.executar_transacao.assert_any_call(
            comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            params=("2024-09-26", 100.50, 4),
        )
        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @patch("app.Model.databaseManager.BaseDB")
    def test_listar_gasto_especificado(self, mock_base_db):
        mock_db = MagicMock()
        mock_base_db.return_value = mock_db
        mock_db.executar_transacao.return_value = [
            (1, "2024-09-26", 100.50, "Transporte"),
        ]

        db = GastosDB()
        gasto = Gastos(id=1)
        resultado = db.listar_gastos(gasto)

        mock_db.executar_transacao.assert_called_with(
            comando=(
                "SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                "FROM Gastos "
                "JOIN Categorias ON Gastos.categoria_id = Categorias.id WHERE gasto_id = ?"
            ),
            params=(1,),
        )
        self.assertEqual(
            resultado,
            [
                {
                    "id": 1,
                    "data": "2024-09-26",
                    "valor": 100.50,
                    "categoria_nome": "Transporte",
                },
            ],
        )

    @patch("app.Model.databaseManager.BaseDB")
    def test_listar_todos_os_gastos(self, mock_base_db):
        mock_db = MagicMock()
        mock_base_db.return_value = mock_db
        mock_db.executar_transacao.return_value = [
            (1, "2024-09-26", 100.50, "Transporte"),
            (2, "2024-08-12", 110.50, "Alimentação"),
        ]

        db = GastosDB()
        resultado = db.listar_gastos(Gastos())

        mock_db.executar_transacao.assert_called_with(
            comando=(
                "SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
                "FROM Gastos "
                "JOIN Categorias ON Gastos.categoria_id = Categorias.id"
            ),
        )
        self.assertEqual(
            resultado,
            [
                {
                    "id": 1,
                    "data": "2024-09-26",
                    "valor": 100.50,
                    "categoria_nome": "Transporte",
                },
                {
                    "id": 2,
                    "data": "2024-08-12",
                    "valor": 110.50,
                    "categoria_nome": "Alimentação",
                },
            ],
        )
