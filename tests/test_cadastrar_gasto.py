import unittest
from unittest.mock import patch, MagicMock
# from app.Model.gastosModel import adicionar_gasto, listar_gastos


class TestRegistrarGasto(unittest.TestCase):

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")
    
    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    # a função adicionar nao existe mais
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_existente(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = (1,)
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur

        resultado = adicionar_gasto("2024-09-26", "100.50", "Transporte")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Transporte",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 1),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    @patch("app.Model.gastosModel.conexao")
    def test_adicionar_gasto_com_categoria_nova(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_cur.fetchone.return_value = None
        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur
        mock_cur.lastrowid = 4

        resultado = adicionar_gasto("2024-09-26", "100.50", "Viagem")

        mock_cur.execute.assert_any_call(
            "SELECT id FROM Categorias WHERE nome = ?", ("Viagem",)
        )
        mock_cur.execute.assert_any_call(
            "INSERT INTO Gastos (data, valor, categoria_id) VALUES (?, ?, ?)",
            ("2024-09-26", "100.50", 4),
        )

        self.assertEqual(resultado, "Gasto adicionado com sucesso!")

    @unittest.skip("Teste ainda em desenvolvimento")
    @patch("app.Model.gastosModel.conexao")
    def test_listar_gasto_especificado(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur
        mock_cur.fetchone.return_value = [
            {"id": 1, "data": "2024-09-26", "valor": "100.50", "categoria_id": 1},
        ]
        gasto_id = 1
        resultado = listar_gastos(gasto_id)

        mock_cur.execute.assert_any_call(
            "SELECT * FROM Gastos WHERE id = ?", (gasto_id,)
        )
        self.assertEqual(
            resultado,
            [{"id": 1, "data": "2024-09-26", "valor": "100.50", "categoria_id": 1}],
        )

    
    @unittest.skip("Teste ainda em desenvolvimento")
    @patch("app.Model.gastosModel.conexao")
    def test_listar_todos_os_gastos(self, mock_conexao):
        mock_con = MagicMock()
        mock_cur = MagicMock()

        mock_conexao.return_value = mock_con
        mock_con.cursor.return_value = mock_cur
        mock_cur.fetchall.return_value = [
            {"id": 1, "data": "2024-09-26", "valor": "100.50", "categoria_id": 1},
            {"id": 2, "data": "2024-08-12", "valor": "110.50", "categoria_id": 2},
        ]
        resultado = listar_gastos()

        mock_cur.execute.assert_any_call("SELECT * FROM Gastos")
        self.assertEqual(
            resultado,
            [
                {"id": 1, "data": "2024-09-26", "valor": "100.50", "categoria_id": 1},
                {"id": 2, "data": "2024-08-12", "valor": "110.50", "categoria_id": 2},
            ],
        )
