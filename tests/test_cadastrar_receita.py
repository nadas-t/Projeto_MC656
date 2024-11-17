import unittest
from app.Model.receitasModel import (
    Receita,
    ReceitaDB,
    Categoria,
    CategoriaDB,
    ValorDeReceitaInsulficiente,
    NomeCategoriaInvalido,
)
from datetime import datetime
from unittest.mock import patch, MagicMock


class TestRegistrarReceita(unittest.TestCase):

    def test_cadastrar_receita_com_data_de_cadastro(self):
        # when
        receita = Receita(
            data_recebimento="2024-09-26",
            categoria="teste",
            valor=400,
        )
        self.assertIsInstance(receita.data_cadastro, datetime)

    def test_falha_cadastro_receita_com_valor_negativo(self):
        with self.assertRaises(ValorDeReceitaInsulficiente):
            Receita(
                data_recebimento="2024-09-26",
                categoria="teste",
                valor=-100,
            )

    @patch("app.Model.receitasModel.BaseDB")
    def test_cadastrar_receita_com_velha_categoria(self, mock_baseDB):
        mock_db = MagicMock()


class TestRegistrarReceita(unittest.TestCase):
    def setUp(self): ...
