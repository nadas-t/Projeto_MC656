import unittest
from unittest.mock import patch, MagicMock
from app.Model.gastosModel import GastosDB, Gastos
from app.Controller.gastosController import GastosController

class TestGastos(unittest.TestCase):


        # Executa a função
        resultado = converte_gasto_horas(gastos, ganho_por_hora)

        # Verifica os resultados
        self.assertEqual(resultado[0].valor, 4.0)  # 200 / 50
        self.assertEqual(resultado[1].valor, 6.0)  # 300 / 50
        
class TestGastosDB(unittest.TestCase):

    # @patch("app.Model.gastosModel.DBTransactionManager")
    # @patch("app.Model.gastosModel.CategoriasDB")
    # @patch("app.Model.gastosModel.BaseDB")
    # def test_registrar_gasto_com_categoria_existente(
    #     self, mock_basedb, mock_categoriasdb, mock_transaction
    # ):
    #     mock_db = MagicMock()
    #     mock_categorias = MagicMock()

    #     # Mocking the database and category behavior
    #     mock_basedb.return_value = mock_db
    #     mock_categoriasdb.return_value = mock_categorias
    #     mock_categorias.vincular_categoria.return_value = 1  # Categoria já existe

    #     gastos_db = GastosDB()
    #     gasto = Gastos(data="2024-09-26", valor=100.50)

    #     gastos_db.registrar_gasto_com_transacao(gasto, Categorias(nome="Transporte"))

    #     mock_categorias.vincular_categoria.assert_called_with(
    #         Categorias(nome="Transporte")
    #     )
    #     mock_db.executar_transacao.assert_called_with(
    #         comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
    #         params=("2024-09-26", 100.50, 1),
    #     )

    # @patch("app.Model.gastosModel.DBTransactionManager")
    # @patch("app.Model.gastosModel.CategoriasDB")
    # @patch("app.Model.gastosModel.BaseDB")
    # def test_registrar_gasto_com_categoria_nova(
    #     self, mock_basedb, mock_categoriasdb, mock_transaction
    # ):
    #     mock_db = MagicMock()
    #     mock_categorias = MagicMock()

    #     # Mocking the database and category behavior
    #     mock_basedb.return_value = mock_db
    #     mock_categoriasdb.return_value = mock_categorias
    #     mock_categorias.vincular_categoria.return_value = 4  # Nova categoria

    #     gastos_db = GastosDB()
    #     gasto = Gastos(data="2024-09-26", valor=100.50)

    #     gastos_db.registrar_gasto_com_transacao(gasto, Categorias(nome="Viagem"))

    #     mock_categorias.vincular_categoria.assert_called_with(Categorias(nome="Viagem"))
    #     mock_db.executar_transacao.assert_called_with(
    #         comando="INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
    #         params=("2024-09-26", 100.50, 4),
    #     )

    # @patch("app.Model.gastosModel.DBTransactionManager")
    # @patch("app.Model.gastosModel.BaseDB")
    # def test_listar_gasto_especificado(self, mock_basedb, mock_transaction):
    #     mock_db = MagicMock()
    #     mock_basedb.return_value = mock_db

    #     # Mocking query results
    #     mock_db.executar_transacao.return_value = [
    #         (1, "2024-09-26", 100.50, "Transporte")
    #     ]

    #     gastos_db = GastosDB()
    #     gasto = Gastos(id=1)

    #     resultado = gastos_db.listar_gastos(gasto)

    #     mock_db.executar_transacao.assert_called_with(
    #         comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
    #         "FROM Gastos "
    #         "JOIN Categorias ON Gastos.categoria_id = Categorias.id WHERE gasto_id = ?",
    #         params=(1,),
    #     )
    #     self.assertEqual(
    #         resultado,
    #         [
    #             {
    #                 "id": 1,
    #                 "data": "2024-09-26",
    #                 "valor": 100.50,
    #                 "categoria_nome": "Transporte",
    #             },
    #         ],
    #     )

    # @patch("app.Model.gastosModel.DBTransactionManager")
    # @patch("app.Model.gastosModel.BaseDB")
    # def test_listar_todos_os_gastos(self, mock_basedb, mock_transaction):
    #     mock_db = MagicMock()
    #     mock_basedb.return_value = mock_db

    #     # Mocking query results
    #     mock_db.executar_transacao.return_value = [
    #         (1, "2024-09-26", 100.50, "Transporte"),
    #         (2, "2024-08-12", 110.50, "Viagem"),
    #     ]

    #     gastos_db = GastosDB()
    #     gasto = Gastos()

    #     resultado = gastos_db.listar_gastos(gasto)

    #     mock_db.executar_transacao.assert_called_with(
    #         comando="SELECT Gastos.id AS gasto_id, data, valor, Categorias.nome AS categoria_nome "
    #         "FROM Gastos "
    #         "JOIN Categorias ON Gastos.categoria_id = Categorias.id"
    #     )
    #     self.assertEqual(
    #         resultado,
    #         [
    #             {
    #                 "id": 1,
    #                 "data": "2024-09-26",
    #                 "valor": 100.50,
    #                 "categoria_nome": "Transporte",
    #             },
    #             {
    #                 "id": 2,
    #                 "data": "2024-08-12",
    #                 "valor": 110.50,
    #                 "categoria_nome": "Viagem",
    #             },
    #         ],
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