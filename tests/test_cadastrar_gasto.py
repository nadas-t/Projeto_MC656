import unittest
from unittest.mock import MagicMock, patch
from app.Model.gastosModel import Gastos, GastosDB, converte_gasto_horas
from app.Model.categoriasModel import Categorias

class TestConverteGastoHoras(unittest.TestCase):
    def test_converte_gasto_horas(self):
        # Dados de entrada
        gastos = [
            Gastos(data="2024-12-01", valor=200.0, id=1, categoria=Categorias(nome="Transporte")),
            Gastos(data="2024-12-01", valor=300.0, id=2, categoria=Categorias(nome="Alimentação")),
        ]
        ganho_por_hora = 50.0

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
        # Configuração inicial
        self.gastos_db = GastosDB()
        self.gastos_db._db = MagicMock()
    
    def test_registrar_gasto(self):
        # Simula a inserção de um gasto
        gasto = Gastos(data="2024-12-01", valor=150.0, id=1)
        CPF = "12345678900"
        categoria_id = 2

        self.gastos_db.registrar_gasto(categoria_id, gasto, CPF)

        self.gastos_db._db.executar_transacao.assert_called_once_with(
            comando="INSERT INTO Gastos (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=("2024-12-01", 150.0, 2, "12345678900"),
        )
    
    def test_atualizar_gasto(self):
        gasto = Gastos(data="2024-12-02", valor=200.0, id=1)
        categoria_nome = "Educação"

        resultado = self.gastos_db.atualizar_gasto(categoria_nome, gasto)

        self.assertEqual(resultado, "Gasto atualizado com sucesso!")

    '''Revisar depois 
    def test_deletar_gasto(self):
        gasto_id = 1

        resultado = self.gastos_db.deletar_gasto(gasto_id)

        self.gastos_db._db.executar_transacao.assert_called_once_with(
            comando="DELETE FROM Gastos WHERE id = ?",
            params=(gasto_id,),
        )
        self.assertEqual(resultado, "Gasto deletado com sucesso!")
    '''