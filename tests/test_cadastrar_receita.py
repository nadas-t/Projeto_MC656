import unittest
from unittest.mock import MagicMock
from app.Model.receitasModel import Receitas, ReceitasDB, converte_receita_horas

from app.Model.categoriasModel import Categorias

class TestReceitasDB(unittest.TestCase):
    def setUp(self):
        self.receitas_db = ReceitasDB()
        self.receitas_db._db = MagicMock()
        self.receita = Receitas(
            data="2024-12-01",
            valor=500.0,
            id=1,
            categoria=Categorias(nome="Salário"),
        )
        self.CPF = "12345678900"
        
    def test_converte_receita_horas(self):
        receitas = [
            Receitas(data="2024-12-01", valor=500.0, id=1, categoria=Categorias(nome="Salário")),
            Receitas(data="2024-12-02", valor=1000.0, id=2, categoria=Categorias(nome="Freelance")),
        ]
        receita_por_hora = 50.0

        resultado = converte_receita_horas(receitas, receita_por_hora)

        self.assertEqual(resultado[0].valor, 10.0)  # 500 / 50
        self.assertEqual(resultado[1].valor, 20.0)  # 1000 / 50
        
    def test_registrar_receita(self):
        categoria_id = 1
        self.receitas_db.registrar_receita(categoria_id, self.receita, self.CPF)

        self.receitas_db._db.executar_transacao.assert_called_once_with(
            comando="INSERT INTO Receitas (data, valor, categoria_id, usuario_id) VALUES (?, ?, ?, ?)",
            params=("2024-12-01", 500.0, 1, "12345678900"),
        )
        
    def test_atualizar_receita(self):
        categoria_nome = "Investimento"
        resultado = self.receitas_db.atualizar_receita(categoria_nome, self.receita)

        self.receitas_db._db.executar_transacao.assert_any_call(
            comando="UPDATE Receitas SET data = ?, valor = ? WHERE id = ?",
            params=("2024-12-01", 500.0, 1),
        )

        self.receitas_db._db.executar_transacao.assert_any_call(
            comando="UPDATE Categorias SET nome = ? WHERE id = (SELECT categoria_id FROM Receitas WHERE id = ? LIMIT 1);",
            params=("Investimento", 1),
        )

        self.assertEqual(resultado, "Receita atualizada com sucesso!")
        
    def test_listar_receitas(self):
        self.receitas_db._db.executar_transacao.return_value = [
            (1, "2024-12-01", 500.0, "Salário"),
            (2, "2024-12-02", 1000.0, "Freelance"),
        ]

        resultado = self.receitas_db.listar_receitas(Receitas(), self.CPF)

        self.receitas_db._db.executar_transacao.assert_called_once()
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["valor"], 500.0)
        
    def test_deletar_receita(self):
        receita_id = 1
        resultado = self.receitas_db.deletar_receita(receita_id)

        self.receitas_db._db.executar_transacao.assert_called_once_with(
            comando="DELETE FROM Receitas WHERE id = ?",
            params=(1,),
        )
        self.assertEqual(resultado, "Receita deletada com sucesso!")