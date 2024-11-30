import unittest
from unittest.mock import patch, MagicMock
from app.Model.gastosModel import Gastos, GastosDB
from app.Model.categoriasModel import Categorias


class TestGastosDB(unittest.TestCase):

    @patch("app.Model.gastosModel.DBTransactionManager")
    @patch("app.Model.gastosModel.CategoriasDB")
    @patch("app.Model.gastosModel.BaseDB")
    def test_registrar_gasto_com_categoria_existente(
        self, mock_basedb, mock_categoriasdb, mock_transaction
    ):
        mock_db = MagicMock()
        mock_categorias = MagicMock()

        # Mocking the database and category behavior
        mock_basedb.return_value = mock_db
        mock_categoriasdb.return_value = mock_categorias
        mock_categorias.vincular_categoria.return_value = 1  # Categoria já existe

        gastos_db = GastosDB()
        gasto = Gastos(data="2024-09-26", valor=100.50)

        gastos_db.registrar_gasto_com_transacao(gasto, Categorias(nome="Transporte"))

        mock_categorias.vincular_categoria.assert_called_with(
            Categorias(nome="Transporte")
        )
        mock_db.executar_transacao.assert_called_with(
            comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            params=("2024-09-26", 100.50, 1),
        )

    @patch("app.Model.gastosModel.DBTransactionManager")
    @patch("app.Model.gastosModel.CategoriasDB")
    @patch("app.Model.gastosModel.BaseDB")
    def test_registrar_gasto_com_categoria_nova(
        self, mock_basedb, mock_categoriasdb, mock_transaction
    ):
        mock_db = MagicMock()
        mock_categorias = MagicMock()

        # Mocking the database and category behavior
        mock_basedb.return_value = mock_db
        mock_categoriasdb.return_value = mock_categorias
        mock_categorias.vincular_categoria.return_value = 4  # Nova categoria

        gastos_db = GastosDB()
        gasto = Gastos(data="2024-09-26", valor=100.50)

        gastos_db.registrar_gasto_com_transacao(gasto, Categorias(nome="Viagem"))

        mock_categorias.vincular_categoria.assert_called_with(Categorias(nome="Viagem"))
        mock_db.executar_transacao.assert_called_with(
            comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            params=("2024-09-26", 100.50, 4),
        )

    @patch("app.Model.gastosModel.DBTransactionManager")
    @patch("app.Model.gastosModel.BaseDB")
    def test_listar_gasto_especificado(self, mock_basedb, mock_transaction):
        mock_db = MagicMock()
        mock_basedb.return_value = mock_db

        # Mocking query results
        mock_db.executar_transacao.return_value = [
            (1, "2024-09-26", 100.50, "Transporte")
        ]

        gastos_db = GastosDB()
        gasto = Gastos(id=1)

        resultado = gastos_db.listar_gastos(gasto)

        mock_db.executar_transacao.assert_called_with(
            comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
            "FROM Gastos "
            "JOIN Categorias ON Gastos.categoria_id = Categorias.id WHERE gasto_id = ?",
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

    @patch("app.Model.gastosModel.DBTransactionManager")
    @patch("app.Model.gastosModel.BaseDB")
    def test_listar_todos_os_gastos(self, mock_basedb, mock_transaction):
        mock_db = MagicMock()
        mock_basedb.return_value = mock_db

        # Mocking query results
        mock_db.executar_transacao.return_value = [
            (1, "2024-09-26", 100.50, "Transporte"),
            (2, "2024-08-12", 110.50, "Viagem"),
        ]

        gastos_db = GastosDB()
        gasto = Gastos()

        resultado = gastos_db.listar_gastos(gasto)

        mock_db.executar_transacao.assert_called_with(
            comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
            "FROM Gastos "
            "JOIN Categorias ON Gastos.categoria_id = Categorias.id"
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
                    "categoria_nome": "Viagem",
                },
            ],
        )
